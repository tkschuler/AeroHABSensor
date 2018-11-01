#!/usr/bin/env python

import socket
import time
import sys
from termcolor import colored

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
        print colored("received data:",'yellow'), data
        time.sleep(1)
    except (KeyboardInterrupt, socket.error), e:
        try:
            s.send("close")
            s.close()
            print colored("Connection closed",'red')
            sys.exit()
        except socket.error:
            s.close()
            print colored("Connection closed unexpectedly. Check Server state...",'red')
            sys.exit()

s.close() 
