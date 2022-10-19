from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.speed(0)
        self.color('cyan')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.new_food()

    def new_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)


class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-300, -300)
        self.pensize(5)
        self.down()
        self.color('white')
        for i in range(4):
            self.fd(600)
            self.left(90)
        self.hideturtle()
