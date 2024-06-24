from Utility_Functions import moveTo
from Grass import get_grass
from Wood import get_wood
from Carrots import get_carrots
from Pumpkins import get_pumpkins
from Sunflower import get_sunflower

plot_size = get_world_size()
num_squares = plot_size ** 2 
crops_list = [
    "Hay", 
    "Wood", 
    "Carrots", 
    "Pumpkins", 
    "Sunflowers"
]

moveTo([0, 0])
while True:
    for crop in crops_list:
        if crop == "Hay":
            print("Hay")
            get_grass() 
        elif crop == "Wood":
            print("Wood")
            get_wood()
        elif crop == "Carrots":
            print("Carrots")
            get_carrots(plot_size, num_squares)
        elif crop == "Pumpkins":
            print("Pumpkins")
            get_pumpkins(plot_size, num_squares)
        elif crop == "Sunflowers":
            print("Sunflowers")
            get_sunflower(plot_size, num_squares)