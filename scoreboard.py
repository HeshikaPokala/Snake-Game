from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = self.get_highest_score()  # Initialize with the highest score from file
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def get_highest_score(self):
        with open('data.txt') as data:
            return int(data.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.goto(0, 0)
        self.write(f'GAME OVER!', align="center", font=("Courier", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
