#!/bin/bash

echo '/dev/ttyACM0' > portscan.cache
minecraft-pi &
sleep 30
sudo /usr/bin/python /home/pi/punchcard_reader/card2minecraft.py &
