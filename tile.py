import random
from turtle import Turtle


class Tile(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.tiles = []
        self.colors = ["yellow", "blue", "green"]
        self.levels = 4
        self.height_position = int(screen_height / 2 - 100)
        self.width_position = int(screen_width / 2)

        self.create_tiles()

    def create_tiles(self):
        for pos_y in range(0, self.levels):
            for pos_x in range(-self.width_position + 25, self.width_position, 54):
                self.create_tile((pos_x, self.height_position))
            self.height_position -= 24

    def create_tile(self, position):
        tile = Turtle(shape="square")
        print(tile.turtlesize())
        tile.shapesize(stretch_len=2.5)
        print(tile.turtlesize())
        tile.penup()
        tile.hideturtle()
        tile.color(random.choice(self.colors))
        tile.speed(0)
        tile.setposition(position)
        tile.showturtle()
        self.tiles.append(tile)
