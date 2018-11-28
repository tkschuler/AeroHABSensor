import datetime
import csv
from termcolor import colored
from sense_hat import SenseHat
from time import sleep
import time
from gps3 import gps3
import sys


'''This file colelcts data from the Sense Hat and GPS module and saves them to local variables.'''

class DataCollection:
    def __init__(self, datacsv, supressOutput):
        self.lat = self.lon = self.alt = 0.0
        self.roll = self.pitch = self.yaw = self.oldroll = self.oldpitch = self.oldyaw = 0.0
        self.rollrate = self.pitchrate = self.yawrate = 0.0
        self.temp = self.humi = self.pres = 0.0
        self.ti = self.ts = self.tf = self.dt = 0.0
        self.timestr = ''
        self.gpstimestr = ''
        self.datacsv = datacsv
        self.ON = True
        self.supressOutput = supressOutput

    def createFile(self):
        timestamp = datetime.datetime.now() #Date + timestamp
        timestr = timestamp.strftime('%Y-%m-%d_%H:%M:%S')
        self.f2 = open("Data/" + timestr +".csv", 'w')
        header = ",".join(["Time","Altitude","Latitude","Longitude","Pitch","Roll", "Yaw", \
                             "Pitch Rate","Roll Rate","Yaw Rate","Temperature","Humidity","Pressure"])
        self.f2.write(header + "\n")
        print self.datacsv + " created."
        

    def write2File(self):
        try:
            everything = ",".join([str(self.timestr),str(self.alt),str(self.lat),str(self.lon), \
                                 str(self.pitch),str(self.roll),str(self.yaw), \
                                 str(self.pitchrate),str(self.rollrate),str(self.yawrate), \
                                 str(self.temp),str(self.humi),str(self.pres)])   
            self.f2.write(everything+ '\n')
        except:
            print "Couldn't write to file."
        print "writing..."

    def collectData(self):
        self.tf = datetime.time.second
        gps_socket = gps3.GPSDSocket()
        data_stream = gps3.DataStream()
        gps_socket.connect()
        gps_socket.watch()

        sense = SenseHat()
        sense.set_imu_config(True, True, True)

        self.createFile()
        

        while self.ON:
            '''Collect Sense Hat Data'''
            timestamp = datetime.datetime.now() #Date + timestamp
            self.timestr = timestamp.strftime('%H:%M:%S.%f') #pretty format timestamp
            self.gpstimestr = timestamp.strftime('%H:%M:%S') #pretty format for GPS 
            self.tf = time.time()
            self.dt = self.tf - self.ti
            self.ti = self.tf
            orientation = sense.get_orientation_degrees()
            gyroS = ('{pitch},{roll},{yaw}').format(**orientation)

            if (orientation['pitch'] == 'n/a'):
                self.pitch = 'n/a'

            else:
                self.pitch = '{0:.6f}'.format(float(orientation['pitch']))

            if (orientation['roll'] == 'n/a'):
                self.roll = 'n/a'


            else:
                self.roll = '{0:.6f}'.format(float(orientation['roll']))

            if (orientation['yaw'] == 'n/a'):
                self.yaw = 'n/a'

            else:
                self.yaw = '{0:.6f}'.format(float(orientation['yaw']))

            self.rollrate = (float(self.roll) - float(self.oldroll)) / self.dt
            self.yawrate = (float(self.yaw) - float(self.oldyaw)) / self.dt
            self.pitchrate = (float(self.pitch) - float(self.oldpitch)) / self.dt

            self.oldroll = self.roll
            self.oldpitch = self.pitch
            self.oldyaw = self.yaw

            self.temp = '{0:.6f}'.format(sense.temp)
            self.humi = '{0:.6f}'.format(sense.humidity)
            self.pres = '{0:.6f}'.format(sense.pressure)
            
            #collect GPS Data
            for new_data in gps_socket:
                if new_data:
                    #print colored(new_data,"green")
                    data_stream.unpack(new_data)
                    if (data_stream.TPV['alt'] == 'n/a'):
                        self.alt = ''

                    else:
                        self.alt = '{0:.6f}'.format(float(data_stream.TPV['alt']))

                    if (data_stream.TPV['lat'] == 'n/a'):
                        self.lat = ''

                    else:
                        self.lat = '{0:.6f}'.format(float(data_stream.TPV['lat']))

                    if (data_stream.TPV['lon'] == 'n/a'):
                        self.lon = ''

                    else:
                        self.lon = '{0:.6f}'.format(float(data_stream.TPV['lon']))

                else:
                    print colored("No gps data", 'red')
                break
            
            if (self.supressOutput != True):
                 print("Time Stamp: " + str(self.timestr))
                 
                 print(colored(('Roll: ' + str(self.roll)), 'magenta'))
                 print(colored(('Pitch: ' + str(self.pitch)), 'magenta'))
                 print(colored(('Yaw: ' + str(self.yaw)), 'magenta'))
                 
                 print(colored(('Roll Rate: ' + str(self.rollrate)), 'cyan'))
                 print(colored(('Pitch Rate: ' + str(self.pitchrate)), 'cyan'))
                 print(colored(('YawRate: ' + str(self.yawrate)), 'cyan'))
                 
                 print("Temperature: " + self.temp + " C")
                 print("Humidity:    " + self.humi + " rh")
                 print("Pressure:    " + self.pres + " Mb")
                 
                 print(colored(('Altitude: ', self.alt), 'yellow'))
                 print(colored(('Latitude: ', self.lat), 'yellow'))
                 print(colored(('Longitude: ',self.lon), 'yellow'))
                 

            self.write2File()
            print self.timestr
            time.sleep(.1) #currently set to 10 Hz
        
        self.f2.close()
        print self.datacsv + " closed."

'''Main Loop for testing'''
#d = DataCollection("test.csv")
#d.createFile()
#d.collectData()
