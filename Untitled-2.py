#!/usr/bin/env python
import time
import serial
import sys
import math
import urllib
import http.client
import pynmea2

id = 'pi-SIM'
server = 'insecure.benax.rw'
period = 1

ser = serial.Serial(
    port='/dev/serial0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter=0

conn = http.client.HTTPConnection(server)


def send(conn, lat, lon):
    params = (('id', id), ('timestamp', int(time.time())), ('lat', lat), ('lon', lon))
    
    try:
        conn.request('GET', '/pydata/gps.php?' + urllib.parse.urlencode(params))
        conn.getresponse().read()
    except NameError:
      print("Unable to communicate with the host!")
    except:
      print("Something else went wrong")    
    


while 1:
    nmea = ser.readline()[0:].decode("utf-8").strip()
    tokens = nmea.split(",")
    if tokens[0]=="$GPRMC":
        print(nmea)
        msg = pynmea2.parse(nmea)
        lat = msg.latitude
        lon = msg.longitude
        send(conn, lat, lon)          

    time.sleep(period)