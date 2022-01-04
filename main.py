from time import sleep
from turtle import Screen

from paddle import Paddle

"""
TODO:
Create Screen
Create and Move the paddle
Create the ball and make it move
Detect collision with wall and bounce
Detect collision with paddle
Detect when paddle misses
Keep score
"""
if __name__ == "__main__":
    # CREATE SCREEN
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)  # Controlls animations

    # CREATE PADDLES AND BALL
    paddle_left = Paddle()
    paddle_right = Paddle(-350, 0)
    ball = Paddle(0, 0, paddle=False)

    # LISTEN FOR PADDLE MOVEMENTS
    screen.listen()
    screen.onkey(paddle_left.go_up, "Up")
    screen.onkey(paddle_left.go_down, "Down")
    screen.onkey(paddle_right.go_up, "w")
    screen.onkey(paddle_right.go_down, "s")

    # GAME LOOP
    game_is_on = True
    while game_is_on:
        sleep(0.1)
        screen.update()
        ball.move()

        # DETECT COLLISION WITH WALLS
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # DETECT COLLISION WITH RIGHT PADDLE
        if (
            ball.distance(paddle_right) < 50
            and ball.xcor() > 340
            or ball.distance(paddle_left) < 50
            and ball.xcor() < -340
        ):
            ball.bounce_x()

    screen.exitonclick()
