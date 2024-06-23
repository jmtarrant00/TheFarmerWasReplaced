moveTo([0,0])
trade(Items.Fertilizer, 50)

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
           for direction in directions:
                if move(direction):
                    available_directions.append(direction)

                # if len(available_directions) > 1:
                     