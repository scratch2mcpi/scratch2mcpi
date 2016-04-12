#!/bin/sh
sudo ps aux | grep 'scratch2mcpi_2.py' | grep -v grep | awk '{print $2}' | xargs sudo kill -9
NU_SCRATCH=`ls /usr/share/scratch/NuScratch*.image`
SQUEAK_STACK=`ls /usr/bin/squeak-stack`
MCPI_TEMPLATE="/home/pi/Documents/Scratch Projects/mcpi_template.sb"
if [ $NU_SCRATCH ] -a [ $SQUEAK_STACK ]
then
  /usr/bin/squeak-stack -vm-sound-alsa $NU_SCRATCH --document "$MCPI_TEMPLATE" & sleep 60
else
  scratch --document "$MCPI_TEMPLATE" & sleep 30
fi
lxterminal -t Scratch2MCPI -e python /home/pi/scratch2mcpi/scratch2mcpi_2.py
