from picamera import PiCamera
from time import sleep
import datetime

#camera = PiCamera()

#camera.start_preview()
while True:
    sleep(1)
    dt = datetime.datetime.now()
    dtstr = dt.strftime('%m-%d-%Y-%H_%M_%S')
    print dtstr
    #camera.capture('/home/pi/Desktop/Stills/' + dtstr + '.jpg')
#camera.stop_preview()