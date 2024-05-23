from turtle import Turtle
class Grid(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.hideturtle()
        self.penup()
        self.goto(0,-300)
        self.pendown()
        self.setheading(90)
        self.forward(600)
