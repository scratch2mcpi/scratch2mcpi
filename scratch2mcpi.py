#!/usr/bin/env python

import sys
import os
import gettext
import scratch
import mcpi.minecraft as minecraft
import mcturtle.minecraftturtle as turtle
import mcstuff.minecraftstuff as stuff
import mcpi.block as block
import time

VERSION = "2.0.2"
localedir = os.path.join(os.path.dirname(__file__), 'locale')
_ = gettext.translation(domain = 'scratch2mcpi', localedir = localedir, fallback = True).ugettext

def is_number(value):
    if (isinstance(value, (int, float))):
        return True
    else:
        return False

def connect():
    try:
        return scratch.Scratch()
    except scratch.ScratchError:
        print _("Error: Unable to connect to Scratch. Scratch may be not running or the remote sensor connections may be not enabled.")
        return None

def _listen(s):
    while True:
        try:
            yield s.receive()
        except scratch.ScratchError:
            print _("Error: Disconnected from Scratch.")
            raise StopIteration

def listen(s, mc):
    mcpiX = 0
    mcpiY = 0
    mcpiZ = 0
    mcpiX0 = 0
    mcpiY0 = 0
    mcpiZ0 = 0
    mcpiX1 = 0
    mcpiY1 = 0
    mcpiZ1 = 0
    blockTypeId = 1
    blockData = 0

    # Minecraft Graphics Turtle
    speed = 10
    steps = 0
    degrees = 0

    mc = minecraft.Minecraft.create()
    pos = mc.player.getPos()
    steve = turtle.MinecraftTurtle(mc, pos)

    # Minecraft Stuff
    radius = 0
    shapePoints = []
    fill = True
    mcDrawing = stuff.MinecraftDrawing(mc)

    for msg in _listen(s):
        if (msg):
            print "Received: %s" % str(msg)
            if msg[0] == 'broadcast':
                if not mc:
                    mc = minecraft.Minecraft.create()
                if msg[1] == 'hello_minecraft':
                    mc.postToChat("hello minecraft")
                elif msg[1] == 'setPos':
                    if (is_number(mcpiX) and is_number(mcpiY) and is_number(mcpiZ)):
                        mc.player.setPos(mcpiX, mcpiY, mcpiZ)
                        print "setPos: %.1f %.1f %.1f" % (mcpiX, mcpiY, mcpiZ)
                elif msg[1] == 'setBlock':
                    if (is_number(mcpiX) and is_number(mcpiY) and is_number(mcpiZ) and is_number(blockTypeId) and is_number(blockData)):
                        mc.setBlock(mcpiX, mcpiY, mcpiZ, blockTypeId, blockData)
                        print "setBlock: %d %d %d %d %d" % (mcpiX, mcpiY, mcpiZ, blockTypeId, blockData)
                # Minecraft Graphics Turtle(Start)
                elif msg[1] == 'turtle:setPos':
                    if is_number(mcpiX) and is_number(mcpiY) and is_number(mcpiZ):
                        steve.setposition(mcpiX, mcpiY, mcpiZ)
                        print "turtle:setPos: %.1f %.1f %.1f" % (mcpiX, mcpiY, mcpiZ)
                elif msg[1] == 'turtle:forward':
                    if is_number(steps):
                        steve.forward(steps)
                        print "steve.forward: (%d)" % (steps)
                elif msg[1] == 'turtle:backward':
                    if is_number(steps):
                        steve.backward(steps)
                        print "steve.backward: (%d)" % (steps)
                elif msg[1] == 'turtle:right':
                    if is_number(degrees):
                        steve.right(degrees)
                        print "steve.right: (%d)" % (degrees)
                elif msg[1] == 'turtle:left':
                    if is_number(degrees):
                        steve.left(degrees)
                        print "steve.left: (%d)" % (degrees)
                elif msg[1] == 'turtle:up':
                    if is_number(degrees):
                        steve.up(degrees)
                        print "steve.up: (%d)" % (degrees)
                elif msg[1] == 'turtle:down':
                    if is_number(degrees):
                        steve.down(degrees)
                        print "steve.down: (%d)" % (degrees)
                elif msg[1] == 'turtle:penup':
                    steve.penup()
                    print "steve.penup"
                elif msg[1] == 'turtle:pendown':
                    steve.pendown()
                    print "steve.pendown"
                elif msg[1] == 'turtle:setheading':
                    if is_number(degrees):
                        steve.setheading(degrees)
                        print "steve.setheading: (%d)" % (degrees)
                elif msg[1] == 'turtle:setverticalheading':
                    if is_number(degrees):
                        steve.setverticalheading(degrees)
                        print "steve.setverticalheading: (%d)" % (degrees)
                # Minecraft Graphics Turtle(End)
                # Minecraft Stuff(Start)
                elif msg[1] == 'stuff:drawLine':
                    mcDrawing.drawLine(int(mcpiX1), int(mcpiY1), int(mcpiZ1), int(mcpiX), int(mcpiY), int(mcpiZ), blockTypeId, blockData)
                    print "mcDrawing.drawLine: (%d, %d, %d, %d, %d, %d, %d, %d)" % (mcpiX1, mcpiY1, mcpiZ1, mcpiX, mcpiY, mcpiZ, blockTypeId, blockData)
                elif msg[1] == 'stuff:drawSphere':
                    mcDrawing.drawSphere(mcpiX, mcpiY, mcpiZ, radius, blockTypeId, blockData)
                    print "mcDrawing.drawSphere: (%d, %d, %d, %d, %d, %d)" % (mcpiX, mcpiY, mcpiZ, radius, blockTypeId, blockData)
                elif msg[1] == 'stuff:drawCircle':
                    mcDrawing.drawCircle(mcpiX, mcpiY, mcpiZ, radius, blockTypeId, blockData)
                    print "mcDrawing.drawCircle: (%d, %d, %d, %d, %d, %d)" % (mcpiX, mcpiY, mcpiZ, radius, blockTypeId, blockData)
                elif msg[1] == 'stuff:resetShapePoints':
                    shapePoints = []
                    mcDrawing = stuff.MinecraftDrawing(mc)
                elif msg[1] == 'stuff:setShapePoints':
                    shapePoints.append(minecraft.Vec3(int(mcpiX), int(mcpiY), int(mcpiZ)))
                    print "append.shapePoints:"
                    print ' '.join(str(p) for p in shapePoints)
                elif msg[1] == 'stuff:drawFace':
                    if (fill == 'True'):
                        fillFlag = True
                    elif (fill == 'False'):
                        fillFlag = False
                    mcDrawing.drawFace(shapePoints, fillFlag, blockTypeId)
                    print "mcDrawing.drawFace:"
                    print ' '.join(str(p) for p in shapePoints)
                    print(fill)
                    print(blockTypeId)
                # Minecraft Stuff(End)

                elif msg[1] == 'setBlocks':
                    if (is_number(mcpiX0) and is_number(mcpiY0) and is_number(mcpiZ0) and is_number(mcpiX1) and is_number(mcpiY1) and is_number(mcpiZ1) and is_number(blockTypeId) and is_number(blockData)):
                        mc.setBlocks(mcpiX0, mcpiY0, mcpiZ0, mcpiX1, mcpiY1, mcpiZ1, blockTypeId, blockData)
                        print "setBlocks(%d, %d, %d, %d, %d, %d, %d, %d" % (mcpiX0, mcpiY0, mcpiZ0, mcpiX1, mcpiY1, mcpiZ1, blockTypeId, blockData)
                elif msg[1] == 'getPos':
                    playerPos = mc.player.getPos()
                    pos = playerPos
                    s.sensorupdate({
                        'playerX': playerPos.x,
                        'playerY': playerPos.y,
                        'playerZ': playerPos.z
                    })
                elif msg[1] == 'getHeight':
                    posY = mc.getHeight(mcpiX, mcpiZ)
                    s.sensorupdate({'posY': posY})
                    mc.postToChat("posY: %d" % posY)
                elif msg[1] == 'getBlock':
                    blockFound = mc.getBlockWithData(mcpiX, mcpiY, mcpiZ)
                    s.sensorupdate({
                        'blockTypeId': blockFound.id,
                        'blockData': blockFound.data
                    })
                elif msg[1] == 'pollBlockHits':
                    blockEvents = mc.events.pollBlockHits()
                    print blockEvents
                    if blockEvents:
                        blockEvent = blockEvents[-1]
                        s.sensorupdate({
                            'blockEventX': blockEvent.pos.x,
                            'blockEventY': blockEvent.pos.y,
                            'blockEventZ': blockEvent.pos.z,
                            'blockEventFace': blockEvent.face,
                            'blockEventEntityId': blockEvent.entityId
                        })
                    else:
                        s.sensorupdate({
                            'blockEventX': '',
                            'blockEventY': '',
                            'blockEventZ': '',
                            'blockEventFace': '',
                            'blockEventEntityId': ''
                        })
                elif msg[1] == 'reset':
                    mc.postToChat('reset the world')
                    mc.setBlocks(-100, 0, -100, 100, 63, 100, 0, 0)
                    mc.setBlocks(-100, -63, -100, 100, -2, 100, 1, 0)
                    mc.setBlocks(-100, -1, -100, 100, -1, 100, 2, 0)
                    mc.player.setPos(0, 0, 0)
                elif msg[1] == 'echo' or msg[1].startswith('echo '):
                    words = msg[1].split()
                    mc.postToChat(" ".join(words[1:]))
            elif msg[0] == 'sensor-update':
                mcpiX = msg[1].get('mcpiX', mcpiX)
                mcpiY = msg[1].get('mcpiY', mcpiY)
                mcpiZ = msg[1].get('mcpiZ', mcpiZ)
                mcpiX0 = msg[1].get('mcpiX0', mcpiX0)
                mcpiY0 = msg[1].get('mcpiY0', mcpiY0)
                mcpiZ0 = msg[1].get('mcpiZ0', mcpiZ0)
                mcpiX1 = msg[1].get('mcpiX1', mcpiX1)
                mcpiY1 = msg[1].get('mcpiY1', mcpiY1)
                mcpiZ1 = msg[1].get('mcpiZ1', mcpiZ1)
                blockTypeId = msg[1].get('blockTypeId', blockTypeId)
                blockData = msg[1].get('blockData', blockData)

                # Minecraft Graphics Turtle
                speed = msg[1].get('speed', speed)
                steps = msg[1].get('steps', steps)
                degrees = msg[1].get('degrees', degrees)
                steve.speed(speed)
                steve.penblock(blockTypeId, blockData)

                # Minecraft Stuff
                radius = msg[1].get('radius', radius)
                fill = msg[1].get('fill', fill)

