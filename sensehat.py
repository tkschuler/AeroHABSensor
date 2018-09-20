from sense_hat import SenseHat
from time import sleep
import datetime

sense = SenseHat()
sense.set_imu_config(True, True, True)

while True:
    #sleep(1)
    dt = datetime.datetime.now()
    dtstr = dt.strftime('%H:%M:%S')
    
    orientation = sense.get_orientation_degrees()
    print(("Pitch:   {pitch}\n" + 
          "Roll:     {roll}\n" +  
          "Yaw:      {yaw}\n").format(**orientation))
    
    print "Time:        " + str(dtstr)
    print("Temperature: " + str(sense.temp) + " C")
    print("Humidity:    " + str(sense.humidity) + " rh")
    print("Pressure:    " + str(sense.pressure) + " Mb")

    print("-------------------------------------")


