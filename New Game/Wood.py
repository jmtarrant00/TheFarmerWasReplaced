def wood(world_size):  

    for y in range(world_size):
        for x in range(world_size):
            x_pos = get_pos_x()
            y_pos = get_pos_y()

            if y_pos % 2 == 0 and x_pos % 2 == 0 and can_harvest():
                harvest()
                plant(Entities.Tree)
            elif y_pos % 2 != 0 and x_pos % 2 != 0 and can_harvest():
                harvest()
                plant(Entities.Tree)
            elif can_harvest(): 
                harvest()
                plant(Entities.Bush)
                        
            
            move(North)
        move(East)
        
        
#wood(get_world_size())