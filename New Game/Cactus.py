from Utils import *
from Pumpkins import pumpkins

def Cactus(world_size):

    while num_items(Items.Pumpkin) < (2 * (world_size ** 2)):
        pumpkins(world_size)

    for x in range(world_size):
        for y in range(world_size):
            
            if get_ground_type() != Grounds.Soil:
                till()

            if can_harvest():
                harvest_process(Entities.Cactus)

            else:
                harvest_process(Entities.Cactus)

            move(North)
        move(East)

    sizes = []
    for y in range(world_size):
        sizes.append(measure())
        move(North)

    quick_print(sizes)
    #     current_size = measure()
    #     # quick_print("Size at ", get_pos_x(), ", ", get_pos_y(), ": ", current_size)
    #     move(North)
    #     comp_size = measure()
    #     # quick_print("Size at ", get_pos_x(), ", ", get_pos_y(), ": ", comp_size)

    #     quick_print("Current Size: ", current_size)
    #     quick_print("Comp Size: ", comp_size)

    #     if comp_size < current_size:
    #         swap(South)

    # for y in range(world_size):
    #     quick_print(measure())
    #     move(South)
    

    # moveTo([0, 0])


while True:
    Cactus(get_world_size())