from turtle import Turtle
ALIGHMENT = "center"
FONT = ("Arial", 10, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 285)

    def update(self):
        self.count += 1
        self.clear()
        self.write(arg=f"Score: {self.count}", align=ALIGHMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.color("red")
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGHMENT, font=("Arial", 15, "bold"))
        self.goto(0, -20)
        self.write(arg=f"Score: {self.count}", align=ALIGHMENT, font=FONT)




