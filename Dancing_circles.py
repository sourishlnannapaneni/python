import turtle
import random
import time

t = turtle.Turtle()
t.speed(100)
sc = turtle.Screen()
sc.bgcolor("black")

def draw_circle():
    t.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.goto(x, y)
    
    #choosing a random color for the circle
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    sc.colormode(255)
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)

    #Draw the circle
    t.begin_fill()
    t.pendown()
    t.circle(random.randint(30, 90))
    t.penup()
    t.end_fill()

    t.hideturtle()

delay = 0.9
start_time = time.time()
for i in range(63):
    draw_circle()
    time.sleep(delay)
    t.clear()
    delay = max(0.01, delay - 0.05)
end_time = time.time()

elapsed_time = end_time - start_time
t.penup()
t.goto(0, 0)
t.color("white")
t.write(f"total animation time = {elapsed_time} seconds",
         align = "center", font = ("Arial", 20, "bold"))
time.sleep(5)
print(f"Total animation time = {elapsed_time} seconds")
turtle.done()
