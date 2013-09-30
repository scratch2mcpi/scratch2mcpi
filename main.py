# -*- coding: utf-8 -*-

from scratra import *
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
mc_blockTypeId = 1
mc_x = mc_y = mc_z = None

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

@update('blockTypeId')
def update_blockTypeId(scratch, value):
  global mc_blockTypeId
  mc_blockTypeId = value

@broadcast('setBlock')
def setBlock(scratch):
  pos = mc.player.getTilePos()
  x = mc_x or pos.x
  y = mc_y or pos.y
  z = mc_z or pos.z
  print u"setBlock: %d %d %d %d" % (x, y, z, mc_blockTypeId)
  mc.setBlock(x, y, z, mc_blockTypeId)

@broadcast('setPos')
def setPos(scratch):
  pos = mc.player.getTilePos()
  x = mc_x or pos.x
  y = mc_y or pos.y
  z = mc_z or pos.z
  print u"setPos: %d %d %d" % (x, y, z)
  mc.player.setPos(x, y, z)

run()