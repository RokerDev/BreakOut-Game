import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.shape("circle")
        self.set_ball()
        self.speed(1)
        self.showturtle()

    def move(self):
        self.forward(4)

    def bounce_y(self):
        self.setheading(360 - self.heading() + random.randint(-5, 5))

    def bounce_x(self):
        self.setheading(180 - self.heading() + random.randint(-5, 5))

    def set_ball(self):
        self.setposition(0, -180)
        self.setheading(random.randint(70, 110))
