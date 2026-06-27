import pgzrun
import random


def draw():
    rad = 30
    
    r = 255
    g = 0
    b = random.randint(0, 255)
    for i in range(25):
        screen.draw.circle((150, 250), 30, (r, g, b))
        r = r - 10
        g = g + 10

    rad = rad + 10


    


    

pgzrun.go()
