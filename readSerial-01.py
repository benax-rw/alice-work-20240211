#!/usr/bin/env python3

import serial

ser = serial.Serial(
        port='/dev/cu.usbserial-110', #plz change this according to your port number
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

ser.flush()


if __name__ == '__main__':
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            f=open("smser.txt","a")
            f.write(line)
            f.write("\n")
            f.close()
            print(line)
