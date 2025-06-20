from Utils import *
from Carrots import carrots

def pumpkins(world_size):

    while num_items(Items.Carrot) < (7 * (world_size ** 2)):
        carrots(world_size)

    for i in range(2):
        replant_list = []
        
        for x in range(world_size):
            for y in range(world_size):

                if get_ground_type() != Grounds.Soil:
                    till()

                if i == 0 and can_harvest():
                    harvest_process(Entities.Pumpkin)

                elif i == 1 and can_harvest():
                    pass

                else:
                    plant(Entities.Pumpkin)
                    replant_list.append([x, y])

                if get_water() < 0.5:
                    water()
                
                move(North)
            move(East)

    quick_print(replant_list)

    while len(replant_list) > 0:
        quick_print(replant_list)
        for tile in replant_list:
            quick_print("Moving to: ", tile)
            moveTo(tile)

            if can_harvest():
                replant_list.remove(tile)
                continue
            else:
                plant(Entities.Pumpkin)
    
    harvest()
    moveTo([0,0])


#pumpkins(get_world_size())