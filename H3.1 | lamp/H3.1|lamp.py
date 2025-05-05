import pygame as py

py.init ()

screen = py.display.set_mode ((125, 200))

py.display.set_caption ("Birthday card")

font = py.font.SysFont ("Calibri", 25)

while True:
    lampOn = py.image.load ("H3.1 | lamp/lampOn.png")
    lampOff = py.image.load ("H3.1 | lamp/lampOff.png")
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
        if event.type == py.MOUSEBUTTONDOWN:
            screen.fill ("black")
            screen.blit (lampOn, (0, 0))
        elif event.type == py.MOUSEBUTTONUP:
            screen.fill ("black")
            screen.blit (lampOff, (0, 0))
    py.display.update ()