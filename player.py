from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.setposition(0, -380)
        self.showturtle()

    def move_left(self):
        self.backward(20)

    def move_right(self):
        self.forward(20)

    def set_player(self):
        self.setposition(0, -380)

    def set_paddle(self, event):
        paddle_x = -300 + event.x
        self.setx(paddle_x)
