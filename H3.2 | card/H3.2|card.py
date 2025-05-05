import pygame as py
import time as t

py.init ()

screen = py.display.set_mode ((500, 500))
py.display.set_caption ("animated card")

font = py.font.SysFont ("Calibri", 10)

frames = ["H3.2 | card/1.png", "H3.2 | card/2.png", "H3.2 | card/3.png", "H3.2 | card/4.png", "H3.2 | card/5.png", "H3.2 | card/6.png", "H3.2 | card/7.png", "H3.2 | card/8.png", "H3.2 | card/9.png", "H3.2 | card/10.png", "H3.2 | card/11.png", "H3.2 | card/12.png"]

speed = 0.15

while True:
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
    for img in frames:
        img = py.image.load (img)
        screen.blit (img, (0, 0))
        text = font.render (str(round(speed, 2)), True, "white")
        screen.blit (text, (250, 25))
        py.display.update ()
        t.sleep (speed)