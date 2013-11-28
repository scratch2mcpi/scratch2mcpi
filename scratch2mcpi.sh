#!/bin/sh
sudo ps aux | grep 'scratch2mcpi.py' | grep -v grep | awk '{print $2}' | xargs sudo kill -9
scratch --document "/home/pi/Documents/Scratch Projects/mcpi_template.sb" &
sleep 40
lxterminal -e python /home/pi/scratch2mcpi/scratch2mcpi.py

