from Utility_Functions import moveTo, water, harvest_process
from Grass import get_grass
from Wood import get_wood

def get_carrots(plot_size, num_squares):
    num_carrot_seeds = num_items(Items.Carrot_Seed)
    if num_carrot_seeds < num_squares:
        carrot_seeds_needed = num_squares - num_carrot_seeds
        if carrot_seeds_needed * 10 > num_items(Items.Wood):
            get_wood()
        elif carrot_seeds_needed * 10 > num_items(Items.Hay):
            get_grass()
        
        trade(Items.Carrot_Seed, num_squares - num_carrot_seeds)
    for i in range(plot_size):
        for j in range(plot_size):
            if can_harvest() and get_ground_type() == Grounds.Soil:
                harvest_process(Entities.Carrots)
            elif can_harvest() and get_ground_type() != Grounds.Soil:
                harvest()
                till()
                plant(Entities.Carrots)
                water()
            elif get_ground_type() != Grounds.Soil:
                till()
                plant(Entities.Carrots)
                water()
            move(North)
        move(East)
get_carrots(get_world_size(), get_world_size() ** 2)