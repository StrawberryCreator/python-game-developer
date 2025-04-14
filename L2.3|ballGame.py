import pygame as py

py.init ()

screen = py.display.set_mode ((1000, 500))

py.display.set_caption ("Bouncing ball")

ball = py.draw.circle (surface = screen, color = "black", center = [500, 250], radius = 50)
speed = [1, 1]

while True:
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
    screen.fill ("white")
    ball = ball.move (speed)
    if ball.left <= 0 or ball.right >= 1000:
        speed[0] = -speed[0]
    if ball.top <= 0 or ball.bottom >= 500:
        speed[1] = -speed[1]
    py.draw.circle (surface = screen, color = "black", center = ball.center, radius = 50)
    py.display.update ()