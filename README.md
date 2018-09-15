# mpy-miniterm v0.1

Tool for seamless serial debug and file synchronisation with MicroPython devices via the serial REPL. 

mpy-miniterm allows seamless transitions between serial debugging and file download via the MicroPython REPL, and is intended to provide a smoother user experience than ampy, mpfshell and others. It is particularly useful for targets without USB mass storage functionality, like the ESP-32/8266 boards.

mpy-miniterm is based on  pySerial miniterm. There is an additional menu option for synchronising a source folder on the host to the MicroPython device's filesystem over the serial REPL. mpy-miniterm hashes the files to decide which ones to synchronise, so no time is wasted downloading unchanged files.

mpy-miniterm makes use of a slightly modified version of the ReplControl class from Nick Moore (part of https://github.com/nickzoic/mpy-utils)

## Usage
Specify your local folder of source code with the --sync-dir command line option. Then with mpy-miniterm running and connected to your board, press Ctrl+T Ctrl+G to syncronise the code onto the MicroPython target device. After the code is synchronised, the REPL will be active again, and you can reset and run your new code by pressing CTRL-D as usual.

If the --delete option is specified, files on your MicroPython board that aren't in your source folder will be automatically deleted from the device.

## Dependencies

* [https://pypi.org/project/pyserial/](pyserial)

## Example

# Set up virtualenv (optional)
```shell
$ virtualenv venv
New python executable in venv/bin/python
Installing setuptools, pip, wheel...done.
$ source venv/bin/activate
(venv) $
```

#### Install dependencies
```shell
(venv) $ pip install -r requirements.txt
Collecting pyserial (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/0d/e4/2a744dd9e3be04a0c0907414e2a01a7c88bb3915cbe3c8cc06e209f59c30/pyserial-3.4-py2.py3-none-any.whl
  Installing collected packages: pyserial
  Successfully installed pyserial-3.4
```


#### Set up a new hello world program
```shell
$ mkdir src
$ touch src/boot.py
$ echo 'print("Hello world!")' > src/main.py
$
```

#### Run mpy-miniterm with syncing, and deleting of files that are only on the MicroPython side.
```shell
(venv) $ python mpy-miniterm.py /dev/tty.SLAB_USBtoUART --sync-dir src/ --delete
--- Miniterm on /dev/tty.SLAB_USBtoUART  115200,8,N,1 ---
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---

>>>
>>>

<press ctrl-T, then ctrl-G to trigger syncing>

--- Synchronising MicroPython code ---
copying   'src/boot.py' => 'boot.py'
copying   'src/main.py' => 'main.py'

MicroPython v1.9.4-8-ga9a3caad0 on 2018-05-11; ESP module with ESP8266
Type "help()" for more information.
>>>

<press ctrl-D to restart MicroPython>

PYB: soft reboot
#7 ets_task(40100130, 3, 3fff83ec, 4)
Hello world!
MicroPython v1.9.4-8-ga9a3caad0 on 2018-05-11; ESP module with ESP8266
Type "help()" for more information.
>>>
```

#### Exiting mpy-miniterm
```shell
>>>

<press ctrl-]>

--- exit ---
(venv) $

