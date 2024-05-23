from turtle import Turtle
STARTSPEED=0.05

class Ball(Turtle):
    def __init__(self, xp, yp):
        super().__init__()
        self.shape("circle")
        self.color("Blue")
        self.penup()
        self.goto(xp, yp)
        self.setheading(30)
        self.speed("fastest")
        self.Speed=0.05

    def ballmove(self):
        self.forward(10)

    def ballpaddlecollide(self):
        global h1, newh1
        h1 = self.heading()
        print(h1)
        if h1 > 180 and h1 < 270:
            newh1 = 540 - h1
        elif h1 > 90 and h1 < 180:
            newh1 = 180 - h1
        elif h1 > 270 and h1 < 360:
            newh1 = 540 - h1
        elif h1 > 0 and h1 < 90:
            newh1 = 180 - h1
        elif h1 == 0:
            newh1 = 180
        elif h1 == 180:
            newh1 = 0
        print(newh1)
        self.setheading(newh1)
        self.Speed*=0.9

    def ballwallcollide(self):
        global h2, newh2
        h2 = self.heading()
        print(h2)
        if h2 > 0 and h2 < 90:
            newh2 = 360 - h2
        elif h2 > 90 and h2 < 180:
            newh2 = 360 - h2
        elif h2 > 270 and h2 < 360:
            newh2 = 360 - h2
        elif h2 > 180 and h2 < 270:
            newh2 = 360 - h2
        elif h2 == 90:
            newh2 = 270
        elif h2 == 270:
            newh2 = 90
        print(newh2)
        self.setheading(newh2)

    def ballreset(self):
        self.Speed=STARTSPEED
        h3=self.heading()
        self.setheading(h3+180)
        self.goto(0,0)




