from Utility_Functions import moveTo


moveTo([0,0])
trade(Items.Fertilizer, 50)

opp_dirs = {
    North:South,
    South:North,
    East:West,
    West:East
}

while True:
    plant(Entities.Bush)
    while get_entity_type() != Entities.Hedge:
        use_item(Items.Fertilizer)
        if get_entity_type() == Entities.Hedge:
            break
    
    available_directions = []
    branches = {}
    directions = [North, East, South, West]
    while get_entity_type() != Entities.Treasure:
        x_pos = get_pos_x()
        y_pos = get_pos_y()
        quick_print("X:", x_pos)
        quick_print("Y:", y_pos)
        available_directions = []
        for direction in directions:
            quick_print("Testing", direction)
            if move(direction):
                
                move(opp_dirs[direction])
                available_directions.append(direction)

        if len(available_directions) > 1:
            branches[(x_pos, y_pos)] = available_directions

        move(available_directions[0])
        
        quick_print(branches)
                     