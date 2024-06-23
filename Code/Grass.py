def get_grass():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_ground_type() != Grounds.Turf:
                harvest()
                till()
            elif can_harvest():
                harvest()
            move(North)
        move(East)
        
get_grass()