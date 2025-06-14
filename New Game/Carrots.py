# Harvests, tills, plants, and waters carrots across the world as needed.
while True: 
    for i in range(get_world_size()):

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


        # Water if soil is too dry
        if get_water() < 0.1:
            while get_water() != 1:
                use_item(Items.Water)   

        move(North)
    move(East)