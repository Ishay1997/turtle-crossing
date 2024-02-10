import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
go_sleep = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager(screen)
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(go_sleep)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish_line():
        scoreboard.level_up()
        car_manager.level_up()
        player.go_to_start()


screen.exitonclick()
