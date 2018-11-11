#!/usr/bin/python

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

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

sense = SenseHat()
sense.set_imu_config(True, True, True)

print "Data Collection Activated."
    
d = datacollectionthread.DataCollection("test.csv")

sensor = Thread(target=d.collectData)
sensor.daemon = True  # Allows you to exit the program with Ctr+c
sensor.start()

s = serverthread.Server()
s.connect()
s.listen()


