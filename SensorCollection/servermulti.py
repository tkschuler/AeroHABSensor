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

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

sense = SenseHat()
sense.set_imu_config(True, True, True)
oldtime = time.time()

myFile = open('data2.csv', 'w')

'''This sends data back to clients'''


def newClient(clientsocket, addr):
    while True:
        msg = clientsocket.recv(1024)
        if msg == 'stabilization':
            print colored("Stabilization data requested.", 'white')
            clientsocket.send(str(roll) + "," + str(pitch) + "," + str(yaw))

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


'''All sensor collection code is in this function'''


def sensorCollection():
    # variables must be global for other threads to use
    global i, dt, lat, lon, alt, roll, pitch, yaw, time, temp, humi, pres, everything, ti, ts, oldtime, tf, rollrate, pitchrate, yawrate, oldroll, oldpitch, oldyaw
    
    
    oldpitch = 0
    oldroll = 0
    oldyaw = 0
    tf = datetime.time.second
    with myFile:
        writer = csv.writer(myFile, delimiter=',', lineterminator='\n', )
        writer.writerow(["Time,Altitude,Latitude,Longitude,Pitch,Roll,Yaw,Temperature,Humidity,Pressure"])
        while True:
            dt = datetime.datetime.now()
            ti = datetime.time.second
            dtstr = dt.strftime('%H:%M:%S')
            newtime = time.time()
            ts = newtime - oldtime
            oldtime = newtime
            print("Time step" + str(ts))

            # ddelta = ti - tf
            # print("time delta is " + ddelta)

            orientation = sense.get_orientation_degrees()
            accel = sense.get_accelerometer()
            print(sense.orientation);
            print('x: {pitch}, y: {roll}, z: {yaw}'.format(**accel))
            gyroS = ('{pitch},{roll},{yaw}').format(**orientation)

            i += 1
            if (orientation['pitch'] == 'n/a'):
                pitch = 'n/a'

            else:
                pitch = '{0:.6f}'.format(float(orientation['pitch']))

            if (orientation['roll'] == 'n/a'):
                roll = 'n/a'


            else:
                roll = '{0:.6f}'.format(float(orientation['roll']))


            if (orientation['yaw'] == 'n/a'):
                yaw = 'n/a'

            else:
                yaw = '{0:.6f}'.format(float(orientation['yaw']))


            print(ts)
            print(float(oldroll))
            print(float(roll))

            rollrate = (float(roll) - float(oldroll))/ts
            yawrate = (float(yaw) - float(oldyaw)) / ts
            pitchrate = (float(pitch) - float(oldpitch)) / ts

            oldroll = roll
            oldpitch = pitch
            oldyaw = yaw

            print(colored(('Roll Rate = '+ str(rollrate)), 'cyan'))
            print(colored(('Pitch Rate = '+ str(pitchrate)), 'cyan'))
            print(colored(('YawRate = ' + str(yawrate)), 'cyan'))

            temp = '{0:.6f}'.format(sense.temp)
            humi = '{0:.6f}'.format(sense.humidity)
            pres = '{0:.6f}'.format(sense.pressure)
            # roll += random.uniform(-10.0,10.0)
            # pitch += random.uniform(-10.0,10.0)
            # yaw += random.uniform(-10.0,10.0)
            # print "..."
            # print pitch,roll,yaw
            print "Time:        " + str(dtstr)
            print("Temperature: " + str(sense.temp) + " C")
            print("Humidity:    " + str(sense.humidity) + " rh")
            print("Pressure:    " + str(sense.pressure) + " Mb")
            print(gyroS)
            tf = datetime.time.second
            time.sleep(.1)
            for new_data in gps_socket:
                if new_data:
                    data_stream.unpack(new_data)
                    # print colored("Time:        " + str(dtstr),"green")
                    print(colored(('Altitude = ', data_stream.TPV['alt']), 'yellow'))
                    print(colored(('Latitude = ', data_stream.TPV['lat']), 'yellow'))
                    print(colored(('Longitude = ', data_stream.TPV['lon']), 'yellow'))
                    # i = 0
                    if (data_stream.TPV['alt'] == 'n/a'):
                        alt = 'n/a'

                    else:
                        alt = '{0:.6f}'.format(float(data_stream.TPV['alt']))

                    if (data_stream.TPV['lat'] == 'n/a'):
                        lat = 'n/a'

                    else:
                        lat = '{0:.6f}'.format(float(data_stream.TPV['lat']))

                    if (data_stream.TPV['lon'] == 'n/a'):
                        lon = 'n/a'

                    else:
                        lon = '{0:.6f}'.format(float(data_stream.TPV['lon']))

                    writer.writerow([dtstr, alt, lat, lon, pitch, roll, yaw, temp, humi, pres])
                    everyting = "" + dtstr + ", " + alt + ", " + lat + ", " + lon + ", " + pitch + ", " + roll + ", " + yaw + ", " + temp + ", " + humi + ", " + pres
                else:
                    print colored("No gps data", 'red')
                break


i = 0
roll = 1
pitch = 2
yaw = 3.1
s = socket.socket()  # Create a socket object
# host = '127.0.0.1' # Get local machine name
host = 'aerohab.eduroam.gmu.edu'
port = 50010  # Reserve a port for your service.

print 'Server started!'
print 'Waiting for clients...'

s.bind((host, port))  # Bind to the port
s.listen(5)  # Now wait for client connection.

sensor = Thread(target=sensorCollection)
sensor.daemon = True  # Allows you to exit the program with Ctr+c
sensor.start()

# Server must be in while open to stay open and listen
while True:
    c, addr = s.accept()  # Establish connection with client.
    print 'Got connection from', addr
    thread.start_new_thread(newClient, (c, addr))
s.close()
