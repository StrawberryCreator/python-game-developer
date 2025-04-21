import pygame as py

py.init ()

screen = py.display.set_mode ((500, 500))

screen.fill ("white")

class myCircle:
    def __init__ (self, color, pos, radius, growSpeed):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.screen = screen
        self.growSpeed = growSpeed
        self.minRadius = radius
        self.growBig = True
    def draw (self):
        py.draw.circle (self.screen, self.color, self.pos, self.radius)
    def grow (self):
        if self.growBig:
            self.radius += self.growSpeed
            py.draw.circle (self.screen, self.color, self.pos, self.radius)
        else:
            self.radius -= self.growSpeed
            py.draw.circle (self.screen, self.color, self.pos, self.radius)
        if self.radius >= 100:
            self.growBig = False
        elif self.radius <= self.minRadius:
            self.growBig = True

c1 = myCircle ("red", (125, 250), 10, 3)
c2 = myCircle ("green", (250, 250), 30, 1)
c3 = myCircle ("blue", (375, 250), 20, 2)

while True:
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
        if event.type == py.MOUSEBUTTONUP:
            screen.fill ("white")
            c1.draw ()
            c2.draw ()
            c3.draw ()
            py.display.update ()
        if event.type == py.MOUSEBUTTONDOWN:
            screen.fill ("white")
            c1.grow ()
            c2.grow ()
            c3.grow ()
            py.display.update ()
