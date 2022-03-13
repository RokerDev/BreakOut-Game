from turtle import Turtle, Screen
from tile import Tile

screen = Screen()
screen.setup(600, 800)
screen.bgcolor("black")
screen.title("BlackOut Game")
# screen.tracer(0)

tile = Tile(screen.window_width(), screen.window_height())

screen.exitonclick()
