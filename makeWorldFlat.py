#http://www.minecraftforum.net/forums/other-platforms/minecraft-pi-edition/1959866-simple-flatmap-script
import sys
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
mc.setBlocks(-128,0,-128,128,64,128,0)
if(len(sys.argv) > 1):
        bid = int(sys.argv[1])
else:
        bid = block.SNOW_BLOCK.id

if bid < 0 or bid > 108:
        bid = block.SNOW_BLOCK.id

mc.setBlocks(-128,0,-128,128,-64,128,bid)

