#!/usr/bin/env python3
import serial
import time
if __name__ == '__main__':
    ser = serial.Serial(
        port='/dev/tty.usbmodem101',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    ser.flush()

    while True:
        ser.write(b"forward 3\n")
        ser.write(b"stop 2\n")
        ser.write(b"reverse 3\n")
        ser.write(b"stop 2\n")
                
        time.sleep(0.5)
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
