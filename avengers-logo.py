import turtle
import math
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Avengers Logo")
turtle.colormode(255)

# Main turtle for logo
logo = turtle.Turtle()
logo.speed(0)
logo.pensize(5)
logo.hideturtle()

# Gradient turtle
shine = turtle.Turtle()
shine.speed(0)
shine.hideturtle()
shine.pensize(1)

# Text turtle
text = turtle.Turtle()
text.hideturtle()
text.color("white")

def move(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_circle():
    logo.color((200, 200, 200))
    move(logo, 0, -200)
    logo.circle(200)

def draw_A():
    logo.fillcolor((245, 245, 245))
    move(logo, -30, -70)
    logo.setheading(0)
    logo.begin_fill()
    logo.forward(60)
    logo.left(120)
    logo.forward(180)
    logo.left(120)
    logo.forward(60)
    logo.left(120)
    logo.forward(55)
    logo.end_fill()

    # Crossbar
    move(logo, 0, 20)
    logo.setheading(90)
    logo.forward(70)

def draw_slash():
    logo.color((220, 220, 220))
    move(logo, -90, 140)
    logo.setheading(-60)
    logo.forward(320)

def gradient_fill_circle():
    for i in range(200, 0, -4):
        shine.color((255 - i, 255 - i, 255 - i))
        move(shine, 0, -i)
        shine.begin_fill()
        shine.circle(i)
        shine.end_fill()

def shine_effect():
    shine.color("white")
    for angle in range(-120, 60, 2):
        shine.clear()
        move(shine, -100, 0)
        shine.setheading(angle)
        shine.forward(300)
        shine.backward(600)
        screen.update()
        time.sleep(0.01)
    shine.clear()

def draw_text():
    move(text, -105, -250)
    text.color("white")
    text.write("A V E N G E R S", font=("Courier", 24, "bold"))

# Draw the full logo with effects
screen.tracer(0)  # Turn off animation
gradient_fill_circle()
draw_circle()
draw_A()
draw_slash()
draw_text()
screen.tracer(1)  # Turn back on

# Shine sweep
shine_effect()

# Hold screen
turtle.done()
