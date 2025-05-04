import argparse
import json
import logging
import os
import re
import time
import urllib.request
import urllib.error

from http.cookiejar import CookieJar
from queue import Queue
from threading import Thread, Event
from urllib.parse import urlparse

logging.basicConfig(level=logging.INFO, format='[%(asctime)s %(levelname)s] %(message)s', datefmt='%I:%M%p')

def parse_response(response: urllib.response):
    """
    Helpers to parse the response from the Canvas API.  May be html or json.
    """
    if 'application/json' in response.headers.get('Content-Type'):
        return json.loads(response.read().decode('utf-8'))
    elif 'text/html' in response.headers.get('Content-Type'): # need to parse the html, hence why it's slower than api (bigger payloads)
        ret = response.read().decode('utf-8')
        display_name = re.search(r'Download (.*?)</a>', ret)
        if not display_name:
            raise Exception('Error parsing display name from response')
        display_name = display_name.group(1)

        path = re.search(r'<a href="([^"]*?/files/\d+)"', ret)
        if not path:
            raise Exception('Error parsing url from response')
        path = path.group(1)
        parsed = urlparse(response.geturl())
        url = f'{parsed.scheme}://{parsed.netloc}{path}'
        return {
            'display_name': display_name,
            'created_at': '',
            'url': url + '/download?download_frd=1'
        }   
    else:
        raise Exception(f'Unexpected content type: {response.headers.get("Content-Type")}')

def sweep_files_reverse(start: int,
                        increment: int, 
                        stop: int,
                        url: str, 
                        **kwargs):
    """
    Polls url, starting from file_id = start - 1 (skipping start)
    and decrementing by increment. Stops when it reaches file_id = stop.

    For each file_id, it sends a GET request to the URL:
        if 200 (OK), file found, add to queue. 
        if 404 (not found), continue exploring
        otherwise, stop the thread and return the queue.
    
    Example:
    >> sweep_files_reverse(start=10, increment=2, url='https://example.com/files', stop=0)
    would create the following threads:
    Thread 1: will explore the odd file_ids:
        https://example.com/files/9
        https://example.com/files/7
        ...
    Thread 2: will explore the even file_ids:
        https://example.com/files/8
        https://example.com/files/6
        ...
    Both will stop when one of them reaches file_id = 0. That is,
    Thread 1 will stop at file_id = 1
    Thread 2 will stop at file_id = 0

    By decrementing by the number of threads, we guarantee that
    we can explore all file_ids in the range (stop, start].
    """
    assert start > stop, "start must be greater than stop"
    stop_signal = Event()
    queue = Queue()

    def process(start: int, increment: int, stop: int, url: str):
        start_time = time.time()
        for i in range(start, stop - 1, increment):
            if stop_signal.is_set(): return

            try:
                request = urllib.request.Request(f'{url}/{i}')
                response = urllib.request.urlopen(request)
                
                response_data = parse_response(response)
                
                logging.info(f'FOUND: {url}/{i}')
                
                queue.put({
                    'id': i,
                    'url': f"{url.replace('/api/v1', '')}/{i}",
                    'display_name': response_data.get('display_name'),
                    'created_at': response_data.get('created_at'),
                    'download_url': response_data.get('url')
                })
                
            except urllib.error.HTTPError as e:
                if e.code != 404:  # we expect majority of errors to be 404
                    if e.code == 401: logging.error('Unauthorized access. Please get a new token.')
                    if e.code == 403 and '(Rate Limit Exceeded)' in e.read().decode('utf-8'): logging.error('Rate limit exceeded. Please reduce number of threads.')
                    logging.error(f'Status Code: {e.code} for {url}/{i}')
                    # print(f'Error body: {e.read().decode("utf-8")}')
                    stop_signal.set()
                    return
                if i % kwargs['log_every'] == 0:
                    time_per_item = (time.time() - start_time) / max(start - i, 1)
                    logging.info(f'Status: {e.code} -- File Id: {i} -- TMR: {time_per_item * (i - stop) / 60:.2f} min')
                continue
            except Exception as e:
                logging.error(f'Unexpected error for File Id: {i} --> {str(e)}')
                stop_signal.set()
                return

    threads = [ 
        Thread(target=process, 
                args=(
                        start + (i * -1) - 1, # skip start
                        increment * -1, 
                        stop,
                        url
                    )) for i in range(increment) 
    ]
    
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    found_files = []
    while not queue.empty():
        found_files.append(queue.get())
    return found_files

