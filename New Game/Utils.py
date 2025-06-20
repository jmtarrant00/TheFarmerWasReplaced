def moveTo(coords):
    # Set maximum value for coordinates
    max_value = get_world_size()

    # Reduce the given coord to the max if over the value
    x = min(coords[0], max_value)
    y = min(coords[1], max_value)

    # Get the current position of the drone
    current_x = get_pos_x()
    current_y = get_pos_y()

    # calculate how many squares the drone needs to move
    x_to_move = abs(x - current_x)
    y_to_move = abs(y - current_y)

    # Determine the direction to move the drone based on whether or not 
    #   the desired coord value is greater or less than the current position
    if x < current_x and y >= current_y:
        for x in range(x_to_move):
            move(West)
        for y in range(y_to_move):
            move(North)
    elif y < current_y and x >= current_x:
        for x in range(x_to_move):
            move(East)
        for y in range(y_to_move):
            move(South)
    elif x < current_x and y < current_y:
        for x in range(x_to_move):
            move(West)
        for y in range(y_to_move):
            move(South)
    elif x >= current_x and y >= current_y:
        for x in range(x_to_move):
            move(East)
        for y in range(y_to_move):
            move(North)
    else:
        return
    

def water():
    while get_water() < 1:
        if num_items(Items.Water) > 1:
            use_item(Items.Water)

        else:
            break
    return
    
def harvest_process(plant_type):
    if plant_type == None:
        harvest()
        water()
        return
    
    if can_harvest():
        harvest()
        plant(plant_type)
        water()
        return
    else:
        plant(plant_type)
        water()
        return