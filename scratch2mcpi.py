#!/usr/bin/env python
import sys
import os
import gettext
import scratch
import mcpi.minecraft as minecraft

localedir = os.path.join(os.path.dirname(__file__), 'locale')
_ = gettext.translation(domain = 'main', localedir = localedir, fallback = True).ugettext

#try:
#  mc = minecraft.Minecraft.create()
#except:
#  print _("Error: Unable to connect to Minecraft. Minecraft may be not running.")
#  sys.exit()
 
try:
  s = scratch.Scratch()
except scratch.ScratchError:
  print _("Error: Unable to connect to Scratch. Scratch may be not running or the remote sensor connections may be not enabled.") 
  sys.exit()

print _("Connected to Scratch")
mcpiX = 0
mcpiY = 0
mcpiZ = 0
blockTypeId = 1
blockData = 0

s.broadcast("hello_minecraft")
s.broadcast("setPos")
s.broadcast("setBlock")
s.broadcast("getPos")

def listen():
  while True:
    try:
      yield s.receive()
    except scratch.ScratchError:
      raise StopIteration

for msg in listen():
  print "Received: %s" % str(msg)
  if msg[0] == 'broadcast':
    if msg[1] == 'hello_minecraft':
      mc = minecraft.Minecraft.create()
      mc.postToChat("hello minecraft")
    elif msg[1] == 'setPos':
      mc = minecraft.Minecraft.create()
      mc.player.setPos(mcpiX, mcpiY, mcpiZ)
      print "setPos: %d %d %d" % (mcpiX, mcpiY, mcpiZ)
    elif msg[1] == 'setBlock':
      mc = minecraft.Minecraft.create()
      mc.setBlock(mcpiX, mcpiY, mcpiZ, blockTypeId, blockData)
      print "setBlock: %d %d %d %d %d" % (mcpiX, mcpiY, mcpiZ, blockTypeId, blockData)
    elif msg[1] == 'getPos':
      mc = minecraft.Minecraft.create()
      playerPos = mc.player.getPos()
      s.sensorupdate({'playerX': playerPos.x, 'playerY': playerPos.y, 'playerZ': playerPos.z})
  elif msg[0] == 'sensor-update':
    mcpiX = msg[1].get('mcpiX', mcpiX)
    mcpiY = msg[1].get('mcpiY', mcpiY)
    mcpiZ = msg[1].get('mcpiZ', mcpiZ)
    blockTypeId = msg[1].get('blockTypeId', blockTypeId)
    blockData = msg[1].get('blockData', blockData)
    print "mcpiX:%d, mcpiY:%d, mcpiZ:%d, blockTypeId:%d, blockData:%d" % (mcpiX, mcpiY, mcpiZ, blockTypeId, blockData)

