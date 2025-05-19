import pygame as py

py.init ()
screen = py.display.set_mode ((500, 500))
screen.fill ("white")

font = py.font.SysFont ("Calibri", 25)

while True:
    ludo = py.image.load ("H5 | connect/images/ludo.png")
    ludoTxt = font.render ("Ludo", True, "red")
    subSurf = py.image.load ("H5 | connect/images/subway surfers.png")
    subSurfTxt = font.render ("Subway Surfers", True, "green")
    tmplRun = py.image.load ("H5 | connect/images/temple run.png")
    tmplRunTxt = font.render ("Temple Run", True, "blue")
    screen.blit (ludo, (25, 80))
    screen.blit (subSurfTxt, (300, 110))
    screen.blit (subSurf, (25, 205))
    screen.blit (tmplRunTxt, (300, 235))
    screen.blit (tmplRun, (25, 330))
    screen.blit (ludoTxt, (300, 360))
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
        if event.type == py.MOUSEBUTTONDOWN:
            pos = py.mouse.get_pos ()
            startPos = pos
            py.draw.circle (screen, "black", pos, 25)
        if event.type == py.MOUSEBUTTONUP:
            pos = py.mouse.get_pos ()
            endPos = pos
            py.draw.circle (screen, "black", pos, 25)
            py.draw.line (screen, "black", startPos, endPos, 5)
    py.display.update ()