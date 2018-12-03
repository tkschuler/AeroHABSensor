import socket
import time
import sys
from termcolor import colored
import thread
from threading import Thread
from sense_hat import SenseHat

class SenseLight:
    def __init__(self,d,s):
        self.server = s
        self.s = SenseHat()
        self.d = d
        self.s.low_light = True
        self.c = None
        self.green = (0, 255, 0)
        self.yellow = (255, 255, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.white = (255,255,255)
        self.nothing = (0,0,0)
        self.pink = (255,105, 180)
        self.count = 0
        
    def GPS(self):
        P = self.pink
        O = self.nothing
        B = self.blue
        logo = [
        O, O, O, O, O, O, B, B,
        O, O, O, O, O, O, B, B,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo
        
    def GPSandServer(self):
        G = self.green
        O = self.nothing
        B = self.blue
        logo = [
        G, G, O, O, O, O, B, B,
        G, G, O, O, O, O, B, B,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo
    
    def GPSandServerClient2(self):
        G = self.green
        O = self.nothing
        B = self.blue
        Y = self.yellow
        P = self.pink
        logo = [
        G, G, O, O, O, O, B, B,
        G, G, O, O, O, O, B, B,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        P, P, Y, Y, O, O, O, O,
        P, P, Y, Y, O, O, O, O,
        ]
        return logo
    
    def GPSandServerClient1(self):
        G = self.green
        O = self.nothing
        B = self.blue
        Y = self.yellow
        P = self.pink
        logo = [
        G, G, O, O, O, O, B, B,
        G, G, O, O, O, O, B, B,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        P, P, O, O, O, O, O, O,
        P, P, O, O, O, O, O, O,
        ]
        return logo
        
    def Server(self):
        G = self.green
        O = self.nothing
        B = self.blue
        logo = [
        G, G, O, O, O, O, O, O,
        G, G, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo
    
    def Server1Client(self):
        G = self.green
        O = self.nothing
        P = self.pink
        B = self.blue
        logo = [
        G, G, O, O, O, O, O, O,
        G, G, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        P, P, O, O, O, O, O, O,
        P, P, O, O, O, O, O, O,
        ]
        return logo
    
        
    def Server2Client(self):
        G = self.green
        O = self.nothing
        P = self.pink
        B = self.blue
        Y = self.yellow
        logo = [
        G, G, O, O, O, O, O, O,
        G, G, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        P, P, Y, Y, O, O, O, O,
        P, P, Y, Y, O, O, O, O,
        ]
        return logo
    
        
    def Client1(self):
        G = self.green
        O = self.nothing
        P = self.pink
        B = self.blue
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        P, P, O, O, O, O, O, O,
        P, P, O, O, O, O, O, O,
        ]
        return logo
    
    def Client2(self):
        G = self.green
        O = self.nothing
        P = self.pink
        B = self.blue
        Y = self.yellow
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        P, P, Y, Y, O, O, O, O,
        P, P, Y, Y, O, O, O, O,
        ]
        return logo
        
    def Off(self):
        P = self.pink
        O = self.nothing
        B = self.blue
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo


    def GPSDisplay(self):
      images = [self.GPS, self.Off]
      self.s.set_pixels(images[self.count % len(images)]())
      time.sleep(.5)
      self.count += 1
      
    def GPSandServerDisplay(self):
      images = [self.GPSandServer, self.GPS, self.GPSandServer, self.GPS, self.GPSandServer, self.Off, self.Server, self.Off, self.Server, self.Off]
      self.s.set_pixels(images[self.count % len(images)]())
      time.sleep(.1)
      self.count += 1

    def ServerDisplay(self):
      images = [self.Server, self.Off]
      self.s.set_pixels(images[self.count % len(images)]())
      time.sleep(.1)
      self.count += 1
      
    def Server1ClientDisplay(self):
      images = [self.Server1Client, self.Client1]
      self.s.set_pixels(images[self.count % len(images)]())
      time.sleep(.1)
      self.count += 1
      
    def Server2ClientDisplay(self):
      images = [self.Server2Client, self.Client2]
      self.s.set_pixels(images[self.count % len(images)]())
      time.sleep(.1)
      self.count += 1
      
    def Server1ClientGPSDisplay(self):
      images = [self.GPSandServerClient1, self.GPS, self.GPSandServerClient1, self.GPS, self.GPSandServerClient1, self.Client1, self.Server1Client, self.Client1, self.Server1Client, self.Client1]
      self.s.set_pixels(images[self.count % len(images)]())
      time.sleep(.1)
      self.count += 1
      
    def Server2ClientGPSDisplay(self):
      images = [self.GPSandServerClient2, self.GPS, self.GPSandServerClient2, self.GPS, self.GPSandServerClient2, self.Client2, self.Server2Client, self.Client2, self.Server2Client, self.Client2]
      self.s.set_pixels(images[self.count % len(images)]())
      time.sleep(.1)
      self.count += 1
      
    def LED_STATUS(self):
        while True:
            if self.d.lat == '' or self.d.lat == 0.0:
                if self.server.numberOfClients == 1:
                    self.Server1ClientDisplay()
                elif self.server.numberOfClients == 2:
                    self.Server2ClientDisplay()
                else:
                    self.ServerDisplay()
            else:
                if self.server.numberOfClients == 1:
                    self.Server1ClientGPSDisplay()
                elif self.server.numberOfClients == 2:
                    self.Server2ClientDisplay()
                else:
                    self.GPSandServerDisplay()

#s = SenseHat()
#s.low_light = True

#SL = SenseLight(s)
#SL.LEDSTATUS()
#while True: 
    #SL.GPSDisplay()
    #SL.GPSandServerDisplay()
    #SL.ServerDisplay()
