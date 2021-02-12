from turtle import Turtle

class Pong(Turtle):
    def __init__(self,position):
        super().__init__()
        self.setpos(position)
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)






    def go_up(self):
        new_y = self.ycor()+20.0
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20.0
        self.goto(self.xcor(), new_y)