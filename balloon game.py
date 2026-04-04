import turtle
import random
import time

sc = turtle.Screen()
sc.bgcolor("light blue")
#sc.setup(w, h)
sc.setup(800, 400)
sc.tracer(0) #tracer(0) to turn off screen animation

#player
p = turtle.Turtle()
p.shape("triangle")
p.color("red")

p.penup()
p.goto(0, 400)
p.setheading(90)

#score
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup
score_display.goto(-800, 400)
score_display.color("black")
score_display.write(f"score = {score} ", align = "left", 
                    font = ("Arial", 20, "bold"))

#create balloons
balloons = [] 

#game variables
game_speed = 0.02
difficulty_increase = 0.001
spawn_interval = 2
last_spawn_time = time.time()
running = True

#functions
def move_left():
    x = p.xcor() -50
    if x > -390:
        p.setx(x)

def move_right():
    x = p.xcor() +50
    if x > 390:
        p.setx(x)

sc.listen()
sc.onkey(move_left, "Left")
sc.onkey(move_right, "Right")

turtle.done()
