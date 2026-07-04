import pgzrun
import random

TITLE = "Shoot the Alien"
W = 500
H = 500
msg = ' '
alien = Actor("alien")

def draw():
    screen.clear()
    screen.fill(color = (0, 125, 125))
    alien.draw()
    screen.draw.text(msg, center = (250, 25), fontsize = 30, color = ("yellow"))

#change alien position
def place_alien():
    alien.x = random.randint(100, 500)
    alien.y = random.randint(100, 500)
 
def on_mouse_down(pos):
    global msg
    if alien.collidepoint(pos):
        msg = "Good Shot, You hit the Alien"
        place_alien()
    else:
        msg = "Bad Luck, You missed the Alien \n Try again"

place_alien()

pgzrun.go()
