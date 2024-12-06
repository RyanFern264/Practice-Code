
from turtle import Turtle, Screen, colormode
from random import random, choice, randint, uniform
import colorgram

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkOliveGreen")
timmy.speed("fastest")
colormode(255)

def draw_shapes(num_sides):
    for i in range(3, num_sides):
        color_code = ((randint(0, 255)), (randint(0, 255)), (randint(0, 255)))
        timmy.pencolor(color_code)
        for j in range(1, i+1):
            timmy.forward(30)
            timmy.right(360/i)

def rand_walk(steps):
    timmy.width(10)
    for _ in range(0, steps):
        turn_degree = 90*randint(0, 4)
        timmy.setheading(turn_degree)
        timmy.forward(20)
        color_code = ((randint(0, 255)), (randint(0, 255)), (randint(0, 255)))
        timmy.pencolor(color_code)

def spirograph(degree):
    turn = 360/degree
    for i in range(1, degree+1):
        color_code = ((randint(0, 255)), (randint(0, 255)), (randint(0, 255)))
        timmy.pencolor(color_code)
        timmy.circle(100)
        timmy.right(turn)

spirograph(50)










screen = Screen()
screen.exitonclick()