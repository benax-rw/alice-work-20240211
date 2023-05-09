#!/usr/bin/env python3
from os import system,popen
import urllib.parse
import json,urllib.request
import sys
import serial
from time import sleep


system("clear")
print("Benax::")
print("++++++++++++++++++++++")


if __name__ == "__main__":
    ser = serial.Serial(
        port="/dev/tty.usbmodem101",
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    ser.flush()
    
while True:
    try:
        x = urllib.request.urlopen("https://robots.benax.rw/commands.php").read()
        y = json.loads(x)
        for k in range(len(y)):
            command = y[k]["command"]
            command_as_bytes = bytes(command+"\n","UTF-8")
            ser.write(command_as_bytes)
            line = ser.readline().decode("utf-8").rstrip()
            #print(line)
    except:
        print("Listening to new commands...")
    sleep(0.5)
