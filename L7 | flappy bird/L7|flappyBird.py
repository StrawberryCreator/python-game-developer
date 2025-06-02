import pygame as py
import random as r

py.init ()
screen = py.display.set_mode ((864, 768))
screen.fill ("white")

gameOver = False
flying = False
score = 0
groundX = 0

clock = py.time.Clock ()

bg = py.image.load ("L7 | flappy bird/images/bg.png")
ground = py.image.load ("L7 | flappy bird/images/ground.png")

class bird (py.sprite.Sprite):
    def __init__ (self, x, y):
        py.sprite.Sprite.__init__ (self)
        self.images = []
        self.index = 0
        self.vel = 0
        self.clicked = False
        self.counter = 0
        for i in range (1, 4, 1):
            image = py.image.load (f"L7 | flappy bird/images/bird{i}.png")
            self.images.append (image)
        self.image = self.images [self.index]
        self.rect = self.image.get_rect ()
        self.rect.center = x, y
    def update (self):
        if flying:
            self.vel += 0.5
            if self.vel >= 5:
                self.vel = 5
            if self.rect.bottom <= 600:
                self.rect.y += self.vel
        if gameOver == False:
            if py.mouse.get_pressed () [0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
            if py.mouse.get_pressed () [0] == 0:
                self.clicked = False
            self.counter += 1
            if self.counter >= 5:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images [self.index]
                

birdGroup = py.sprite.Group ()
flappy = bird (50, 300)
birdGroup.add (flappy)

while True:
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
        if event.type == py.MOUSEBUTTONDOWN:
            flying = True
    clock.tick (60)
    screen.blit (bg, (0, 0))
    screen.blit (ground, (groundX, 600))
    birdGroup.draw (screen)
    birdGroup.update ()
    if flying and gameOver == False:
        groundX -= 4
        if groundX <= -35:
            groundX = 0
    py.display.update ()