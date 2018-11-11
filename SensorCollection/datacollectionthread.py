import datetime
import csv
from termcolor import colored
#from sense_hat import SenseHat
from time import sleep
#from gps3 import gps3


class DataCollection:
    def __init__(self, datacsv):
        self.lat = self.lon = self.alt = 0.0
        self.roll = self.pitch = self.yaw = self.oldroll = self.oldpitch = self.oldyaw = self.rollrate = self.pitchrate = self.yawrate = 0.0
        self.temp = self.humi = self.pres = 0.0
        self.ti = self.ts = self.tf = self.dt = 0.0
        self.datacsv = datacsv
        self.f = open(self.datacsv, 'w')

    def createFile(self):
        with open(self.datacsv, 'w'):
            writer = csv.writer(self.f, delimiter=',', lineterminator='\n', )
            writer.writerow(["Time","Altitude,Latitude,Longitude,Pitch,Roll,Yaw,Temperature,Humidity,Pressure"])
        #self.f.close()
        print self.datacsv + " created."

    def write2File(self):
        with open(self.datacsv, 'w'):
            writer = csv.writer(self.f, delimiter=',', lineterminator='\n', )
            writer.writerow(["stuff","stuff2","stuff3"])
        print "writing"


    def collectData(self):
        self.tf = datetime.time.second
        gps_socket = gps3.GPSDSocket()
        data_stream = gps3.DataStream()
        gps_socket.connect()
        gps_socket.watch()

        sense = SenseHat()
        sense.set_imu_config(True, True, True)

        while True:
            #dt = datetime.datetime.now()
            #self.ti = datetime.time.second
            #dtstr = dt.strftime('%H:%M:%S')
            #newtime = time.time()
            self.tf = time.time()
            self.dt = self.ti - self.tf
            self.ti = self.tf
            print("Time step" + str(self.dtdt))

            # ddelta = ti - tf
            # print("time delta is " + ddelta)

            orientation = sense.get_orientation_degrees()
            accel = sense.get_accelerometer()
            print(sense.orientation);
            print('x: {pitch}, y: {roll}, z: {yaw}'.format(**accel))
            gyroS = ('{pitch},{roll},{yaw}').format(**orientation)

            i += 1
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

            print(colored(('Roll Rate = ' + str(self.rollrate)), 'cyan'))
            print(colored(('Pitch Rate = ' + str(self.pitchrate)), 'cyan'))
            print(colored(('YawRate = ' + str(self.yawrate)), 'cyan'))

            print(colored('Roll Rate = ', self.rollrate, 'cyan'))
            print(colored('Pitch Rate = ', self.pitchrate, 'cyan'))
            print(colored('YawRate = ', self.yawrate, 'cyan'))

            self.temp = '{0:.6f}'.format(sense.temp)
            self.humi = '{0:.6f}'.format(sense.humidity)
            self.pres = '{0:.6f}'.format(sense.pressure)
            # roll += random.uniform(-10.0,10.0)
            # pitch += random.uniform(-10.0,10.0)
            # yaw += random.uniform(-10.0,10.0)
            # print "..."
            # print pitch,roll,yaw
            #print "Time:        " + str(dtstr)
            print("Temperature: " + self.temp + " C")
            print("Humidity:    " + self.humi + " rh")
            print("Pressure:    " + self.pres + " Mb")
            #print(gyroS)
            #tf = datetime.time.second
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
                        self.alt = 'n/a'

                    else:
                        self.alt = '{0:.6f}'.format(float(data_stream.TPV['alt']))

                    if (data_stream.TPV['lat'] == 'n/a'):
                        self.lat = 'n/a'

                    else:
                        self.lat = '{0:.6f}'.format(float(data_stream.TPV['lat']))

                    if (data_stream.TPV['lon'] == 'n/a'):
                        self.lon = 'n/a'

                    else:
                        self.lon = '{0:.6f}'.format(float(data_stream.TPV['lon']))

                    #writer.writerow([dtstr, alt, lat, lon, pitch, roll, yaw, temp, humi, pres])
                    #everyting = "" + dtstr + ", " + alt + ", " + lat + ", " + lon + ", " + pitch + ", " + roll + ", " + yaw + ", " + temp + ", " + humi + ", " + pres
                else:
                    print colored("No gps data", 'red')
                break




d = DataCollection("test.csv")
#d.createFile()
#for i in range (0,5):
#    d.write2File()

d.collectData()
