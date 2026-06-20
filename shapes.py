import pgzrun
import random

W = 300
H = 500

def draw():
    r = 255
    g = 0
    b = random.randint(0, 255)
    w = W
    h = H - 50
    for i in range(25):
        rect = Rect((0, 0), (w, h))
        rect.center = (150, 250)
        screen.draw.rect((rect), (r, g, b))
        r = r - 10
        g = g + 10

        w = w - 10
        h = h + 10


    

pgzrun.go()
