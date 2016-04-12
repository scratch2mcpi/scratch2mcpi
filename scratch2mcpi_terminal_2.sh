#!/bin/sh
sudo ps aux | grep 'scratch2mcpi_2.py' | grep -v grep | awk '{print $2}' | xargs sudo kill -9
lxterminal -t Scratch2MCPI -e python /home/pi/scratch2mcpi/scratch2mcpi_2.py
