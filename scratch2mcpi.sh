#!/bin/sh
/home/pi/mcpi/minecraft-pi &
ps aux | grep 'python.*scratch2mcpi.py' | grep -v grep | awk '{print $2}' | xargs sudo kill -9 
scratch --document "/home/pi/Documents/Scratch Projects/mcpi_template.sb" &
sleep 30
python /home/pi/scratch2mcpi/scratch2mcpi.py &
