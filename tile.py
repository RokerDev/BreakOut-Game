import random
from turtle import Turtle

tile_colors = ["Red", "Blue", "Yellow"]


class Tile(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_len=2.5)
        self.penup()
        self.color(random.choice(tile_colors))
        self.speed(0)

    def broken_tile(self):
        self.hideturtle()
