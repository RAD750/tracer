Communication Interface for Tracer MT-5
=======================================

This is an Arduino and Python library for interfacing with the SainSonic Tracer
series solar charge regulators.

I have tested both the Arduino and Python software extensively with a Raspberry Pi and an Arduino Nano on my EPSOLAR TRACER 1210RN.

The protocol is described in [Protocol Tracer MT-5][tracer-doc] (copy here in
`docs/`) and implemented in Python and Arduino. There's also a copy of the C
CRC as stated in the docs by itself with a test.

Physical Interface
------------------

The Tracer uses an [8P8C][] connector (the same physical type of connector as
RJ-45 Ethernet cables, but very much not an Ethernet connection).


**WARNING**: some solar charge controllers, while having an 8P8C connector, use a different pinout, protocol and interface (RS485). These programs won't work!

Pinout
------

Pin 1 is on the left when looking at the connector with the contacts facing
forward and the wire down. See [8P8C][] for an example of the physical
connector and location of pin 1.

1. +12V (seems to be regulated)
2. Gnd (common to both data and power)
3. +12V
4. Gnd
5. TXD (3.3V)
6. RXD (3.3V)
7. Gnd
8. Gnd

It communicates using TTL-232 at 9600 baud. TTL-232 in this context means +3.3V
is 1 and 0V is 0 (not to be confused with [RS-232][] which would be +3.3V is 0
and -3.3V is 1).



Warning about serial ports on the Raspberry Pi
-------

Usually, the default (hardware) serial port on the Raspberry Pi is called `/dev/ttyAMA0`. This is *not* the case on the Raspberry Pi Zero W (and possibly others), where `/dev/ttyAMA0` does exist, but is non-functional. 

If the script hangs, after checking the hardware part (connections, pinout etc.) you should modify the Python scripts to use `/dev/ttyS0` instead (this also applies if you are using an USB-to-UART adapter).

Also, make sure the serial console is disabled, but the serial port is enabled (use `raspi-config` to do so, and check with `dmesg |grep tty` the results).


License
-------

The Arduino and C code is mostly incomplete and as such is placed in the
[public domain][].

The Python library is a bit more complete and is licensed under the [LGPL v3][LGPL].

I have modified the example query so it can produce JSON output. This makes it very easy to interface it with other software.       

[8P8C]: https://en.wikipedia.org/wiki/Modular_connector#8P8C
[RS-232]: https://en.wikipedia.org/wiki/RS-232#Voltage_levels
[tracer-doc]: https://dl.dropboxusercontent.com/s/ftb7lxmp9030u7b/Protocoll-Trcaer-MT-5%EF%BC%88111213%EF%BC%89%281%29.pdf?dl=1&token_hash=AAHvuNfsGRew40X7TqT7XzKpcc6WzkL92hEiv7ej-xv0pA
[public domain]: http://creativecommons.org/publicdomain/zero/1.0/
[LGPL]: https://www.gnu.org/licenses/lgpl.html
