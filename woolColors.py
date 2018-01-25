from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def getWoolState(color):
    """ Takes a color as a string and returns the wool block state for that color """
    if color == "pink":
        blockState = 6
    elif color == "red":
        blockState = 14
    elif color == "orange":
        blockState = 1
    elif color == "yellow":
        blockState = 4
    elif color == "green":
        blockState = 13
    elif color == "lime":
        blockstate = 5
    elif color == "blue":
        blockState = 11
    elif color == "light blue":
        blockState = 3
    elif color == "purple":
        blockState = 10
    elif color == "black":
        blockState = 15
    return blockState

colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)
