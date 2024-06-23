def get_wood():
    for i in range(get_world_size()):
        for j in range(get_world_size() / 2):
            if get_pos_x() % 2 == 0:
                if get_ground_type() != Grounds.Soil:
                    harvest_process(Entities.Grass)
                    till()
                harvest_process(Entities.Tree)
                move(North)
                harvest_process(Entities.Grass)
                harvest_process(Entities.Bush)
                move(North)
            elif get_pos_x() % 2 != 0:
                move(North)
                if get_ground_type() != Grounds.Soil:
                    harvest_process(Entities.Grass)
                    till()
                harvest_process(Entities.Tree)
                move(North)
                harvest_process(Entities.Grass)
                harvest_process(Entities.Bush)
        move(East)
                
while True:
    get_wood()