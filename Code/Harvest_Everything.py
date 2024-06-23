def harvest_everything():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            harvest()
            move(North)
        move(East)
    moveTo([0,0])
    return

harvest_everything()