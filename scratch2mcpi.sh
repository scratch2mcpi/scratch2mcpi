#!/bin/sh
/home/pi/mcpi/minecraft-pi &
ps aux | grep 'python.*scratch2mcpi.py' | grep -v grep | awk '{print $2}' | xargs sudo kill -9 
scratch --document "/home/pi/Documents/Scratch Projects/hello_minecraft.sb" &
sleep 20
python /home/pi/scratch2mcpi/scratch2mcpi.py &
