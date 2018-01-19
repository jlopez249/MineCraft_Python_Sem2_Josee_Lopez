from mcpi.minecraft import Minecraft
mc = Minecraft.create()



height = 5
width1 = 6
length1 = 6
width2 = 4
length2 = 4

def growTree(x, y, z):
    mc.setBlocks(x + 2, y, z, x + 2, y + 5, z, 17)
    mc.setBlocks(x + 4, y + 5, z - 2, x, y + 5, z + 2, 18)
    mc.setBlocks(x + 3, y + 6, z - 1, x + 1, y + 6, z + 1, 18)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x + 1, y, z)
