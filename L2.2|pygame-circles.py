import pygame as py

py.init ()

screen = py.display.set_mode ((500, 500))

screen.fill ("white")

class myCircle:
    def __init__ (self, color, pos, radius):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.screen = screen
    def draw (self):
        py.draw.circle (self.screen, self.color, self.pos, self.radius)

c1 = myCircle ("red", (125, 250), 10)
c2 = myCircle ("green", (250, 250), 30)
c3 = myCircle ("blue", (375, 250), 20)

while True:
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
        if event.type == py.MOUSEBUTTONDOWN:
            c1.draw ()
            c2.draw ()
            c3.draw ()
            py.display.update ()