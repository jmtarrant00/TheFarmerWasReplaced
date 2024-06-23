plot_size = get_world_size()
num_squares = plot_size ** 2 
moveTo([0, 0])
while True:
    for plants in range(3):
        if plants == 0:
            print("Hay")
            get_grass() 
        elif plants == 1:
            print("Wood")
            get_wood()
        elif plants == 2:
            print("Carrots")
            get_carrots(plot_size, num_squares)
        elif plants == 3:
            print("Pumpkins")
            harvest_everything()
            get_pumpkins(plot_size, num_squares)