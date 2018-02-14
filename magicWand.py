from mcpi.minecraft import Minecraft
mc = Mine.craft.create()

import time

time.sleep(60)

hits = mc.events.pollBlocksHits()
block = 103

for hit in hits:
    
