from mcpi.minecraft import Minecraft
mc = Minecraft.create()



def melon():
    mc.setBlock(x, y, z, 103)

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
