from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.shape("circle")
        self.setheading(90)
        self.setposition(0, -180)
        self.showturtle()

