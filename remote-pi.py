#!/usr/bin/env python3
from os import system,popen
import urllib.parse
import json
import urllib.request
import sys
import serial
from time import sleep


system("clear")
print("Benax::")
print("++++++++++++++++++++++")
print("Listening ...")

if __name__ == "__main__":

def writeToSerial(mPort):
    mSer = serial.Serial(
        port=mPort,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    return mSer

while True:
    try:
        url = "https://robots.benax.rw/commands.php"
        headers = {"User-Agent" : "Mozilla/5.0"}
        req = urllib.request.Request(url , headers=headers)
        with urllib.request.urlopen(req) as f:
            x = f.read().decode('utf-8')
            y = json.loads(x)
            for k in range(len(y)):
                command = y[k]["command"]
                print(command) 
                command_as_bytes = bytes(command+"\n","UTF-8")
                ser = writeToSerial("/dev/ttyACM0")
                ser.write(command_as_bytes)
                line = ser.readline().decode("utf-8").rstrip()
                #print(line)
    except:
        print("...")
    sleep(0.5)
