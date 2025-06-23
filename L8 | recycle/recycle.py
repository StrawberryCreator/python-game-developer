import pygame as py
import random as r

py.init ()
screen = py.display.set_mode ((750, 750))
screen.fill ("white")
font = py.font.SysFont ("Calibri", 50)
bg = py.transform.scale (py.image.load ("L8 | recycle/images/bg.jpeg"), (1500, 750))
clock = py.time.Clock ()

badCount = 25
goodCount = 20
score = 0
time = 0
startTime = -1
gameOver = False
mode = 0

class Player (py.sprite.Sprite):
    def __init__ (self):
        global mode
        py.sprite.Sprite.__init__ (self)
        image1 = py.transform.scale (py.image.load ("L8 | recycle/images/bin.png"), (30, 25))
        image2 = py.transform.scale (py.image.load ("L8 | recycle/images/grabber.png"), (30, 25))
        mode = 0
        self.images = [image1, image2]
        self.image = self.images[0]
        self.rect = self.image.get_rect ()  
    def move (self):
        global startTime, mode
        if not gameOver:
            if py.key.get_pressed () [py.K_w]:
                if self.rect.top > 0:
                    self.rect.y -= 5
                if startTime == -1:
                    startTime = py.time.get_ticks()
            if py.key.get_pressed () [py.K_a]:
                if self.rect.left > 0:
                    self.rect.x -= 5
                if startTime == -1:
                    startTime = py.time.get_ticks()
            if py.key.get_pressed () [py.K_s]:
                if self.rect.bottom < 750:
                    self.rect.y += 5
                if startTime == -1:
                    startTime = py.time.get_ticks()
            if py.key.get_pressed () [py.K_d]:
                if self.rect.right < 750:
                    self.rect.x += 5
                if startTime == -1:
                    startTime = py.time.get_ticks()
            if py.key.get_pressed () [py.K_q]:
                mode = 0
            if py.key.get_pressed () [py.K_e]:
                mode = 1
            self.image = self.images[mode]
            if not startTime:
                startTime = py.time.get_ticks()

class GoodItem (py.sprite.Sprite):
    def __init__ (self, item):
        py.sprite.Sprite.__init__ (self)
        image = py.transform.scale (py.image.load (f"L8 | recycle/images/good{item}.png"), (60, 50))
        self.image = image
        self.rect = self.image.get_rect ()    

class BadItem (py.sprite.Sprite):
    def __init__ (self):
        py.sprite.Sprite.__init__ (self)
        image = py.transform.scale (py.image.load ("L8 | recycle/images/bad1.png"), (60, 50))
        self.image = image
        self.rect = self.image.get_rect ()

goodItems = py.sprite.Group ()
badItems = py.sprite.Group ()
allSprites = py.sprite.Group ()

bin = Player ()
allSprites.add (bin)

def overlapCheck (sprite, group):
    for i in range (100):
        sprite.rect.center = r.randint (50, 700), r.randint (50, 700)
        if not py.sprite.spritecollideany (sprite, group):
            return True
    return False
        
for x in range (badCount):
    bad = BadItem ()
    if overlapCheck (bad, allSprites):
        badItems.add (bad)
        allSprites.add (bad)

for x in range (goodCount):
    good = GoodItem (r.randint (1, 2))
    if overlapCheck (good, allSprites):
        goodItems.add (good)
        allSprites.add (good)

while True:
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
    
    clock.tick (60)
    keys = py.key.get_pressed ()
    bin.move ()

    hitlistGood = py.sprite.spritecollide(bin, goodItems, True)
    for hit in hitlistGood:
        if mode == 0:
            score += 5
        else:
            score -= 2
    hitlistBad = py.sprite.spritecollide(bin, badItems, True)
    for hit in hitlistBad:
        if mode == 0:
            score -= 4
        else:
            score += 3

    if not (startTime == -1) and not (gameOver):
        elapsed_time = (py.time.get_ticks() - startTime) / 1000
        time = round(elapsed_time, 1)
    
    screen.blit (bg, (-375, 0))
    allSprites.update ()
    allSprites.draw (screen)
    scoreTxt = font.render (f"Score: {score}", True, "black")
    screen.blit (scoreTxt, (10, 10))
    timeTxt = font.render(f"Time: {time}", True, "black")
    screen.blit(timeTxt, (10, 50))

    if len(goodItems) == 0 and len(badItems) == 0:
        gameOver = True
    
    py.display.update ()