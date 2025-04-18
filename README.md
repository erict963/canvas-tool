# Canvas File Explorer

A tool to explore a canvas course, and potentially find homework solutions and exams from previous semesters. **This does not work for every course.** This only works if a professor re-initializes a course that he/she has taught before.

**[<svg xmlns="http://www.w3.org/2000/svg"   style="vertical-align: middle;" viewBox="0 0 48 48" width="24px" height="24px"><path fill="#f44336" d="M42,37c0,2.762-2.238,5-5,5H11c-2.761,0-5-2.238-5-5V11c0-2.762,2.239-5,5-5h26c2.762,0,5,2.238,5,5 V37z"/><path fill="#fff" d="M36.499,25.498c-0.276-0.983-1.089-1.758-2.122-2.021C32.506,23,24,23,24,23s-8.506,0-10.377,0.478 c-1.032,0.263-1.846,1.037-2.122,2.021C11,27.281,11,31,11,31s0,3.719,0.501,5.502c0.276,0.983,1.089,1.758,2.122,2.021 C15.494,39,24,39,24,39s8.505,0,10.377-0.478c1.032-0.263,1.846-1.037,2.122-2.021C37,34.719,37,31,37,31S37,27.281,36.499,25.498z"/><path fill="#f44336" d="M16.333 37L14.667 37 14.667 26.655 13 26.655 13 25 18 25 18 26.655 16.333 26.655zM23 37h-1.5l-.167-1.132C20.675 36.579 19.892 37 19.283 37c-.533 0-.908-.231-1.092-.653C18.083 36.083 18 35.687 18 35.092V27.5h1.667v7.757c.042.24.217.33.433.33.333 0 .867-.363 1.233-.843V27.5H23V37zM35 32.663v-2.701c0-.777-.192-1.338-.533-1.702-.458-.496-1.117-.76-1.942-.76-.842 0-1.492.264-1.967.76C30.2 28.623 30 29.218 30 29.995v4.593c0 .768.225 1.313.575 1.669C31.05 36.752 31.7 37 32.567 37c.858 0 1.533-.256 1.983-.785.2-.231.333-.496.392-.785C34.95 35.298 35 34.943 35 34.522h-1.667v.661c0 .38-.375.694-.833.694s-.833-.314-.833-.694v-2.52H35zM31.667 29.392c0-.388.375-.694.833-.694s.833.306.833.694v2.123h-1.667V29.392zM28.783 28.492c-.208-.646-.717-1.001-1.35-1.01-.808-.008-1.142.414-1.767 1.142V25H24v12h1.5l.167-1.034C26.192 36.611 26.875 37 27.433 37c.633 0 1.175-.331 1.383-.977.1-.348.175-.67.183-1.399V30.28C29 29.461 28.892 28.84 28.783 28.492zM27.333 34.41c0 .869-.2 1.167-.65 1.167-.258 0-.75-.174-1.017-.439v-5.686c.267-.265.758-.521 1.017-.521.45 0 .65.273.65 1.142V34.41z"/><path fill="#fff" d="M15 9l1.835.001 1.187 5.712.115 0 1.128-5.711 1.856-.001L19 16.893V21h-1.823l-.003-3.885L15 9zM21.139 14.082c0-.672.219-1.209.657-1.606.437-.399 1.024-.6 1.764-.601.675 0 1.225.209 1.655.63.429.418.645.96.645 1.622l.003 4.485c0 .742-.209 1.326-.63 1.752C24.812 20.788 24.234 21 23.493 21c-.714 0-1.281-.221-1.712-.656-.428-.435-.64-1.023-.641-1.76l-.003-4.503L21.139 14.082 21.139 14.082zM22.815 18.746c0 .236.057.423.178.553.115.128.279.193.495.193.221 0 .394-.066.524-.201.129-.129.196-.314.196-.547l-.003-4.731c0-.188-.069-.342-.201-.459-.131-.116-.305-.175-.519-.175-.199 0-.361.06-.486.176-.124.117-.186.271-.186.459L22.815 18.746zM32 12v9h-1.425l-.227-1.1c-.305.358-.622.63-.953.815C29.067 20.901 28.747 21 28.437 21c-.384 0-.671-.132-.866-.394-.195-.259-.291-.65-.291-1.174L27.276 12h1.653l.004 6.825c0 .204.036.355.106.449.066.09.183.14.335.14.124 0 .278-.062.46-.186.188-.122.358-.281.512-.471L30.344 12 32 12z"/></svg> Video demo](https://youtu.be/7f0Lu8lJ3iI)**

**[<svg xmlns="http://www.w3.org/2000/svg"  style="vertical-align: middle;" viewBox="0 0 48 48" width="24px" height="24px"><radialGradient id="La9SoowKGoEUHOnYdJMSEa" cx="24" cy="10.009" r="32.252" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#8c9eff"/><stop offset=".368" stop-color="#889af8"/><stop offset=".889" stop-color="#7e8fe6"/><stop offset="1" stop-color="#7b8ce1"/></radialGradient><path fill="url(#La9SoowKGoEUHOnYdJMSEa)" d="M40.107,12.15c-0.065-0.102-0.139-0.182-0.236-0.255c-0.769-0.578-4.671-3.339-9.665-3.875	c-0.01-0.001-0.048-0.003-0.057-0.003c-0.098,0-0.183,0.057-0.224,0.14l-0.269,0.538c0,0-0.001,0-0.001,0	c-0.017,0.033-0.026,0.071-0.026,0.111c0,0.109,0.07,0.202,0.168,0.236c0.006,0.002,0.048,0.011,0.063,0.014	c4.267,1.028,6.863,2.89,9.149,4.945c-4.047-2.066-8.044-4.001-15.009-4.001s-10.961,1.936-15.009,4.001	c2.286-2.055,4.882-3.917,9.149-4.945c0.015-0.004,0.057-0.012,0.063-0.014c0.098-0.034,0.168-0.127,0.168-0.236	c0-0.04-0.009-0.078-0.026-0.111c0,0-0.001,0-0.001,0l-0.269-0.538c-0.041-0.083-0.125-0.14-0.224-0.14	c-0.009,0-0.048,0.002-0.057,0.003c-4.994,0.536-8.896,3.297-9.665,3.875c-0.097,0.073-0.17,0.153-0.236,0.255	c-0.708,1.107-5.049,8.388-5.892,21.632c-0.009,0.142,0.04,0.289,0.135,0.395c4.592,5.144,11.182,5.752,12.588,5.823	c0.167,0.008,0.327-0.065,0.427-0.199l1.282-1.709c0.1-0.134,0.046-0.322-0.111-0.379c-2.705-0.986-5.717-2.7-8.332-5.706	C11.231,34.457,16.12,37,24,37s12.769-2.543,16.009-4.993c-2.616,3.006-5.627,4.719-8.332,5.706	c-0.157,0.057-0.211,0.245-0.111,0.379l1.282,1.709c0.101,0.134,0.26,0.208,0.427,0.199c1.407-0.072,7.996-0.679,12.588-5.823	c0.095-0.106,0.144-0.253,0.135-0.395C45.156,20.538,40.815,13.257,40.107,12.15z"/><ellipse cx="30.5" cy="26" opacity=".05" rx="4.5" ry="5"/><ellipse cx="30.5" cy="26" opacity=".05" rx="4" ry="4.5"/><ellipse cx="30.5" cy="26" fill="#fff" rx="3.5" ry="4"/><ellipse cx="17.5" cy="26" opacity=".05" rx="4.5" ry="5"/><ellipse cx="17.5" cy="26" opacity=".05" rx="4" ry="4.5"/><ellipse cx="17.5" cy="26" fill="#fff" rx="3.5" ry="4"/></svg> Discord Server for tech support ](https://discord.gg/k7yNftGEAA)**

## Why does this work?

This script works because Canvas uses a sequential numbering system for file IDs. This is known as an **auto-incrementing primary key**. When a file is uploaded to Canvas, it is assigned a unique ID that is one greater than the previous file's ID. This means that the IDs are sequential and predictable. So if you know the ID of one file, you can easily find the IDs of other files by simply incrementing or decrementing the known ID.
As an example, consider this:

```
https://canvas.example.edu/courses/123/files/455000 // Homework 10 Solutions
https://canvas.example.edu/courses/123/files/455001 // Midterm Exam
https://canvas.example.edu/courses/123/files/455002 // Final Exam Solutions


https://canvas.example.edu/courses/123/files/456000 // Syllabus
```

If you have the location of the syllabus (`456000`), you can easily find the location of the other files by simply decrementing the file ID. This is what this script does. It starts at a given file ID and checks as many files as you want (specified by the `--num-files` flag) by decrementing the file ID.

Our goal is to find the old files when a professor re-initializes a course. If a professor re-initializes a course, the old file IDs will appear concentrated and in close proximity due to the sequential, auto-incrementing nature of the file IDs in the database.

![Sequential IDs](assets/sequential-ids.png)

## Prerequisites

- Install Python 3 ([Awesome Tutorial](https://realpython.com/installing-python/))
- Open a terminal (On macOS, press `Command + Space` and type `Terminal`. On Windows, press `Windows + R` and type `cmd`)
- Clone this repo and navigate to the directory where you cloned it. You can do this by running the following commands in your terminal:

```bash
git clone https://github.com/erict963/canvas-tool.git
cd canvas-tool
```

This script was built with only the standard library, so no additional packages are required! You should be able to run it without any additional installations.

## Usage

### Example

The following example command will start at `https://canvas.example.edu/courses/123/files/456000`
and search all the URLs from `456000` to `(456000 - 10000 = 446000)`.

Example command to paste into your terminal:

```
python3 canvas.py --canvas-session Ggx-OQY... \
 --url https://canvas.example.edu/courses/123/files/456000 \
 --num-files 10000 \
 --use-api
```

The `--use-api` flag is optional. It will use the Canvas API to get file names instead of the default method, which is to scrape the frontend page. The API method is faster, but it may not work for all files. See the Canvas API section on why this is the case.

So to be perfectly clear, the above command will check these URLs:

```
https://canvas.example.edu/api/v1/courses/123/files/456000
https://canvas.example.edu/api/v1/courses/123/files/455999
https://canvas.example.edu/api/v1/courses/123/files/455998
...
https://canvas.example.edu/api/v1/courses/123/files/446000
```

If you do not pass in the `--use-api` flag, it will resort to checking the frontend URLs instead. The URLs will look like this:

```
https://canvas.example.edu/courses/123/files/456000
https://canvas.example.edu/courses/123/files/455999
https://canvas.example.edu/courses/123/files/455998
...
https://canvas.example.edu/courses/123/files/446000
```

**Important:** The script assumes that the URL matches this ending pattern: `/files/{file_id}` where `{file_id}` is an integer.

### Full Command Line Options

To see all the command line options, you can run the following command:

```
python3 canvas.py -h
```

This will show you all the available options and their descriptions. Here is a summary of the options:

```
usage: canvas.py [-h] -u URL [-f NUM_FILES] [-s CANVAS_SESSION] [-w NUM_WORKERS]
                 [-l LOG_EVERY] [--use-api]

Canvas file sweeper

options:
  -h, --help            show this help message and exit
  -u, --url URL         The URL of the file to start from, e.g.
                        https://canvas.example.edu/courses/123/files/456
  -f, --num-files NUM_FILES
                        Number of files to scan (default 10000, min 1)
  -s, --canvas-session CANVAS_SESSION
                        The Canvas API canvas_session, provided as an environment
                        variable or command line argument. If not provided, the
                        script will use the CANVAS_SESSION environment variable.
  -w, --num-workers NUM_WORKERS
                        Number of threads to use (default 16, max 32)
  -l, --log-every LOG_EVERY
                        Log every (X) files found (default 1000, min 1)
  --use-api             Experimental: Use the Canvas API instead of the frontend
                        (default: False) - this will be faster but may not
                        necessarily find all files. See README for more details.
```

## Canvas session

The `canvas_session` is what allows this Python script to check for your Canvas files. It's like a password (hence why you **shouldn't share it with anyone**). Whenever you log into Canvas, this `canvas_session` is created and stored securely in your browser. Applications use tokens to authenticate users and authorize access to resources.

In short, it gives the script permissions to act on your behalf. Don't worry, all this script is doing is checking if your professor's files are available or not. See the code in `canvas.py` for more details, and feel free to ask ChatGPT if you think any lines are suspicious.

### Obtaining

To obtain a `canvas_session`, first make sure you're logged into your school's Canvas. Then, visit any page in Canvas. For example, go to

```
https://canvas.example.edu/courses/123/files/456
```

Then right-click on the page and select "Inspect". This will open the developer tools. In the developer tools, select the "Application" tab.

![Application Tab](assets/application-tab.png)

On the left side, you should see a list of items. Click on "Cookies" and then select your school's Canvas domain. You should see a list of cookies. Look for a cookie called `canvas_session`. Copy the value of this cookie.

![Obtaining Token](assets/obtaining-token.png)

### Using an environment variable

If you prefer to not repeatedly have to enter the `canvas_session` with the `--canvas-session` flag, you can certainly export it as an environment variable. This is done by running the following command in your terminal:

```bash
export CANVAS_SESSION=Ggx-OQY...
```

Now, you can run the script without the `--canvas-session` flag. The script will automatically use the `canvas_session` from the environment variable each time you run it.

```bash
python3 canvas.py --url https://canvas.example.edu/courses/123/files/456000 --num-files 10000 --use-api
```

## Canvas API

### Why use the API?

Great question! You're asking what's the difference between visiting this URL:

`https://canvas.example.edu/api/v1/courses/123/files/456000` versus this URL `https://canvas.example.edu/courses/123/files/45600`

Let's take a look at the api URL first. If you enter this `https://canvas.example.edu/api/v1/courses/123/files/456000` into your browser (just an example, but do try it with your courses!), you should see something like this (truncated for brevity):

```json
{
  "id": 123,
  "uuid": "tRuCMqv9QumS9OqBhXe2gPs0SdtUl4RHFcY5hdmo",
   ...
}
```

Now, let's take a look at the frontend URL. Simply delete the `api/v1/` part of the URL and enter it into your browser.
So the URL would look like this: `https://canvas.example.edu/courses/123/files/456000`, and the response would be something like this (truncated for brevity):

```html
<!DOCTYPE html>
<html dir="ltr" lang="en">
  <head>
    ...
  </head>
</html>
```

The main difference is the **size** of the responses. A typical example would be something like this: The API response is `300B` while the frontend response is `13kB`. This means the server will take longer to send the frontend response.

### Why does the API "miss" some files (not necessarily a bad thing) ?

I observed this "missing" behavior empirically, so this explanation is slightly speculative. Please let me know if you have a better explanation.

If you go to the [actual code of how Canvas is implemented](https://github.com/instructure/canvas-lms/blob/ddaaa0089cb3e83783056404d44106527dfe5ef1/app/models/attachment.rb#L1756)

You may see something like this:

```ruby
def destroy_content_and_replace(deleted_by_user = nil)
```

This means that when a professor re-initializes a course, the old files may start like this:

```
https://canvas.example.edu/courses/123/files/1 // Homework 10 Solutions
https://canvas.example.edu/courses/123/files/2 // Midterm Exam
https://canvas.example.edu/courses/123/files/3 // Final Exam Solutions
```

However, now let's say the professor makes a correction to Homework 10 Solutions before making them available to everyone. Because the content is destroyed but replaced with a new ID, and the fact that the IDs are sequential, the new file ID may look like this:

```
https://canvas.example.edu/courses/123/files/4 // Updated Homework 10 Solutions
```

So the API will no longer detect that the old file ID lives at `1`, but rather at `4`.

However, the frontend will still show the old file ID `1` as a valid file, and redirect to the new file ID `4` via the API.

This is why using this script to search via API may "miss" some files - the frontend relies on the API to report the correct data. Note, the frontend search will always "hit" every ID that exists.

This is not necessarily a bad thing, because our entire goal is to get the "old files" that aren't currently available to the public.
