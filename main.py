# -*- coding: utf-8 -*-

from scratra import *
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
mc_blockTypeId = 1
mc_x = 0.0
mc_y = 0.0
mc_z = 0.0

@start
def whenstart(scratch):
  print "start"

@broadcast('hi')
def hi(scratch):
  mc.postToChat("hi minecraft")

@update('x')
def update_x(scratch, value):
  global mc_x
  mc_x = value

@update('y')
def update_y(scratch, value):
  global mc_y
  mc_y = value

@update('z')
def update_z(scratch, value):
  global mc_z
  mc_z = value

@update('b')
def update_blockTypeId(scratch, value):
  global mc_blockTypeId
  mc_blockTypeId = value

@broadcast('b')
def setBlock(scratch):
  print u"setBlock: %d %d %d %d" % (mc_x, mc_y, mc_z, mc_blockTypeId)
  mc.setBlock(mc_x, mc_y, mc_z, mc_blockTypeId)

@broadcast('p')
def setPos(scratch):
  print u"setPos: %d %d %d" % (mc_x, mc_y, mc_z)
  mc.player.setPos(mc_x, mc_y, mc_z)

@broadcast('getPos')
def getPos(scratch):
  pos = mc.player.getTilePos()
  mc.postToChat(u"Player Position: %d %d %d" % (pos.x, pos.y, pos.z))

run()