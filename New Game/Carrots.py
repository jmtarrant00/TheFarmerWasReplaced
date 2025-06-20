from Utils import * 
from Wood import wood
from Grass import grass

# Harvests, tills, plants, and waters carrots across the world as needed.
def carrots(world_size): 

    while num_items(Items.Wood) < (11 * (world_size ** 2)) or num_items(Items.Hay) < (11 * (world_size ** 2)):
        wood(world_size)
        grass(world_size)
        

    for y in range(world_size):
        for x in range(world_size):

            # If ready to harvest and soil is correct, harvest and replant
            if can_harvest() and get_ground_type() == Grounds.Soil:
                harvest()
                plant(Entities.Carrot)

            # If ready to harvest but soil is wrong, harvest, till, and replant
            elif can_harvest() and get_ground_type() != Grounds.Soil:
                harvest()
                till()
                plant(Entities.Carrot)

            # If not ready to harvest and soil is wrong, just till and plant
            elif get_ground_type() != Grounds.Soil:
                till()
                plant(Entities.Carrot)
            
            else:
                return


            # Water if soil is too dry
            if get_water() < 0.5:
                while get_water() != 1:
                    use_item(Items.Water)   

            move(North)
        move(East)


#carrots(get_world_size())