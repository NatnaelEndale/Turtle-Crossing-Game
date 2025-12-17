from turtle import Turtle

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(0, -280)
        self.setheading(90)
    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

