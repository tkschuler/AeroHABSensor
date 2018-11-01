#!/usr/bin/python

import socket
import thread
from threading import Thread
import time
import random
from termcolor import colored

'''This sends data back to clients'''
def newClient(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        if msg == 'stabilization':
            print colored("Stabilization data requested.",'white')
            clientsocket.send(str(roll)+","+str(pitch)+","+str(yaw))
        elif msg == 'faultmanagement':
            print "Fault Management data requested."
            clientsocket.send("1010101010,1010101010,101010101")
        elif msg == 'telemetry':
            print colored("Telemetry data requested.","white")
            clientsocket.send("12.44,56.777,12.333,4.555")
        #Close the connection if the client is terminated.
        elif msg == "close":
            print colored(("Connection "+ str(addr) + " closed."),"magenta")
            break
        else:
            print colored("Unrecognized message requeset.","red")
    clientsocket.close()



'''All sensor collection code is in this function'''
def sensorCollection():
    #variables must be global for other threads to use
    global i, lat, lon, alt, roll, pitch, yaw, time
    while True:
        i+= 1
        roll += random.uniform(-10.0,10.0)
        pitch += random.uniform(-10.0,10.0)
        yaw += random.uniform(-10.0,10.0)
        #print "..."
        print pitch,roll,yaw
        time.sleep(.1)


i = 0
roll = 1
pitch = 2
yaw = 3.1
s = socket.socket()         # Create a socket object
host = '127.0.0.1' # Get local machine name
port = 50010               # Reserve a port for your service.

print 'Server started!'
print 'Waiting for clients...'

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

sensor = Thread(target = sensorCollection)
sensor.daemon = True  #Allows you to exit the program with Ctr+c
sensor.start()

# Server must be in while open to stay open and listen
while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    thread.start_new_thread(newClient,(c,addr))
s.close()
