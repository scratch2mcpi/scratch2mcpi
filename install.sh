#!/bin/sh
wget -P /tmp https://github.com/champierre/scratch2minecraft/archive/master.zip
unzip /tmp/master.zip
mv scratch2minecraft-master scratch2minecraft
rm /tmp/master.zip
echo -n "Please specify Minecraft Pi installation directory[/home/pi/mcpi]: "
read dir 
case $dir in
  /*)
    cp -r $dir/api/python/mcpi scratch2minecraft/;;
  *)
    cp -r /home/pi/mcpi/api/python/mcpi scratch2minecraft/;;
esac
echo "Installation of scratch2minecraft is completed."

