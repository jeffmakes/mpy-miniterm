# mpy-miniterm v0.1

Tool for seamless serial debug and file synchronisation with MicroPython devices via the serial REPL.

mpy-miniterm allows seamless transitions between serial debugging and file download via the MicroPython REPL

mpy-miniterm is based on  pySerial miniterm. There is an additional menu option for synchronising a source folder on the host to the MicroPython device's filesystem over the serial REPL. Activate this function by pressint Ctrl+t Ctrl+g. The source folder is specified with the--sync-dir CLI option.

mpy-miniterm makes use of a slightly modified version of the ReplControl class from Nick Moore (part of https://github.com/nickzoic/mpy-utils)
