# card2csv.py  21/06/2015  D.J.Whale
#
# (c) 2015 D.J.Whale
#
# Read a card and write it to a csv file compatible with the maze builder
# program in Adventures in Minecraft.

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import sys
from math import cos, sin, radians, floor
# Use this to force test harness that returns a test card every second
#from cardreader import tester as cardreader

# Use this to force using the arduino card reader
#from cardreader import arduino as cardreader

# Use this to use whatever cardreader/__init__.py sets as default
import cardreader

GAP = block.AIR.id
WALL = block.STONE.id
DEPTH = 4
try:
    mc = minecraft.Minecraft.create()
except :
    print "Minecraft connection error:", sys.exc_info()[0]
    sys.exit()

def printCard(card):
  for row in card:
    print(row)

def sign(n):
    return 1 if n > 0 else -1

def buildBlocks(card):
    playerPos = mc.player.getTilePos()
    angle = radians(mc.player.getRotation()) #the X is -90 degrees facing axis Z
    px = playerPos.x
    py = playerPos.y
    pz = playerPos.z
    mc.player.setPos(px,py + DEPTH, pz)
    for i, row in enumerate(card):
        for j, col in enumerate(row):
            if col == 'X':
                blockType = WALL
            else:
                blockType = GAP
            for c in range(DEPTH):
                mc.setBlock(px + j - 4, py + c, pz + i - 4, blockType)
        if i >= 7:
            break # ignore mirror test data at end of card buffer

try:
    print "Start\n"
    while True:
        time.sleep(1)
        if cardreader.isReady():
            card = cardreader.read()
            printCard(card)
            buildBlocks(card)

except KeyboardInterrupt:
      print "End\n"
      sys.exit()

# END
