#!/bin/sh
sudo ps aux | grep 'scratch2mcpi.py' | grep -v grep | awk '{print $2}' | xargs sudo kill -9
NU_SCRATCH=`ls /usr/share/scratch/NuScratch*.image`
MCPI_TEMPLATE="/home/pi/Documents/Scratch Projects/mcpi_template.sb"
if [ $NU_SCRATCH ]
then
  /usr/bin/squeak-stack -vm-sound-alsa $NU_SCRATCH --document $MCPI_TEMPLATE & sleep 60
else
  scratch --document $MCPI_TEMPLATE & sleep 30
fi
lxterminal -t Scratch2MCPI -e python /home/pi/scratch2mcpi/scratch2mcpi.py
