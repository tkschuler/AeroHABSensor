#!/bin/sh
sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
echo "we're in" 

python servermulti.py
