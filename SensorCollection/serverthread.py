import socket
import time
import sys
from termcolor import colored

class DataCollection:

    def newClient(clientsocket, addr, d):
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