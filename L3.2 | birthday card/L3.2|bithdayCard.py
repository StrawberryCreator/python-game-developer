import pygame as py
import time as t

py.init ()

screen = py.display.set_mode ((600, 600))

py.display.set_caption ("Birthday card")

font = py.font.SysFont ("Calibri", 25)

while True:
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
    text = font.render ("Happy birthday!", True, "black")
    img = py.image.load ("L3.2 | birthday card/1.jpg")
    screen.blit (img, (0, 0))
    screen.blit (text, (225, 300))
    py.display.update ()
    t.sleep (2)
    text = font.render ("Wish you a happy future...", True, "black")
    img = py.image.load ("L3.2 | birthday card/2.jpg")
    screen.blit (img, (0, 0))
    screen.blit (text, (50, 50))
    py.display.update ()
    t.sleep (2)
    text = font.render ("with a lot of cake.", True, "black")
    img = py.image.load ("L3.2 | birthday card/3.jpg")
    screen.blit (img, (0, 0))
    screen.blit (text, (50, 50))
    py.display.update ()
    t.sleep (2)