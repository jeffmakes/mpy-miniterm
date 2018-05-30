# mpy-miniterm v0.1
==============

Serial terminal and code download tool for Micropython

mpy-miniterm allows seamless transitions between serial debugging and file download via the MicroPython REPL

mpy-miniterm is based on  pySerial miniterm. There is an additional menu option for synchronising a source folder on the host to the MicroPython device's filesystem over the serial REPL. Activate this function by pressint Ctrl+t Ctrl+g. The source folder is specified with the--sync-dir CLI option.

## Requirements

* mpy-utils, available from PyPI and https://github.com/nickzoic/mpy-utils/
