from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(screen.bye, "space")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)

    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.new_score()

    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.xcor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tail
    for segments in snake.segments:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 5:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
