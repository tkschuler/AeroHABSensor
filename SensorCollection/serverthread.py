import socket
import time
import sys
from termcolor import colored
import thread
from threading import Thread

class Server:
    def __init__(self):
        self.s = None
        self.c = None
        self.addr = None
        self.msg = "hey"
        
    def newClient2(self,clientsocket, addr):
        while True:
            msg = clientsocket.recv(1024)
            print str(msg) + "........................"
            if msg == 'stabilization':
                print colored("Stabilization data requested.", 'white')
                #clientsocket.send(str(d.roll) + "," + str(d.pitch) + "," + str(d.yaw))
                clientsocket.send("testing...")

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
        
    def connect(self):
    
        self.s = socket.socket()
        host = '127.0.0.1'
        port = 50058  # Reserve a port for your service.

        print 'Server started!'
        print 'Waiting for clients...'

        self.s.bind((host, port))  # Bind to the port
        self.s.listen(3)  # Now wait for client connection.
        
    def listen(self):
        # Server must be in while open to stay open and listen
        while True:
            try:
                c,addr = self.s.accept()  # Establish connection with client.
                print 'Got connection from', addr
                #s = serverthread.Server()
                #thread.start_new_thread(self.newClient2, (c, addr))
                server = Thread(target=self.newClient2, args=((c,addr)))
                server.daemon = True
                print "made it here"
                server.start()
            except:
                print colored("Socket Error.", "red")
                sys.exit()
                
        self.s.close()
    

#s = Server()
#s.connect()
#s.listen()
    