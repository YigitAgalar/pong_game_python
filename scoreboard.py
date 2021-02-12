from turtle import Turtle

(-200, 280)
class scoreboard(Turtle, ):
    def __init__(self, player , position):
        super().__init__()
        self.player = player
        self.score = 0
        self.hideturtle()
        self.setpos(position)
        self.color("white")
        self.write(f"Player {self.player} Score : {self.score} ", font=("Courier",20, "normal"))
        self.penup()


    def draw_line(self):
        self.clear()
        self.setpos(0, 300)
        self.pensize(5)
        self.setheading(270)
        self.pendown()
        while self.ycor()>-300:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Player {self.player} Score : {self.score} ", font=("Courier", 20, "normal"))

    def game_over(self):
        self.setpos(-120, 60)
        self.write(f" Player {self.player} won", font=("Courier", 20, "normal"))
