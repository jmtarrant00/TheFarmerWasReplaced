def carrots(): 
    for i in range(get_world_size()):
        if can_harvest() and get_ground_type() == Grounds.Soil:
            harvest()
            plant(Entities.Carrot)
        
        elif can_harvest() and get_ground_type() != Grounds.Soil:
            harvest()
            till()
            plant(Entities.Carrot)
        
        elif get_ground_type() != Grounds.Soil:
            till()
            plant(Entities.Carrot)


        if get_water() < 0.5:
            use_item(Items.Water)
        move(North)
    move(East)