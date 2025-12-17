import turtle
from turtle import Turtle, Screen
from my_turtle import MyTurtle
from cars import Car
from scoreboard import ScoreBoard
import time
import random



screen = Screen()
screen.screensize(1200, 600)
screen.tracer(0)



tommy = MyTurtle()
car_manager = Car()
level = ScoreBoard()

screen.listen()
screen.onkey(tommy.go_up, "Up")
screen.onkey(tommy.go_down, "Down")


game_is_on = True
time_speed = 0.1
while game_is_on:
    time.sleep(time_speed)
    screen.update()

    car_manager.create_cars()
    car_manager.move()
    level.display_score()


    # detect collision with cars
    for car in car_manager.all_car:
        if tommy.distance(car) <= 20:
            game_is_on = False
            tommy.write("Game Over!", align="center", font = ("Courier", 48, "normal"))

    # detect collision with the upper wall
    if tommy.ycor() == 280:
        car_manager.level_up()
        tommy.goto(0, -280)
        # time_speed *= 0.99
        level.increase_score()
        level.clear()






screen.exitonclick()