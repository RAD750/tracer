#!/usr/bin/env python

# Modified by Jacopo Cassinis - Modified output to standard JSON format so it can be easily parsed from other software.

import serial
from tracer import Tracer, TracerSerial, QueryCommand

fake = None
# A sample response, to show what this demo does. Uncomment to use.
# fake = bytearray(b'\xEB\x90\xEB\x90\xEB\x90\x00\xA0\x18\xD2\x04\xD3\x04\x00\x00\x0E\x00\x53\x04\xA5\x05\x01\x00\x00\x1F\x00\x00\x00\x01\x33\x0A\x00\x00\x99$

class FakePort(object):
    def __init__(self, data):
        self.data = data
    read_idx = 0
    def read(self, count=1):
        result = self.data[self.read_idx:self.read_idx+count]
        self.read_idx += count
        return result
    def write(self, data):
        return len(data)

if not fake:
    ser = serial.Serial('/dev/ttyS0', 9600, timeout = 1)
else:
    ser = FakePort(fake)

tracer = Tracer(0x16)
t_ser = TracerSerial(tracer, ser)
query = QueryCommand()
t_ser.send_command(query)
result = t_ser.receive_result()

formatted = str(result).replace('{', '{\n"')
formatted = formatted.replace('}', '"\n}')
formatted = formatted.replace(': ', '":"')
formatted = formatted.replace('QueryResult', '')
print formatted.replace(', ', '","')
