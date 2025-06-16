import pygame as py
import random as r

py.init ()
screen = py.display.set_mode ((864, 768))
screen.fill ("white")

font = py.font.SysFont ("Calibri", 50)

gameOver = False
flying = False
score = 0
groundX = 0
pipeDelay = 2500
lastPipe = py.time.get_ticks () - pipeDelay
passPipe = False

clock = py.time.Clock ()

bg = py.image.load ("L7 | flappy bird/images/bg.png")
ground = py.image.load ("L7 | flappy bird/images/ground.png")
restart = py.image.load ("L7 | flappy bird/images/restart.png")
restartRect = py.Rect (372, 279, 120, 42)

class Bird (py.sprite.Sprite):
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
            if self.rect.top <= 0:
                self.rect.y = 0
        global gameOver
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
            if self.rect.bottom >= 600:
                gameOver = True

class Pipe (py.sprite.Sprite):
    def __init__ (self, x, y, pos):
        py.sprite.Sprite.__init__ (self)
        self.image = py.image.load ("L7 | flappy bird/images/pipe.png")
        self.rect = self.image.get_rect ()
        if pos == 1:
            self.image = py.transform.flip (self.image, False, True)
            self.rect.bottomleft = [x, y]
        elif pos == -1:
            self.rect.topleft = [x, y]
    def update (self):
        self.rect.left -= 4
        if self.rect.left <= -78:
            self.kill ()
        if gameOver:
            self.kill ()

birdGroup = py.sprite.Group ()
pipeGroup = py.sprite.Group ()
flappy = Bird (100, 300)
birdGroup.add (flappy)

while True:
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
        if event.type == py.MOUSEBUTTONDOWN:
            pos = event.pos
            if gameOver:
                if restartRect.collidepoint (pos):
                    gameOver = False
                    flying = False
                    flappy.rect.center = (50, 300)
                    flappy.vel = 0
                    groundX = 0
                    score = 0
            else:
                flying = True
    clock.tick (60)
    screen.blit (bg, (0, 0))
    pipeGroup.draw (screen)
    pipeGroup.update ()
    birdGroup.draw (screen)
    birdGroup.update ()
    screen.blit (ground, (groundX, 600))
    scoreTxt = font.render (f"score: {score}", True, "white")
    screen.blit (scoreTxt, (10, 10))
    if pipeGroup:
        bird = birdGroup.sprites ()[0]
        pipe1 = pipeGroup.sprites ()[0]
        pipe2 = pipeGroup.sprites ()[1]
        if bird.rect.left > pipe1.rect.left and bird.rect.right < pipe1.rect.right and not(passPipe):
            passPipe = True
        if passPipe and bird.rect.left > pipe1.rect.right:
            passPipe = False
            score += 1
        if bird.rect.colliderect (pipe1.rect) or bird.rect.colliderect (pipe2.rect):
            gameOver = True
    if gameOver:
        screen.blit (restart, (restartRect.x, restartRect.y))
    if flying and gameOver == False:
        groundX -= 4
        if groundX <= -35:
            groundX = 0
        timeNow = py.time.get_ticks ()
        if timeNow - lastPipe > pipeDelay:
            y = r.randint (100, 500)
            topPipe = Pipe (800, y - 80, 1)
            bottomPipe = Pipe (800, y + 80, -1)
            pipeGroup.add (topPipe)
            pipeGroup.add (bottomPipe)
            lastPipe = timeNow
    py.display.update ()