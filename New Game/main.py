# Import the needed functions for harvesting and running the drone
from Grass import grass
from Wood import wood
from Carrots import carrots
from Pumpkins import pumpkins
from Sunflowers import sunflowers

world_size = get_world_size()

while True:
    grass(world_size)
    wood(world_size)
    carrots(world_size)
    pumpkins(world_size)
    sunflowers(world_size)
    

