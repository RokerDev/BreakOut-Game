import time
from turtle import Screen
from tile_manager import TileManager
from player import Player
from ball import Ball
from scoreboard import Scoreboard

# Set Environment
screen = Screen()
screen.setup(600, 800)
screen.bgcolor("black")
screen.title("BreakOut Game")
screen.tracer(0)

# Set Screen User
tile_manager = TileManager()
player = Player()
ball = Ball()
scoreboard = Scoreboard()

# Set Player Moves
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

mouse_on_screen = screen.getcanvas()
mouse_on_screen.bind('<Motion>', player.set_paddle)

# mouse_on_screen = screen.getcanvas()
# mouse_on_screen.bind('<Motion>', ball.set_mouse_ball)

# Start Game
move = 5
game_is_on = True

while game_is_on:

    ball.move(move)
    move = 2
    screen.update()

    # Detect collision with tiles
    for tile in tile_manager.tiles:

        difference_y = tile.ycor() - ball.ycor()
        difference_x = tile.xcor() - ball.xcor()
        if 16 < difference_y < 22 and ball.distance(tile) < 36:
            tile_manager.remove_tile(tile)
            scoreboard.add_points()
            if -27 < difference_x < 27:
                ball.bounce_y()
            else:
                ball.bounce_y()

        elif -21 < difference_y < -17 and ball.distance(tile) < 36:
            tile_manager.remove_tile(tile)
            scoreboard.add_points()
            if -27 < difference_x < 27:
                ball.bounce_y()
            else:
                ball.bounce_y()

        elif -10 < difference_y < 10 and 35 > ball.distance(tile) > 32:
            if difference_x >= 32:
                tile_manager.remove_tile(tile)
                scoreboard.add_points()
                if 100 > ball.heading() > 80:
                    ball.bounce_x(10)
                elif 280 > ball.heading() > 260:
                    ball.bounce_x(-10)
                else:
                    ball.bounce_x()

            elif difference_x <= -32:
                tile_manager.remove_tile(tile)
                scoreboard.add_points()
                if 100 > ball.heading() > 80:
                    ball.bounce_x(-10)
                elif 280 > ball.heading() > 260:
                    ball.bounce_x(10)
                else:
                    ball.bounce_x()

    # Detect collision with side walls
    if ball.xcor() <= -289 or ball.xcor() >= 281:
        ball.bounce_x()
        # time.sleep(1)

    # Detect collision with top wall
    if ball.ycor() >= 190:
        ball.bounce_y()
        # time.sleep(1)

    # Detect collision with player paddle
    if ball.distance(player) < 63 and ball.ycor() <= -360:
        print(ball.ycor(), ball.heading())
        changer = player.xcor() - ball.xcor()
        ball.sety(-360)
        ball.bounce_y(changer / 2)

    # Detect collision with bottom wall
    if ball.ycor() <= -400:
        player.set_player()
        ball.set_ball()
        time.sleep(1)

    # Detect end lvl
    if tile_manager.end_lvl():
        # print some congratulations and switch to next lvl
        print("Congratz lvl up.")

screen.exitonclick()
