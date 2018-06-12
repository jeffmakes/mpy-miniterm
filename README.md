# mpy-miniterm v0.1

Tool for seamless serial debug and file synchronisation with MicroPython devices via the serial REPL. 

mpy-miniterm allows seamless transitions between serial debugging and file download via the MicroPython REPL, and is intended to provide a smoother user experience than ampy, mpfshell and others. It is particularly useful for targets without USB mass storage functionality, like the ESP-32/8266 boards.

mpy-miniterm is based on  pySerial miniterm. There is an additional menu option for synchronising a source folder on the host to the MicroPython device's filesystem over the serial REPL. mpy-miniterm hashes the files to decide which ones to synchronise, so no time is wasted downloading unchanged files.

mpy-miniterm makes use of a slightly modified version of the ReplControl class from Nick Moore (part of https://github.com/nickzoic/mpy-utils)

## Usage
Specify your folder of source code with --sync-dir command line option. Then with mpy-miniterm running and connected to your board, press Ctrl+T Ctrl+G to syncronise the code onto the device.

If the --delete option is specified, files on your micropython board that aren't in your source folder will be automatically deleted from the device.

