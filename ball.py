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

    def move(self, move=1):
        self.forward(move)

    def bounce_y(self, changer=0):
        self.setheading(360 - self.heading() + changer)

    def bounce_x(self, changer=0):
        self.setheading(180 - self.heading() + changer)

    def set_ball(self):
        self.setposition(0, -360)
        self.setheading(random.randint(70, 110))

    def set_mouse_ball(self, event):
        ball_x = -301 + event.x
        ball_y = 400 - event.y
        self.setx(ball_x)
        self.sety(ball_y)
