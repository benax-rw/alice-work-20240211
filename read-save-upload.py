#!/usr/bin/env python3
import serial
import requests

ser = serial.Serial(
        port='/dev/tty.usbserial-1110', #plz change this according to your port number
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
ser.flush()     
if __name__ == '__main__':
    while True:
        distance = ""
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            f=open("data.txt","a")
            f.write(line)
            f.write("\n")
            f.close()
            distance+=line+"\n"
        if distance.strip() != "":
            formData = {"device": "Microcontroller-Gabriel", "distance": distance}
            HTTP_Request = requests.post("http://insecure.benax.rw/iot/", data=formData)

            if HTTP_Request:
                HTTP_Response = HTTP_Request.text
                print(HTTP_Response)