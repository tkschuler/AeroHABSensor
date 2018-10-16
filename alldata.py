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

myFile = open('data.csv', 'w')

with myFile:
    writer = csv.writer(myFile, delimiter=',',lineterminator='\n',)
    while True:
        #writer.writerow(['Hey!'])
        dt = datetime.datetime.now()
        dtstr = dt.strftime('%H:%M:%S')
        #Array order: time, latitude, longitude, altitude, roll, pitch, yaw, temperature, humidity, pressure, voltage
        
        orientation = sense.get_orientation_degrees()
        print(("Pitch:   {pitch}\n" + 
              "Roll:     {roll}\n" +  
              "Yaw:      {yaw}\n").format(**orientation))
        
        gyroS = ('{pitch},{roll},{yaw}').format(**orientation)
        
        temp = '{0:.6f}'.format(sense.temp)
        humi = '{0:.6f}'.format(sense.humidity)
        pres = '{0:.6f}'.format(sense.pressure)
        print "Time:        " + str(dtstr)
        print("Temperature: " + str(sense.temp) + " C")
        print("Humidity:    " + str(sense.humidity) + " rh")
        print("Pressure:    " + str(sense.pressure) + " Mb")

        for new_data in gps_socket:
            if new_data:
                data_stream.unpack(new_data)
                print colored("Time:        " + str(dtstr),"green")
                print(colored(('Altitude = ', data_stream.TPV['alt']),'yellow'))
                print(colored(('Latitude = ', data_stream.TPV['lat']),'yellow'))
                print(colored(('Longitude = ', data_stream.TPV['lon']),'yellow'))
                #i = 0
                if(data_stream.TPV['alt'] == 'n/a'):
                    alt = 'n/a'
                
                else:
                    alt = '{0:.6f}'.format(float(data_stream.TPV['alt']))
                
                if(data_stream.TPV['lat'] == 'n/a'):
                    lat = 'n/a'
                
                else:
                    lat = '{0:.6f}'.format(float(data_stream.TPV['lat']))
                
                if(data_stream.TPV['lon'] == 'n/a'):
                    lon = 'n/a'
                
                else:
                    lon = '{0:.6f}'.format(float(data_stream.TPV['lon']))
                

                writer.writerow([dtstr,data_stream.TPV['alt'],data_stream.TPV['lat'],data_stream.TPV['lon'],gyroS,temp,humi,pres])
            else:
                print colored("No gps data",'red')
            break
        sleep(.25)
    
    print("-------------------------------------")
    



