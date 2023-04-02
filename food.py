from turtle import Turtle
from random import choice
FOOD_POSITIONS = []

for step in range(-280, 280, 20):
    FOOD_POSITIONS.append(step)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed("fastest")
        # self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(choice(FOOD_POSITIONS), choice(FOOD_POSITIONS))
        self.refresh()

    def refresh(self):
        self.goto(choice(FOOD_POSITIONS), choice(FOOD_POSITIONS))
