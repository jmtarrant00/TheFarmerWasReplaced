def pumpkins():
    for i in range(get_world_size()):

        if can_harvest() and get_ground_type() == Grounds.Soil:
            harvest()
            plant(Entities.Pumpkin)

        elif can_harvest() and get_ground_type() != Grounds.Soil:
            harvest()
            till()
            plant(Entities.Pumpkin)

        elif get_ground_type() != Grounds.Soil:
            till()
            plant(Entities.Pumpkin)
            
        else:
            plant(Entities.Pumpkin)
            

        if get_water() < 0.5:
            while get_water() != 1:
                use_item(Items.Water)

        
        move(North)
    move(East)