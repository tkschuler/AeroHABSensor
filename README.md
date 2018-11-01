<img src="AerospaceCorpLogo.png" align="right" height = "100" /> <img src="GMULogo.png" align="right" height = "120" />

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/pypi/pyversions/event-bus-py2.svg)](https://www.python.org/download/releases/2.7/)

## AeroHab Sensing
This balloon is designed using specifications by the **Global Space Balloon challenge**. 
https://www.balloonchallenge.org/

The project has been sponsored by **The Aerospace Corporation**
https://aerospace.org/

## Overview

Aerohab Sensing is software designed for recording and processing realtime data from a high altitude weather balloon.  This data includes:
- **GPS data** : latitude,longitude,altitude
- **Environmental Data** : temperature, humidity, pressure
- **Orientation Data** : roll, pitch, yaw
- **Camera** : Low resolution image collection at a rate of 1Hz

The weather balloon has 2 raspberry pi’s working in conjunction. One Pi is dedicated to collecting sensor data and the second pi is for telemetry and stabilization. The two pi’s communicate over a TCP connection.  The sensor pi will run a server and the second pi will run multiple clients requesting data from the sensing pi as needed.

### Prerequisites

Install the following dependencies to run the program (The following was tested on Ubuntu 12.04 and Raspberry Pi running Raspbian: 

```
sudo apt-get install sense-hat
pip install termcolor gps3
```
### Setting up GPS
This project uses the [Adafruit Ultimate GPS Breakout](https://www.adafruit.com/product/746) in conjunction with a USB to TTL cable to communicate over serial due to the Sense hat requiring all of the Raspberry PI's GPIO pins. 

Adafruit has provided the following tutorial to set up the GPS:
https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi/introduction

The [gps3 library](https://pypi.org/project/gps3/) is used for parsing data in real time. 

## Authors

* **Tristan Schuler** - *George Mason University* 
* **Loren Druitt** - *George Mason University* 
* **Ryan Mays** - *George Mason University* 
* **Tan Tran** - *George Mason University* 

## Project History

No History yet
