#!/bin/sh
sudo ps aux | grep 'scratch2mcpi.py' | grep -v grep | awk '{print $2}' | xargs sudo kill -9
lxterminal -t Scratch2MCPI -e python2 $HOME/scratch2mcpi/bullseye/scratch2mcpi.py

