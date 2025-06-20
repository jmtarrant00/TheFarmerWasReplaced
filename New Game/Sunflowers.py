from Utils import *
from Carrots import carrots

def sunflowers(world_size):

    while num_items(Items.Carrot) < (world_size ** 2):
        carrots(world_size)

    for i in range(2):
        largest_sunflower = {}
        for x in range(world_size):
            for y in range(world_size):
                if get_ground_type() != Grounds.Soil:
                    till()
                
                if i == 0 and can_harvest():
                    harvest_process(Entities.Sunflower)
                
                elif i == 1 and can_harvest():
                    size = measure()
                    if size in largest_sunflower:
                        largest_sunflower[size].append([x, y])
                    else:
                        largest_sunflower[size] = [[x, y]]
                elif i == 1 and not can_harvest():
                    while not can_harvest():
                        do_a_flip()
                    size = measure()
                    if size in largest_sunflower:
                        largest_sunflower[size].append([x, y])
                    else:
                        largest_sunflower[size] = [[x, y]]
                else:
                    harvest_process(Entities.Sunflower)
                move(North)
            move(East)

        while len(largest_sunflower) > 0:
            largest_key = max(largest_sunflower)
            quick_print("Harvesting Sunflowers with ", largest_key, "petals")
            for coord in largest_sunflower[largest_key]:
                moveTo(coord)
                harvest()
            largest_sunflower.pop(largest_key)
    
    moveTo([0, 0])
                
                

while True:
    sunflowers(get_world_size())