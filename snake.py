from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE_FD = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for cord in POSITIONS:
            self.add_segment(cord)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            nx = self.segments[i - 1].xcor()
            ny = self.segments[i - 1].ycor()
            self.segments[i].goto(nx, ny)
        self.segments[0].fd(DISTANCE_FD)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def add_segment(self, cord):
        new_seg = Turtle('square')
        new_seg.up()
        new_seg.color('White')
        new_seg.goto(cord)
        self.segments.append(new_seg)

    def extend(self):
        # add segment
        self.add_segment(self.segments[-1].position())
