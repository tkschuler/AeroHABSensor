#!/usr/bin/python

import socket
import thread
from threading import Thread
import time


'''This sends data back to clients'''
def newClient(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        if msg == 'stabilization':
            print i, addr
            clientsocket.send(str(roll)+","+str(pitch)+","+str(yaw))
        elif msg == 'faultmanagement':
            print i, addr
            clientsocket.send("1010101010,1010101010,101010101")
        elif msg == 'telemetry':
            print i, addr
            clientsocket.send("12.44,56.777,12.333,4.555")
        #Close the connection if the client is terminated.
        elif msg == "close":
            print "Connection", addr, "closed."
            break
        else:
            print "Unrecognized message request."
    clientsocket.close()



'''All sensor collection code is in this function'''
def sensorCollection():
    #variables must be global for other threads to use
    global i, lat, lon, alt, roll, pitch, yaw, time
    while True:
        i+= 1
        print "..."
        time.sleep(.5)


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
