from picamera import PiCamera
from time import sleep
import datetime
from termcolor import colored

class CameraCapture:
    def __init__(self, d):
        self.rate = 1
        self.d = d #Sensor Data
        self.camera = PiCamera()
        
    def setRate(self,r):
        self.rate = r

    def capture(self):


        #self.camera.start_preview()
        while True:
            sleep(1/self.rate)
            #camera.capture('home/pi/Desktop/test.jpg');
            dt = datetime.datetime.now()
            dtstr = dt.strftime('%H_%M_%S')
            print colored(("Picture captured at " + self.d.gpstimestr), "yellow")
            print colored(self.d.lat,"cyan")
            print colored(self.d.lon,"cyan")
            if self.d.lat != '':
                self.camera.capture('Stills/' + self.d.gpstimestr + '_' +  str(self.d.lat) + "_" + str(self.d.lon) + '.jpg')
            else:
                self.camera.capture('Stills/' + self.d.gpstimestr + '.jpg')
        self.camera.stop_preview()
       
