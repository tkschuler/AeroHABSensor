[![license](https://img.shields.io/badge/license-LGPL%202.1-blue.svg)](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html)
[![license](https://img.shields.io/pypi/pyversions/event-bus-py2.svg)](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html)

## AeroHab Sensing

https://img.shields.io/pypi/pyversions/event-bus-py2.svg

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
pip install termcolor
```

## Authors

* **Tristan Schuler** - *George Mason University* 
* **Loren Druitt** - *George Mason University* 
* **Ryan Mays** - *George Mason University* 
* **Tan Tran** - *George Mason University* 

## Project History

No History yet
