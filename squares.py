import pgzrun
import random

W = 500
H = 500

def draw():
    r = 255
    g = 0
    b = random.randint(0, 255)
    w = W
    h = H
    for i in range(25):
        square = Rect((0, 0), (w, h))
        square.center = (150, 250)
        screen.draw.rect((square), (r, g, b))
        r = r - 10
        g = g + 10

        w = w - 10
        h = h - 10


    

pgzrun.go()