def main():
    print "================="
    print "Sratch2MCPI %s" % VERSION
    print "================="
    print ""

    while True:
        s = connect()
        mc = minecraft.Minecraft.create()

        if (s):
            mc.postToChat("Scratch2MCPI connected to Minecraft Pi.")
            print _("Connected to Scratch")

            s.broadcast("hello_minecraft")
            s.broadcast("setPos")
            s.broadcast("setBlock")
            # s.broadcast("setBlocks")
            s.broadcast("getPos")
            s.broadcast("getHeight")
            s.broadcast("getBlock")
            s.broadcast("pollBlockHits")
            s.broadcast("reset")

            s.broadcast("turtle:forward")
            s.broadcast("turtle:backward")
            s.broadcast("turtle:right")
            s.broadcast("turtle:left")
            s.broadcast("turtle:up")
            s.broadcast("turtle:down")
            s.broadcast("turtle:setPos")
            s.broadcast("turtle:penup")
            s.broadcast("turtle:pendown")
            s.broadcast("turtle:setheading")
            s.broadcast("turtle:setverticalheading")

            s.broadcast("stuff:drawSphere")
            s.broadcast("stuff:drawCircle")
            s.broadcast("stuff:drawLine")
            s.broadcast("stuff:drawFace")
            s.broadcast("stuff:resetShapePoints")
            s.broadcast("stuff:setShapePoints")

            s.sensorupdate({
                'blockTypeId': 0,
                'blockData': 0
            })

            listen(s, mc)
            time.sleep(5)

main()
