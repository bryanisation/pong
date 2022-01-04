from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor=350, ycor=0, paddle=True) -> None:
        super().__init__()
        self.x = xcor
        self.y = ycor
        self.move_x = 10
        self.move_y = 10
        if paddle:
            self.shape("square")
            self.shapesize(stretch_wid=4, stretch_len=1)
            self.color("white")
            self.penup()
            self.goto(self.x, self.y)
        else:
            self.shape("circle")
            self.shapesize(stretch_wid=1, stretch_len=1)
            self.color("white")
            self.penup()
            self.goto(self.x, self.y)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
