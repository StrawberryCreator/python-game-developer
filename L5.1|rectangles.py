import pygame as py

py.init ()
screen = py.display.set_mode ((500, 500))

class rectangle ():
    def __init__ (self, color, dimensions):
        self.color = color
        self.dimensions = dimensions
        self.screen = screen
    def draw (self):
        self.drawRect = py.draw.rect (self.screen, self.color, self.dimensions)

rect1 = rectangle ("red", (125, 350, 50, 65))
rect2 = rectangle ("green", (250, 150, 65, 50))
rect3 = rectangle ("blue", (375, 250, 40, 70))

while True:
    screen.fill ("white")
    rect1.draw ()
    rect2.draw ()
    rect3.draw ()
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
    py.display.update ()