from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.leftpaddlescore=0
        self.rightpaddlescore=0
        self.color("White")
        self.penup()
        self.scoreupdate()

    def scoreupdate(self):
        self.clear()
        self.goto(-230,190)
        self.write(self.leftpaddlescore, move=False, align='left', font=('Arial', 80, 'normal'))
        self.goto(230,190)
        self.write(self.rightpaddlescore, move=False, align='right', font=('Arial', 80, 'normal'))
