from Utility_Functions import *
from Carrots import get_carrots

def get_sunflower(plot_size, num_squares):
    largest_sunflower = {}
    needs_till = False
    num_sunflower_seeds = num_items(Items.Sunflower_Seed)
    if num_sunflower_seeds < num_squares:
        sunflower_seeds_needed = num_squares - num_sunflower_seeds

        if sunflower_seeds_needed > num_items(Items.Carrot):
            get_carrots(plot_size, num_squares)

        trade(Items.Sunflower_Seed, sunflower_seeds_needed)

    for i in range(2):
        for x in range(plot_size):
            for y in range(plot_size):
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
                else:
                    harvest_process(Entities.Sunflower)
                move(North)
            move(East)

    while len(largest_sunflower) > 0:
        largest_key = max(largest_sunflower)
        quick_print("Harvesting Sunflowers with ", largest_key, "petals.")
        for coord in largest_sunflower[largest_key]:
            moveTo(coord)
            harvest()
        largest_sunflower.pop(largest_key)
    
    moveTo([0, 0])



get_sunflower(get_world_size(), get_world_size() ** 2)