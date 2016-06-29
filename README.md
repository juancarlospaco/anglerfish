
# anglerfish

![anglerfish](https://raw.githubusercontent.com/juancarlospaco/anglerfish/master/temp.jpg "Ugly but Enlightening")


[![GPL License](http://img.shields.io/badge/license-GPL-blue.svg?style=plastic)](http://opensource.org/licenses/GPL-3.0) [![LGPL License](http://img.shields.io/badge/license-LGPL-blue.svg?style=plastic)](http://opensource.org/licenses/LGPL-3.0) [![Python Version](https://img.shields.io/badge/Python-3-brightgreen.svg?style=plastic)](http://python.org)

[![Donate BitCoins](https://www.coinbase.com/assets/buttons/donation_large-5cf4f17cc2d2ae2f45b6b021ee498297409c94dcf0ba1bbf76fd5668e80b0d02.png)](https://www.coinbase.com/checkouts/c3538d335faee0c30c81672ea0223877 "Donate Bitcoins") [![Subscribe with BitCoins](https://www.coinbase.com/assets/buttons/subscription_large-11d991f628216af05156fae88a48ce25c0cb36447a265421a43a62e572af3853.png)](https://www.coinbase.com/checkouts/c3538d335faee0c30c81672ea0223877 "Subscribe with BitCoins") [![Pay with BitCoins](https://www.coinbase.com/assets/buttons/buy_now_large-6f15fa5979d25404827a7329e8a5ec332a42cf4fd73e27a2c3ccda017034e1b0.png)](https://www.coinbase.com/checkouts/c3538d335faee0c30c81672ea0223877 "Pay with BitCoins") [![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif "Donate with or without Credit Card")](http://goo.gl/cB7PR)


# Description of functions

---

<details>
<summary>
# make_logger
</summary>
`anglerfish.make_logger(name: str, when: str='midnight', single_zip: bool=False)`

**Description:** Returns a Logger, that has Colored output, logs to STDOUT, logs to Rotating File,
it will try to Log to Unix SysLog Server if any, log file is based on App name,
if the App ends correctly it will automatically ZIP compress the old unused rotated logs,
this should be the first one to use, since others may need a way to log out important info, you should always have a logger.
Please use a unique and distinctive name for your app, and use the same name every time Anglerfish needs an app name.

**Arguments:** 
- `name` is a unique name of your App, string type.
- `when` is one of 'midnight', 'S', 'M', 'H', 'D', 'W0'-'W6', optional will use 'midnight' if not provided, string type.
- `single_zip` Unused Old Rotated Logs will be ZIP Compressed automagically, `True` equals 1 ZIP per Log, `False` equals 1 ZIP for *All* Logs, lets the user choose if you want a single ZIP or one per log file.

**Keyword Arguments:** None.

**Returns:** logging.logger object.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/__init__.py

**Usage Example:**

```python
from anglerfish import make_logger
log = make_logger("MyAppName")
log.debug("This is a Test.")
log.info("This is a Test.")
log.warning("This is a Test.")
log.critical("This is a Test.")
log.exception("This is a Test.")
```
</details>


<details>
<summary>
# get_free_port
</summary>
`anglerfish.get_free_port(port_range: tuple=(8000, 9000))`

**Description:** Returns a free unused port number integer.
Takes a tuple of 2 integers as argument, being the range of port numbers to scan.

**Arguments:**
- `port_range` is the range of port numbers to scan, starting port and ending port numbers. 2 items only are allowed. Tuple type.

**Keyword Arguments:** None.

**Returns:** Integer, a free unused port number.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_free_port.py

**Usage Example:**

```python
from anglerfish import get_free_port
get_free_port()
```
</details>


<details>
<summary>
# make_notification
</summary>
`anglerfish.make_notification(title: str, message: str="", name: str="", icon: str="", timeout: int=3000))`

**Description:** Makes a Passive Notification Bubble (Passive Popup), it works cross-desktop, using one of DBus, PyNotify, notify-send, kdialog, zenity or xmessage.
Should degrade nicely on operating systems that dont have any of those.
Best results are with D-Bus.

**Arguments:**
- `title` is the short title of your message, mandatory, string type.
- `message` is body of your message, defaults to empty string, optional, string type.
- `name` is the name of your App, defaults to empty string, optional, string type.
- `icon` is the icon name of your App, defaults to empty string, optional, string type.
- `timeout` is the timeout for your notification bubble, defaults to `3000`, optional, integer type.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_notification.py

**Usage Example:**

```python
from anglerfish import make_notification
make_notification("test")
```
</details>


<details>
<summary>
# bytes2human
</summary>
`anglerfish.bytes2human(bites: int, to: str, bsize: int=1024)`

**Description:** Returns a Human Friendly string containing the argument integer bytes expressed as KiloBytes, MegaBytes, GigaBytes (...), 
uses a Byte Size of `1024` by default. Its basically a Bytes to KiloBytes, MegaBytes, GigaBytes (...).

**Arguments:**
- `bites` is the number of bytes, integer type.
- `to` is one of 'k', 'm', 'g', 't', 'p', 'e', being KiloBytes, MegaBytes, GigaBytes (...), string type.
- `bsize` is the Byte Size, defaults to `1024`, since tipically is the desired byte size, integer type.

**Keyword Arguments:** None.

**Returns:** string, human friendly representation.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/bytes2human.py

**Usage Example:**

```python
from anglerfish import bytes2human
bytes2human(3284902384, "g")
```
</details>


<details>
<summary>
# check_encoding
</summary>
`anglerfish.check_encoding()`

**Description:** Checks the all the Encodings of the System and Logs the results, to name a few like `STDIN`, `STDERR`, `STDOUT`, FileSystem, `PYTHONIOENCODING` and Default Encoding, takes no arguments, requires a working Logger, all "UTF-8" should be ideal on Linux/Mac.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Bool, `True` if everything is Ok.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/check_encoding.py

**Usage Example:**

```python
from anglerfish import check_encoding
check_encoding()
```
</details>


<details>
<summary>
# check_folder
</summary>
`anglerfish.check_folder(folder_to_check: str)`

**Description:** Checks a working folder from `folder_to_check` argument for everything that can go wrong,
like no Read Permissions, that the folder does not exists, and no space left on it, etc etc. Returns Boolean.

**Arguments:** `folder_to_check` path of the folder to check, string type.

**Keyword Arguments:** None.

**Returns:** Bool, True if everything is Ok.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/check_folder.py

**Usage Example:**

```python
from anglerfish import check_folder
check_folder("/path/to/my/folder/")
```
</details>


<details>
<summary>
# get_clipboard
</summary>
`anglerfish.get_clipboard()`

**Description:** Cross-platform cross-desktop Clipboard functionality, takes no arguments.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Tuple, `clipboard_copy()` and `clipboard_paste()`.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_clipboard.py

**Usage Example:**

```python
from anglerfish import get_clipboard
clipboard_copy, clipboard_paste = get_clipboard()
clipboard_copy("This is a Test.")
print(clipboard_paste())
```
</details>


<details>
<summary>
# get_sanitized_string
</summary>
`anglerfish.get_sanitized_string(stringy: str, repla: str="")`

**Description:** Take string argument and sanitize non-printable weird characters and return a clean string, 
ready to use on ASCII-only if required, optionally you can pass a replacement string to be used.

**Arguments:** 
- `stringy` string to be clean out of weird characters, string type. 
- `repla` a replacement string to be used instead of empty string `""`, can be a single character.

**Keyword Arguments:** None.

**Returns:** string, the same as input but ASCII-only ready.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_sanitized_string.py

**Usage Example:**

```python
from anglerfish import get_sanitized_string
get_sanitized_string("╭∩╮_(҂≖̀‿≖́)_╭∩╮")
```
</details>


<details>
<summary>
# get_temp_folder
</summary>
`anglerfish.get_temp_folder(appname: str)`

**Description:** Creates and returns a folder on the systems Temporary directory, 
creating it or not if needed, the folder will have the same name as the App passed as argument,
it means to be a liittle more safe than just writing everything to the systems temp folder where simple name collisions can overwrite and loss data.

**Arguments:** `appname` the name of your app.

**Keyword Arguments:** None.

**Returns:** string, full path to the apps temp folder.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_temp_folder.py

**Usage Example:**

```python
from anglerfish import get_temp_folder
get_temp_folder("test")
```
</details>


<details>
<summary>
# beep
</summary>
`anglerfish.beep(waveform: tuple)`

**Description:** A "Beep" sound, a Cross-platform sound playing with Standard Lib only, No Sound file is required,
like old days Pc Speaker Buzzer Beep sound, meant for very long running operations and/or headless command line apps,
it works on Linux, Windows and Mac and requires nothing to run.

**Arguments:** `waveform` tuple containing integers, as the sinewave for the beep sound, defaults to `(79, 45, 32, 50, 99, 113, 126, 127)`.

**Keyword Arguments:** None.

**Returns:** Bool, True is sound playing went Ok.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_beep.py

**Usage Example:**

```python
from anglerfish import beep
beep()
```
</details>


<details>
<summary>
# json_pretty
</summary>
`anglerfish.json_pretty(json_dict: dict)`

**Description:** Pretty-Printing JSON data from dictionary to string, very human friendly representation, 
similar to YML but still valid JSON, works perfectly with JavaScript too.

**Arguments:** `json_dict` a dict with data that will be converted to JSON and pretty-printed as string.

**Keyword Arguments:** None.

**Returns:** string, the JSON data.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_json_pretty.py

**Usage Example:**

```python
from anglerfish import json_pretty
json_pretty({"foo": True, "bar": 42, "baz": []})
```
</details>


<details>
<summary>
# log_exception
</summary>
`anglerfish.log_exception()`

**Description:** Log Exceptions but pretty printing with a lot more information of whats going on under the hood, 
returns a string printing it via a working logger at the same time, 
works for Exceptions like on `try...except...finally` constructions, takes no arguments.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** string, the info about the exception.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_log_exception.py

**Usage Example:**

```python
from anglerfish import log_exception
try:
    0 / 0
except Exception:
    log_exception()
```
</details>


<details>
<summary>
# ipdb_on_exception
</summary>
`anglerfish.ipdb_on_exception(debugger: str="ipdb")`

**Description:** Automatic iPDB Debugger when an Exception happens, 
it install a handler to attach a post-mortem ipdb console on an exception on the fly at runtime,
PDB, iPDB can be used as Debugger console.

**Arguments:** 
- `debugger` one of `"ipdb"`, `"pdb"`.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_pdb_on_exception.py

**Usage Example:**

```python
from anglerfish import ipdb_on_exception
ipdb_on_exception()
try:
    0 / 0
except Exception:
    pass
```
</details>


<details>
<summary>
# seconds2human
</summary>
`anglerfish.seconds2human(time_on_seconds: int)`

**Description:** From Time on seconds to very human friendly string representation,
calculates time with precision from seconds to days, returns the string with representation.

**Arguments:** `time_on_seconds` time on seconds, integer type.

**Keyword Arguments:** None.

**Returns:** string, human friendly representation.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/seconds2human.py

**Usage Example:**

```python
from anglerfish import seconds2human
seconds2human(490890)
```
</details>


<details>
<summary>
# set_process_name
</summary>
`anglerfish.set_process_name(name: str)`

**Description:** Set the current process name to the argument `name`, 
so instead of all your apps listing as `python` on the system monitor they will have proper names,
this helps debug, troubleshooting and system administration in general.

**Arguments:** `name` the name of your app.

**Keyword Arguments:** None.

**Returns:** Boolean, True if it can change the process name.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_process_name.py

**Usage Example:**

```python
from anglerfish import set_process_name
set_process_name("MyApp")
```
</details>


<details>
<summary>
# walk2list
</summary>
`anglerfish.walk2list(where: str, target: str, omit: str, links: Bool=False, tuply: Bool=True)`

**Description:** Perform full recursive walk of `where` folder path, 
search for `target` like files, ignoring `omit` like files, follow symbolic links if `links` is `True`,
convert the output to `tuple` if `tuply` is `True`, else return the `list` containing the path of all the files.

**Arguments:** 
- `where` path to a folder to scan, string type.
- `target` type of files to search for, for example `.py`, string type, 
- `omit` type of files to ignote, for example `.pyc`, string type, 
- `links` a Boolean, `True` to follow simbolic links, 
- `tuply` a Boolean, `True` to convert the output `list` into a `tuple`.

**Keyword Arguments:** None.

**Returns:** `list` or `tuple`

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/walk2list.py

**Usage Example:**

```python
from anglerfish import walk2list
walk2list(".")
```
</details>


<details>
<summary>
# walk2dict
</summary>
`anglerfish.walk2dict(folder: str, links: Bool=False, showhidden: Bool=False, strip: Bool=False, jsony: Bool=False)`

**Description:** Return Nested Dictionary that represents the folders and files structure of the folder,


**Arguments:** 
- `folder` path to folder to scan, string type, 
- `links` a Boolean, `True` to follow simbolic links,
- `showhidden` a Boolean, `True` to show hidden files and folders,
- `strip` a Boolean, `True` to strip the relative folder path, 
- `jsony` a Boolean, `True` to convert the `dict` to JSON.

**Keyword Arguments:** None.

**Returns:** `dict` or `str` with JSON.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/walk2dict.py

**Usage Example:**

```python
from anglerfish import walk2dict
walk2dict(".")
```
</details>


<details>
<summary>
# multiprocessed
</summary>
`anglerfish.multiprocessed(function: Callable, arguments: object, cpu_num: int=1, thread_num: int=1, timeout: int=None)`

**Description:** Execute code on multiple CPU Cores and multiple Threads per CPU Core,
with optional Timeout, on a quick and easy way.

**Arguments:** 
- `function` a function of Callable type to execute code, 
- `arguments` is an object that represent the arguments for the function, 
- `cpu_num` how many CPU Cores to use, integer type, 
- `thread_num` how many Threads per CPU Core to use, integer type, 
- `timeout` a Timeout on Seconds, integer type or None.

**Keyword Arguments:** None.

**Returns:** concurrent.futures object.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_multiprocess.py

**Usage Example:**

```python
from anglerfish import multiprocessed
import time

def process_job(job):  # a simple function for testing only
    time.sleep(1)
    count = 100
    while count > 0:
        count -= 1
    return job
jobs = [str(i) for i in range(30)]  # a simple list

print(multiprocessed(process_job, jobs, cpu_num=1, thread_num=4))
print(multiprocessed(process_job, jobs, cpu_num=4, thread_num=1))
```
</details>


<details>
<summary>
# threads
</summary>
`@threads(n: int, timeout=None)`

**Description:** Execute code on multiple Threads, with optional Timeout, on a quick and easy way.

**Arguments:** 
- `n` number of Threads to use for the function execution, integer type, 
- `timeout` a Timeout on seconds or None.

**Keyword Arguments:** None.

**Returns:** Its a Decorator.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_multithread.py

**Usage Example:**

```python
from anglerfish import threads
import time
@threads(4)
def process_job():  # a simple function for testing only
    return time.sleep(1)
process_job()
```
</details>


<details>
<summary>
# retry
</summary>
`@retry(tries: int=5, delay: int=3, backoff: int=2,
          timeout: int=None, silent: Bool=False, logger=None)`

**Description:** Retry calling the decorated function using an exponential backoff and timeout.

**Arguments:** 
- `tries` how many times retry the operation, defaults to 5, integer type.
- `delay` delay between executions, defaults to 3, integer type.
- `backoff` an exponential backoff offset to apply to the `delay`, defaults to 2, integer type.
- `timeout` a timeout for the whole execution or None, defaults to None.
- `silent` a boolean `True` to be Silent when running the reties, defaults to False.
- `logger` a working logger to log into or None to use `print()`.

**Keyword Arguments:** None.

**Returns:** Its a Decorator.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_retry.py

**Usage Example:**

```python
from anglerfish import retry
@retry(4)
def retry_job():  # a simple function for testing only
    return open("").read()  # Will Fail as expected
retry_job()
```
</details>


<details>
<summary>
# set_single_instance
</summary>
`anglerfish.set_single_instance(name: str, port: int=8888)`

**Description:** Set a single instance Lock based on Sockets and return socket.socket object or None.

**Arguments:** 
- `name` the name of your app to be used as Lock name, 
- `port` port number to be used when Unix Socket is not available, mostly on MS Windows, defaults to 8888, integer type.

**Keyword Arguments:** None.

**Returns:** socket.socket object or None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_single_instance.py

**Usage Example:**

```python
from anglerfish import set_single_instance
set_single_instance("MyApp")
```
</details>


<details>
<summary>
# env2globals
</summary>
`anglerfish.env2globals(pattern: str)`

**Description:** Auto add ENV environtment variables starting with `PY_` in upper case to python globals dict.

**Arguments:** `pattern` the pattern to select which variables to add, default to `PY_`

**Keyword Arguments:** None.

**Returns:** Boolean, True if everything is Ok.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/env2globals.py

**Usage Example:**

```python
from anglerfish import env2globals
env2globals()
```
</details>


<details>
<summary>
# html2ebook
</summary>
`anglerfish.html2ebook(files: list, fyle: str=uuid4().hex + ".epub", meta={})`

**Description:** Convert a folder with HTML5/CSS3 to eBook ePub. JavaScript does not Work on ePub.

**Arguments:**
- `files` a tuple with the list of HTML/CSS files to add to the eBook.
- `fyle` an output file path string, defaults to an uuid4 hexadecimal if not provided.

**Keyword Arguments:** `meta` contains a dict with:
- `title` is the eBook Title (Fallbacks to Filename if not provided).
- `author`  is the eBook Author (Fallbacks to Username if not provided).
- `lang` is the eBook Language (Fallbacks to English if not provided).
- `des` is a friendly eBook Description (Fallbacks to Filename if not provided).
- `copi` eBook CopyRights (Fallbacks to Creative Commons 'CC-BY-NC-SA v.4.0' if not provided).
- `pub` the eBook Publisher (Fallbacks to 'Python' if not provided).
- `date` Date and Time ISO format of eBook creation (Fallbacks to Current Date and Time if not provided).

**Returns:** a string with the file path of the new eBook file.

**Usage Example:**

```python
from anglerfish import html2ebook
html2ebook(("/mybook/html/index.html", "/mybook/html/chapter1.html"))
```
</details>


<details>
<summary>
# TemplatePython
</summary>
`anglerfish.TemplatePython(template: str)`

**Description:** TemplatePython is a tiny generic Template Engine that Render and Runs native Python code. Template syntax is similar to Django Templates and Mustache. Fastest way to run Python on HTML and Render the results. No Markup enforced, it can work with HTML/CSS/JS or any kind of Markup. Has built-in optional Minification for HTML.

**Arguments:**
- `template` a template string with native Python 3 code between tags, or a file-like object that supports `.read()`.

**Keyword Arguments:** None.

**Returns:** a string with the Rendered HTML.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_template_python.py

**Usage Example:**

```python
from anglerfish import TemplatePython
demo = """<html><body>
     {%
     def say_hello(arg):
         {{"<tr> hello ", arg, " </tr>"}}
     %}
     <table>
         {% [say_hello(i) for i in range(9) if i % 2] %}
     </table>
     {% {{ testo }} {{ __doc__.title() }} %}
     {% # this is a python comment %}  </body></html>"""
templar_template = TemplatePython(demo)
print(templar_template(testo=9, mini=True))
```
</details>

<details>
<summary>
# path2import
</summary>
`anglerfish.path2import(pat: str, name: str=None)`

**Description:** Imports a Python module from a file path string.
This is *as best as it can be* way to load a module from a file path string that
I can find from the official Python Docs, for Python 3.5+ or higher.
This has been created after having `ImportError` trying to use a 1 line module,
that only contains `__version__ = "1.0.0"`,
not meant to replace the standard way of importing modules.

**Arguments:**
- `pat` is the file path on disk from where to load a Python module from, mandatory. String type.
- `name` is the Python module name, optional,
will try to get it from the filename on the `pat` argument if omitted. String type.

**Keyword Arguments:** None.

**Returns:** object, a *"live"* Python module object ready for use at runtime.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/path2import.py

**Usage Example:**

```python
from anglerfish import path2import
my_module = path2import("/path/to/module.py")
```
</details>


<details>
<summary>
# make_post_exec_msg
</summary>
`anglerfish.make_post_exec_msg(start_time: object=None, comment: str=None)`

**Description:** Simple Post-Execution Message with information about RAM used by your app and execution Time. Can also display an arbitrary string ideal for Donation links, Social, etc.
It will register itself to be executed at exit via `atexit.register()`.
Its basically a *Goodbye* message.

**Arguments:**
- `start_time` a `datetime` object, ideally should be `datetime.now()`.
- `comment` an arbitrary string ideal for Donation links, Social links, Bitcoin, etc. String type.

**Keyword Arguments:** None.

**Returns:** The formatted message, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_postexec_message.py

**Usage Example:**

```python
from anglerfish import make_post_exec_msg
make_post_exec_msg()
```
</details>


<details>
<summary>
# watch
</summary>
`anglerfish.watch(file_path: str, callback: Callable=None, interval: int=60)`

**Description:** Watch a file path for changes run callback if modified. 
A WatchDog.

**Arguments:**
- `file_path` an existent readable file path to watch for changes. String type.
- `callback` a `Callable` callback function to execute when changes are detected. Callable type.
- `interval` an integer number seconds of interval between chacks for changes. Integer type.

**Keyword Arguments:** None.

**Returns:** `Callable` output if theres a callable, else the file path that changed.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_watch.py

**Usage Example:**

```python
from anglerfish import watch
watch("/tmp/file.txt")
```
</details>


<details>
<summary>
# set_desktop_launcher
</summary>
`anglerfish.set_desktop_launcher(app: str, desktop_file_content: str, autostart: bool=False)`

**Description:** Adds your app to autostart and/or launcher icon on the Desktop.
According to XDG standard. Runs on Linux. Other platforms simply does nothing.

**Arguments:**
- `app` the name of your app. String type.
- `desktop_file_content` the content of the launcher file. String type.
- `autostart` a Boolean True or False to choose if your app will be added to auto-start on the desktop.

**Keyword Arguments:** None.

**Returns:** the path of the newly created launcher. string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_desktop_launcher.py

**Usage Example:**

```python
from anglerfish import set_desktop_launcher
set_desktop_launcher("mysuperapp", "")
```
</details>


<details>
<summary>
# set_terminal_title
</summary>
`anglerfish.set_terminal_title(titlez: str="")`

**Description:** Set or Reset Bash CLI Window Titlebar Title.
According to XDG standard. Runs on Linux. Other platforms simply does nothing.

**Arguments:**
- `titlez` the title for the terminal emulator window. Optional. String type.

**Keyword Arguments:** None.

**Returns:** `titlez` if the title has been set on the terminal emulator window or None. string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_terminal_title.py

**Usage Example:**

```python
from anglerfish import set_terminal_title
set_terminal_title("mysuperapp")
```
</details>


<details>
<summary>
# json2xml
</summary>
`anglerfish.json2xml(json_obj: dict, line_padding: str="")`

**Description:** Takes a JSON and returns an XML, optional custom line paddings.

**Arguments:** 
- `json_obj` the json data, dict type.
- `line_padding` optional custom line paddings, string type.

**Keyword Arguments:** None.

**Returns:** XML, string type.

**Source Code file:** 

**Usage Example:**

```python
from anglerfish import json2xml
json2xml({"foo": 42, "bar": 666})
```
</details>


<details>
<summary>
# make_json_flat
</summary>
`anglerfish.make_json_flat(jsony: dict, delimiter: str="__")`

**Description:** Takes a JSON and returns a JSON, but with Flatten out structure, from Nested to Flat, optional custom delimiter.

**Arguments:** 
- `jsony` the json data, dict type.
- `delimiter` optional custom delimiter, string type.

**Keyword Arguments:** None.

**Returns:** JSON, a Flat JSON, dict type.

</details>


---


# Install permanently on the system:

**PIP:** *(Recommended!)*
```
pip3 install anglerfish
```
- Use `sudo pip3 install anglerfish` for installing System-wide.
- Use `python3 examples/basic.py` to run an example of all the functionalities.
- This project is oriented to Developers, NOT end-users.
- Feel free to contact us if you need help integrating Anglerfish on your project.


# Why?:

- Too much repeated code across my projects, almost all of them doing tha same.
- Look into other alternatives like Boltons but they dont solve or improve anything.
- Other libs try to fix Python2 problems, that has been improved on Python3.
- Anglerfish modules are less than 100 lines while other solutions are over-engineered and bloated.
- Lots of functionalities on Anglerfish are a *"Must Have"* for modern Apps, like a Logger, etc.
- 1 Module = 1 file = 1 feature, less than 100 lines per file, do 1 thing do it well.
- No Dependencies at all, just Python 3 standard library, cross-platform.
- Easy to use, KISS philosophy.


# Requisites:

- [Python 3.x](https://www.python.org "Python Homepage") *(or PyPy 3.x)*


# Coding Style Guide:

- Lint, [PEP-8](https://www.python.org/dev/peps/pep-0008), [PEP-257](https://www.python.org/dev/peps/pep-0257), [PyLama](https://github.com/klen/pylama#-pylama), [iSort](https://github.com/timothycrosley/isort) must Pass Ok. `pip install pep8 pep257 pylama isort`
- If there are any kind of tests, they must pass. No tests is also acceptable, but having tests is better.


# Name convention

- For names we use: `get_*`, `set_*`, `check_*`, `make_*` and `*2*`.


# Contributors:

- **Please Star this Repo on Github !**, it helps to show up faster on searchs.
- **Ad-Hocracy Meritocracy**: 3 Pull Requests Merged on Master you become Repo Admin. *Join us!*
- [Help](https://help.github.com/articles/using-pull-requests) and more [Help](https://help.github.com/articles/fork-a-repo) and Interactive Quick [Git Tutorial](https://try.github.io).


# Licence:

- GNU GPL Latest Version *AND* GNU LGPL Latest Version *AND* any Licence [YOU Request via Bug Report](https://github.com/juancarlospaco/css-html-js-minify/issues/new).


# Ethics and Humanism Policy:
- May this FLOSS be always Pristine and Clean, No AdWare, No Spamm, No BundleWare, No Infomercial, No MalWare.
- This project is [LGBTQQIAAP friendly](http://www.urbandictionary.com/define.php?term=LGBTQQIAAP "Whats LGBTQQIAAP").
