#!/usr/bin/env python
import os
import glob

MCPI_TEMPLATE = "/home/pi/Documents/Scratch Projects/mcpi_template.sb"
NU_SCRATCH = "/usr/share/scratch/NuScratch*.image"
SQUEAK_STACK = "/usr/bin/squeak-stack"

def raspi_revision():
  revision = "0000"
  try:
    f = open('/proc/cpuinfo', 'r')
    for line in f:
      if line[0:8] == 'Revision':
        length = len(line)
        revision = line[11:length - 1]
    f.close()
  except:
    revision = "0000"
  return revision

def lower_than_raspi3():
  REVISIONS = ["0002", "0003", "0004", "0005", "0006", "0007", "0008", "0009",
               "000d", "000e", "000f", "0010", "0011", "0012", "a01041", "a21041", "900092"]
  RAPI3_REVISIONS = ["a02082", "a22082"]
  return raspi_revision() in REVISIONS

if glob.glob(NU_SCRATCH) and glob.glob(SQUEAK_STACK):
  os.system("%s -vm-sound-alsa %s --document %s & sleep 60" % (SQUEAK_STACK, NU_SCRATCH, MCPI_TEMPLATE))
else:
  sleep = 10
  if lower_than_raspi3():
     sleep = 30
  os.system("scratch --document \"%s\" & sleep %d" % (MCPI_TEMPLATE, sleep))

os.system("lxterminal -t Scratch2MCPI -e python /home/pi/scratch2mcpi/scratch2mcpi.py")
