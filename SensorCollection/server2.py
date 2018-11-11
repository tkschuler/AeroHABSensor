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

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

sense = SenseHat()
sense.set_imu_config(True, True, True)

print "hello"

'''This sends data back to clients'''


def newClient(clientsocket, addr):
    while True:
        msg = clientsocket.recv(1024)
        print str(msg) + "........................"
        if msg == 'stabilization':
            print colored("Stabilization data requested.", 'white')
            clientsocket.send(str(d.roll) + "," + str(d.pitch) + "," + str(d.yaw))
            #clientsocket.send("testing...")

        elif msg == 'faultmanagement':
            print "Fault Management data requested."
            clientsocket.send(rollrate + "," + pitchrate + "," + yawrate)

        elif msg == 'telemetry':
            print colored("Telemetry data requested.", "white")
            # clientsocket.send("12.44,56.777,12.333,4.555")
            clientsocket.send(everything)


        # Close the connection if the client is terminated.
        elif msg == "close":
            print colored(("Connection " + str(addr) + " closed."), "magenta")
            break

        else:
            print colored("Unrecognized message requeset.", "red")
            clientsocket.send("Error")

    clientsocket.close()

s = socket.socket()  # Create a socket object
#host = '127.0.0.1' # Get local machine name
#host = 'aerohab.eduroam.gmu.edu'
host = '127.0.0.1'
port = 50000  # Reserve a port for your service.

print 'Server started!'
print 'Waiting for clients...'

s.bind((host, port))  # Bind to the port
s.listen(3)  # Now wait for client connection.

d = datacollectionthread.DataCollection("test.csv")

sensor = Thread(target=d.collectData)
sensor.daemon = True  # Allows you to exit the program with Ctr+c
sensor.start()

# Server must be in while open to stay open and listen
while True:
    c, addr = s.accept()  # Establish connection with client.
    print 'Got connection from', addr
    thread.start_new_thread(serverthread.newClient, (c, addr,d))
s.close()

