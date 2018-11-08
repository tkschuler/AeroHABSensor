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
            #clientsocket.send("12.44,56.777,12.333,4.555")
            clientsocket.send(everything)
        #Close the connection if the client is terminated.
        elif msg == "close":
            print colored(("Connection "+ str(addr) + " closed."),"magenta")
            break
        else:
            print colored("Unrecognized message requeset.","red")
    clientsocket.close()