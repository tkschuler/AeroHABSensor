import socket
import time
import sys
from termcolor import colored
import thread
from threading import Thread

'''This file opens a socketed server thread and parses incomming messages to send unique
data packets to multiple clients'''

class Server:
    def __init__(self,d):
        self.s = None
        self.c = None
        self.addr = None
        self.d = d 
        self.msg = "hey"
        self.server = None
        self.ON = True
        
    def newClient2(self,clientsocket, addr):
        while True:
            msg = clientsocket.recv(4)
            print msg
            if msg == 'stabilization':
                print colored((self.d.timestr + "   Stabilization data requested."), 'green')
                clientsocket.send(str(self.d.roll) + "," + str(self.d.pitch) + "," + str(self.d.yaw))

            if msg == 'f':
                print colored((self.d.timestr + "   Fault Management data requested."), 'green')
                clientsocket.send(str(self.d.rollrate) + "," + str(self.d.pitchrate) + "," + str(self.d.yawrate))

            elif msg == 'telemetry':
                clientsocket.send(str(self.d.tf) + "," + str(self.d.lat) + "," + str(self.d.lon) + "," + str(self.d.alt) \
                                  + str(self.d.roll) + "," + str(self.d.pitch) + "," + str(self.d.yaw) \
                                  + str(self.d.temp) + "," + str(self.d.pres) + "," + str(self.d.humi))


            # Close the connection if the client is terminated.
            elif msg == "close":
                print colored(("Connection " + str(addr) + " closed."), "magenta")
                break
            
            else:
                print colored("Unrecognized message requeset.", "red")
                clientsocket.send("Error")
                break

        clientsocket.close()
        
    def connect(self):
    
        self.s = socket.socket()
        host = '127.0.0.1'
       # host = '192.168.1.1'
        port = 5000  # Reserve a port for your server.

        print 'Server started!'
        print 'Waiting for clients...'

        self.s.bind((host, port))  # Bind to the port
        self.s.listen(5)  #Wait for client connection, up to 5.
        
    def listen(self):
        # Server must be in while open to stay open and listen
        while self.ON:
            try:
                c,addr = self.s.accept()  # Establish connection with client.
                print colored(('Got connection from' + str(addr)),"magenta")
                self.server = Thread(target=self.newClient2, args=((c,addr)))
                self.server.daemon = True
                print "made it here"
                self.server.start()
            except:
                print colored("Socket Error.", "red")
                sys.exit()
                
        self.s.close()
        
    #Stop server manually
    def close(self):
        self.ON = False
        print "Server closed."
        
'''Main loop for testing'''
#s = Server()
#s.connect()
#s.listen()
    
