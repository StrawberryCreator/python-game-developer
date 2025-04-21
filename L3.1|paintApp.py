import pygame as py

py.init ()

screen = py.display.set_mode ((500, 500))

py.display.set_caption ("Paint app")

colors = ["red", "yellow", "green", "blue", "pink", "white", "black"]

drawing = False
startPos = None
currentPos = None
color = "black"
colorNum = 6

screen.fill ("white")

while True:
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
        elif event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                startPos = event.pos
                py.display.update ()
        elif event.type == py.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                py.display.update ()
        elif event.type == py.MOUSEMOTION:
            if drawing:
                currentPos = event.pos
                py.draw.line (screen, color, startPos, currentPos)
                startPos = currentPos
                py.display.update ()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_0:
                if colorNum >= 6:
                    colorNum = 0
                else:
                    colorNum += 1
                color = colors[colorNum]