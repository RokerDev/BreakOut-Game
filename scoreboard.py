from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.logo = "BreakOut Game"
        self.score = 0
        self.color("white")
        self.penup()
        self.write_logo()
        self.draw_logo_bottom_line()
        self.draw_top_line()
        self.scores = Turtle(visible=False)
        self.scores.color("white")
        self.scores.penup()
        self.show_score()

    def write_logo(self):
        self.setposition(-240, 320)
        self.write(self.logo, font=("Verdana", 45, "normal"))

    def draw_logo_bottom_line(self):
        self.setposition(-300, 300)
        self.pendown()
        self.goto(300, 300)
        self.penup()

    def draw_top_line(self):
        self.goto(-300, 200)
        self.pendown()
        self.goto(300, 200)
        self.penup()

    def show_score(self):
        self.scores.clear()
        self.scores.setposition(-120, 220)
        self.scores.write(f"Score: {self.score} ", font=("Verdana", 40, "normal"))

    def add_points(self):
        self.score += 1
        self.show_score()
