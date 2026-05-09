import turtle
import time

sc = turtle.Screen()
sc.setup(600, 600)
sc.bgcolor("Black")
sc.title("Brick Breaker")

#paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid = 1, stretch_len = 5)

paddle.penup()
paddle.goto(0, -250)
paddle_width = 100

#ball
ball = turtle.Turtle()
ball.color("red")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

#bricks
bricks = []
colors = ["blue", "green", "yellow"]
for row in range(3):
    for column in range(-240, 241, 80):


sc.mainloop()
