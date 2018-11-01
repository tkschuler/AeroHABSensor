#!/usr/bin/env python

import socket
import fcntl, os
import time
import sys

TCP_IP = '127.0.0.1'
#TCP_IP = '10.151.131.32'
#TCP_IP = 'aerohab.eduroam.gmu.edu'

TCP_PORT = 50010
BUFFER_SIZE = 1024
MESSAGE = "stabilization"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while 1:
    try:
        s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        print "received data:", data
        time.sleep(1)
    except KeyboardInterrupt:
        print "Connection closed"
        s.send("close")
        s.close()
        sys.exit()
