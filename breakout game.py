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
        brick = turtle.Turtle()
        brick.shape("square")
        brick.shapesize(stretch_wid = 1, stretch_len = 3)
        brick.color(colors[row])
        brick.penup()
        brick.goto(column, 150 - (row*40))
        bricks.append(brick)

#score
score = 0
deaths = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 200)

def update_score():
    score_display.clear()
    score_display.write(f"SCORE : {score} LIVES: {5 - deaths}", align = "center", font = ("Arial", 25, "bold"))
update_score()

#game start
game_started = False
def start_game(x, y):
    global game_started
    game_started = True

#movement
def move_left():
    x = paddle.xcor()
    if x > -250:
        paddle.setx(x - 60)
def move_right():
    x = paddle.xcor()
    if x < 250:
        paddle.setx(x + 60)

sc.listen()
sc.onkey(move_left, "left")
sc.onkey(move_right, "right")

#game loop
while True:
    sc.update()
    sc.sleep(0.01)
    if not game_started:
        continue
    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #collision with the wall
    if ball.xcor() > 290 or ball.xcor < -290:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1 
    if ball.ycor() < -290:
        death += 1
        ball.goto(0, 0)
        ball.dy *= -1
        game_started = False
        update_score
        
        if deaths == 5:
            score_display.goto(0, 0)
            score_display.write("GAME OVER", align = "center", font = ("Arial", 35, "bold")) 
            break

sc.mainloop()
