import time
from turtle import Screen
from food import Food, Boundary
from scoreboard import ScoreBoard
from snake import Snake

# play area is 600x600


screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor('black')
screen.title('Nokia Snake')

all_segments = []
game_on: bool = True

screen.tracer(0)
snake = Snake()
screen.listen()

# below does the movement for the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
food = Food()
boundary = Boundary()
score = ScoreBoard()
score.hideturtle()

while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    # detection with food
    if snake.head.distance(food) < 15:
        food.new_food()
        score.increment()
        score.update()
        snake.extend()
    # detection with boundary
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        game_on = False
        score.game_over()

    # detect collision with tail
    # if head collides with any segment of the body
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 5:
            game_on = False
            score.game_over()

screen.exitonclick()
