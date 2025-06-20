def grass(world_size):
    for y in range(world_size):
        for x in range(world_size):
            if get_ground_type() != Grounds.Grassland:
                harvest()
                till()
            if can_harvest():
                harvest()
                
            move(North)
        move(East)
#while True:
#    grass(get_world_size())