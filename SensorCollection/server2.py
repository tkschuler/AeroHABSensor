#!/usr/bin/python

'''Organization: George Mason University

   Author: Tristan Schuler
           Loren Druitt
           Ryan Mays
           
   v2.0
   
   This main file starts a server thread and data collection thread.  The Data collection thread
   collects/parses data from a Sense Hat and GPS, stores the variables locally, and also writes
   them to a csv file.  The Server thread allows multiple clients to request unique data packets
   from the data thread.
'''

import socket
import thread
from threading import Thread
import time
import random
from termcolor import colored
from sense_hat import SenseHat
from time import sleep
from gps3 import gps3
import datetime
import csv
import datacollectionthread
import serverthread
import signal

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

sense = SenseHat()
sense.set_imu_config(True, True, True)

#print "Data Collection Activated."

d = datacollectionthread.DataCollection("test.csv")
s = serverthread.Server(d)

def signal_handler(sig, frame):
        d.ON = False #Stop Thread
        #time.sleep(1) #wait a second so we don't try writing to a closed file
        s.close()
        time.sleep(.5)
        print('Program terminated')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

sensor = Thread(target=d.collectData)
sensor.daemon = True  # Allows you to exit the program with Ctr+c
sensor.start()

s.connect()
s.listen()


