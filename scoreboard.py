from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Turtle Racer", 24, "normal")
COORDINATES = (-220, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1

    def create_scoreboard(self):
        self.goto(COORDINATES)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.create_scoreboard()
