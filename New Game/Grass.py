while True: 
    for i in range(get_world_size()):
        if can_harvest():
            harvest()
        else: 
            pass
        move(North)
    move(East)