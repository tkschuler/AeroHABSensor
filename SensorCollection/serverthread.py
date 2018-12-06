import socket
import time
import sys
from termcolor import colored
import thread
from threading import Thread

'''This file opens a socketed server thread and parses incomming messages to send unique
data packets to multiple clients'''

class Server:
    def __init__(self,d,port,host):
        self.s = None
        self.c = None
        self.addr = None
        self.port = port
        self.host = host
        self.d = d 
        self.msg = "hey"
        self.server = None
        self.ON = True
        self.numberOfClients = 0
        
    def newClient2(self,clientsocket, addr):
        while True:
            print "Number of Clients" , self.numberOfClients
            msg = clientsocket.recv(4)
            print colored(msg,"green")
            if msg == 's':
                print colored((self.d.timestr + "   Stabilization data requested."), 'green')
                clientsocket.send(str(self.d.roll) + "," + str(self.d.pitch) + "," + str(self.d.yaw))

            elif msg == "f\n":
                print colored((self.d.timestr + "   Fault Management data requested."), 'green')
                clientsocket.send(str(self.d.timestr) + "," + str(self.d.alt) + "," + str(self.d.lat) + "," + str(self.d.lon) + ","\
                                  + str(self.d.pitch) + "," + str(self.d.roll) + "," + str(self.d.yaw) + "," \
                                  + str(self.d.rollrate) + "," + str(self.d.pitchrate) + "," + str(self.d.yawrate) + ","\
                                  + str(self.d.temp) + "," + str(self.d.pres) + "," + str(self.d.humi) + "\n")

            elif msg == "t\n":
                print colored((self.d.timestr + "   Telemetry data requested."), 'green')
                clientsocket.send(str(self.d.tf) + "," + str(self.d.lat) + "," + str(self.d.lon) + "," + str(self.d.alt) + + "," \
                                  + str(self.d.pitch) + "," + str(self.d.roll) + "," + str(self.d.yaw) + "," \
                                  + str(self.d.temp) + "," + str(self.d.pres) + "," + str(self.d.humi) + "\n")


            # Close the connection if the client is terminated.
            elif msg == "close":
                print colored(("Connection " + str(addr) + " closed."), "magenta")
                break
            
            else:
                print colored("Unrecognized message requeset.", "red")
                clientsocket.send("Error")
                break

        clientsocket.close()
        self.numberOfClients += -1
        
    def connect(self):
    
        self.s = socket.socket()

        print 'Server started!'
        print 'Waiting for clients...'

        self.s.bind((self.host, self.port))  # Bind to the port
        self.s.listen(5)  #Wait for client connection, up to 5.
        
    def listen(self):
        # Server must be in while open to stay open and listen
        while self.ON:
            try:
                c,addr = self.s.accept()  # Establish connection with client.
                print colored(('Got connection from' + str(addr)),"magenta")
                self.numberOfClients += 1
                self.server = Thread(target=self.newClient2, args=((c,addr)))
                self.server.daemon = True
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
    
