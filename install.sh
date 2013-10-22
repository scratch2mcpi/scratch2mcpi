#!/bin/sh
sudo apt-get install python-setuptools
sudo easy_install scratchpy
wget -P /tmp https://github.com/champierre/scratch2minecraft/archive/master.zip
unzip /tmp/master.zip
mv scratch2minecraft-master scratch2minecraft
rm /tmp/master.zip
if test -d /home/pi/mcpi/api/python/mcpi; then
  cp -r /home/pi/mcpi/api/python/mcpi scratch2minecraft/
else
  echo "\033[31m\033[1mError: Unable to copy 'mcpi' directory to 'scratch2minecraft'. You should manually copy '[minecraft pi dir]/api/python/mcpi' to 'scratch2minecraft'.\033[00m"
fi
echo "Installation of scratch2minecraft is completed."
