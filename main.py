import time
from turtle import Turtle, Screen
from tile_manager import TileManager
from player import Player
from ball import Ball

# Set Environment
screen = Screen()
screen.setup(600, 800)
screen.bgcolor("black")
screen.title("BlackOut Game")
screen.tracer(0)

# Set Screen User
tile_manager = TileManager()
player = Player()
ball = Ball()

# Set Player Moves
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

# Start Game
game_is_on = True
while game_is_on:
    screen.update()
    # time.sleep(1)
    ball.move()

    # Detect collision with tiles
    for tile in tile_manager.tiles:
        ball_tile_dist = ball.distance(tile)
        if ball_tile_dist < 25 and ball.ycor() + 20 == tile.ycor():
            print(ball_tile_dist)
            tile.hideturtle()
            tile_manager.tiles.remove(tile)
            ball.setheading(270)

    # Detect collision with side walls

    # Detect collision with bottom wall

    # Detect collision with player paddle
    if ball.distance(player) < 50 and ball.ycor() <= -180:
        ball.setheading(90)

screen.exitonclick()
