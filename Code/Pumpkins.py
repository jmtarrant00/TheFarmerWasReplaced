from Utility_Functions import moveTo, water, harvest_process

def get_pumpkins(plot_size, num_squares):
    for i in range(2):
        replant_list = []
        for x in range(plot_size):
                for y in range(plot_size):
                    num_pumpkin_seeds = num_items(Items.Pumpkin_Seed)
                    if get_ground_type() != Grounds.Soil:
                        till()
                    if num_pumpkin_seeds < num_squares:
                        trade(Items.Pumpkin_Seed, num_squares - num_pumpkin_seeds)
                    if can_harvest():
                        move(North)
                    else:
                        plant(Entities.Pumpkin)
                        water()
                        replant_list.append([x, y])
                        move(North)
                move(East)

    quick_print(replant_list)
    
    while len(replant_list) > 0:
        for plot in replant_list:
            quick_print("Moving to ", plot)
            moveTo(plot)
            if num_items(Items.Pumpkin_Seed) == 0:
                trade(Items.Pumpkin_Seed)
            
            if can_harvest():
                replant_list.remove(plot)
                continue
            else:
                plant(Entities.Pumpkin)
                water()

    harvest()
    moveTo([0,0])
 
 
    return

                

get_pumpkins(get_world_size(), get_world_size() ** 2)