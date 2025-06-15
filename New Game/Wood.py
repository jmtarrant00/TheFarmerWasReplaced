def wood():

    for i in range(get_world_size()):
        x = get_pos_x()
        y = get_pos_y()

        if y % 2 == 0 and x % 2 == 0 and can_harvest():
            harvest()
            plant(Entities.Tree)
        elif y % 2 != 0 and x % 2 != 0 and can_harvest():
            harvest()
            plant(Entities.Tree)
        else:
            if can_harvest(): 
                harvest()
                plant(Entities.Bush)
        
        
        move(North)
    move(East)