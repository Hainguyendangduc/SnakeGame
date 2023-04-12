from turtle import Turtle

ALIGHMENT = "center"
FONT = ("Arial", 10, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 285)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.count} High score: {self.high_score}", align=ALIGHMENT, font=FONT)

    def reset(self):
        if self.count > self.high_score:
            with open("data.txt", "w") as data:
                data.write(f"{self.count}")
            self.high_score = self.count
        self.count = 0
        self.update()

    def increase_score(self):
        self.count += 1
        self.clear()
        self.update()