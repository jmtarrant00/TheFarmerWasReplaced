from Utility_Functions import moveTo


moveTo([0,0])
trade(Items.Fertilizer, 50)

opp_dirs = {
    North:South,
    South:North,
    East:West,
    West:East
}
dead_ends = []
available_directions = []
dirs_moved = []
branches = {}
directions = [North, East, South, West]
dir_to_move = []

while True:
    if get_entity_type() != Entities.Hedge or get_entity_type() != Entities.Bush:
        plant(Entities.Bush)
        
    while get_entity_type() != Entities.Hedge:
        use_item(Items.Fertilizer)
        if get_entity_type() == Entities.Hedge:
            break
    
    while get_entity_type() != Entities.Treasure:
        x_pos = get_pos_x()
        y_pos = get_pos_y()
        quick_print("X:", x_pos)
        quick_print("Y:", y_pos)
        available_directions = []

        if (x_pos, y_pos) in branches:
            move(branches[(x_pos, y_pos)][0])
        else:
            for direction in directions:
                if len(dirs_moved) > 0:
                    if opp_dirs[direction] == dirs_moved[-1]:
                        continue
                elif move(direction):
                    move(opp_dirs[direction])
                    available_directions.append(direction)

            if len(available_directions) == 1:
                dir_to_move = available_directions[0]
                quick_print("Moving", dir_to_move)
                move(dir_to_move)
                dirs_moved.append(dir_to_move)
            else:
                branches[(x_pos, y_pos)] = available_directions

                quick_print(branches[(x_pos, y_pos)])
                quick_print("Moving", dir_to_move)
                move(dir_to_move)
                dirs_moved.append(dir_to_move)
                branches[(x_pos, y_pos)].pop(0)
                quick_print(branches[(x_pos, y_pos)])   
        
        
                     