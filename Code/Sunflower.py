from Utility_Functions import *
from Carrots import get_carrots

def get_sunflower(plot_size, num_squares):

    num_sunflower_seeds = num_items(Items.Sunflower_Seed)
    if num_sunflower_seeds < num_squares:
        sunflower_seeds_needed = num_squares - num_sunflower_seeds

        if sunflower_seeds_needed > num_items(Items.Carrot_Seed):
            get_carrots(plot_size, num_squares)

        trade(Items.Sunflower_Seed, sunflower_seeds_needed)

    for i in range(2):
        largest_sunflower = {}
        for x in range(plot_size):
            for y in range(plot_size):
                if get_entity_type() != Entities.Sunflower:
                    harvest_process(Entities.Sunflower, False if get_ground_type() == Grounds.Soil else True)
                    largest_sunflower


                # if can_harvest() and get_ground_type() == Grounds.Soil:
                #     current_plant = get_entity_type()
                #     harvest_process(plant_type=None)
                #     plant(Entities.Sunflower)

                # elif can_harvest() and get_ground_type() != Grounds.Soil:
                #     harvest_process(Entities.Sunflower, need_till=True)
                # elif get_ground_type() != Grounds.Soil:
                #     till()
                #     plant(Entities.Sunflower)
                #     water()
                move(North)
            move(East)