def try_frontend(url: str):
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        response_data = response.read().decode('utf-8')
        if "Log into Canvas" in response_data:
            logging.error('Unauthorized access. Please check your canvas session token.')
            exit(1)
        # print(f'Frontend URL is valid, status code: {response.status}')
        logging.info(f'Frontend URL is valid, status code: {response.status}')
    except urllib.error.HTTPError as e:
        if e.code == 401:
            logging.error('Unauthorized access. Please check your canvas session token.')
            exit(1)
        if e.code == 404:
            logging.info(f'Frontend URL is valid, status code: {e.code}') # TODO: don't let 404s pass



def main():
    def validate_url(url):
        try:
            parsed_url = urlparse(url)
            if not all([parsed_url.scheme, parsed_url.netloc]):
                raise argparse.ArgumentTypeError("Invalid URL format")
        except ValueError:
            raise argparse.ArgumentTypeError("Invalid URL format")
        
        pattern = re.compile(r'files/(\d+)')
        match = pattern.search(url)
        if not match:
            raise argparse.ArgumentTypeError("URL does not contain a valid file ID (e.g. /files/123)")
        return url

    env_canvas_session = os.environ.get('CANVAS_SESSION')

    parser = argparse.ArgumentParser(description='Canvas file sweeper')
    parser.add_argument('-u', '--url', 
                        type=validate_url,
                        required=True, 
                        help='The URL of the file to start from, e.g. https://canvas.example.edu/courses/123/files/456')
    parser.add_argument('-f', '--num-files', 
                        type=lambda x: max(int(x), 1), # limit to 1 or more
                        default=10000,
                        help='Number of files to scan (default 10000, min 1)')
    parser.add_argument('-s', '--canvas-session', 
                        type=str, 
                        required=not bool(env_canvas_session), 
                        default=env_canvas_session,
                        help='The Canvas API canvas session, provided as an environment variable or command line argument.  If not provided, the script will use the CANVAS_SESSION environment variable.')
    parser.add_argument('-w', '--num-workers', 
                        type=lambda x: min(max(int(x), 1), 32), # limit to 1-32 workers
                        default=16, 
                        help='Number of threads to use (default 16, max 32)')
    parser.add_argument('-l', '--log-every', 
                        type=lambda x: max(int(x), 1), # limit to 1 or more
                        default=1000,  
                        help='Log every (X) files found (default 1000, min 1)')
    parser.add_argument('--use-api', 
                        action='store_true', 
                        help='Experimental: Use the Canvas API instead of the frontend (default: False) - this will be faster but may not necessarily find all files.  See README for more details.')
    args = parser.parse_args()

    # check if canvas session is provided
    if not args.canvas_session:
        parser.error("Canvas session token must be provided either via --canvas-session or the CANVAS_SESSION environment variable")


    # processing the URL
    url = args.url.rstrip('/') # remove trailing slash if present
    if args.use_api:
        logging.info('Using API, this may be faster but may not find all files.')
        parsed_url = urlparse(url)
        url = f'https://{parsed_url.netloc}/api/v1{parsed_url.path}'

    start = int(re.search(r'files/(\d+)', url).group(1)) 
    url = re.sub(r'files/\d+', '', url) # remove the file id from the URL
    url = url.rstrip('/')
    url = f'{url}/files'
    

    # inject the canvas canvas session 
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(CookieJar()))
    opener.addheaders = [
        ('Cookie', f'canvas_session={args.canvas_session}'),
        ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'),
    ]
    urllib.request.install_opener(opener)
    
    # print(
    #     f'Using URL: {url}\n',
    #     f'Using canvas session: {args.canvas_session}\n',
    #     f'Using num files: {args.num_files}\n',
    #     f'Using log every: {args.log_every}\n',
    #     f'Using num workers: {args.num_workers}\n',
    #     f'Using use_api: {args.use_api}\n'
    # )
    
    try_frontend(args.url)
        
    results = sweep_files_reverse(
        start=start,
        increment=args.num_workers,
        stop=start - args.num_files,
        url=url,
        log_every=args.log_every
    )

    results = sorted(results, key=lambda x: x.get('id'), reverse=True)
    os.makedirs('output', exist_ok=True)
    output_file = os.path.join('output', f'{time.strftime("%Y%m%d-%H%M%S")}-canvas-files.json')
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)



if __name__ == "__main__":
    main()
