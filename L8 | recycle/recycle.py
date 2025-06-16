import pygame as py
import random as r

py.init ()
screen = py.display.set_mode ((750, 750))
screen.fill ("white")

font = py.font.SysFont ("Calibri", 50)

bg = py.image.load ("L8 | recycle/images/bg.png")

badCount = 25
goodCount = 20

class Player (py.sprite.Sprite):
    def __init__ (self):
        py.sprite.Sprite.__init__ (self)
        image = py.transform.scale (py.image.load ("L8 | recycle/images/bin.png"), (40, 50))
        self.image = image
        self.rect = self.image.get_rect ()

class GoodItem (py.sprite.Sprite):
    def __init__ (self, item):
        py.sprite.Sprite.__init__ (self)
        image = py.transform.scale (py.image.load (f"L8 | recycle/images/good{item}.png"), (40, 50))
        self.image = image
        self.rect = self.image.get_rect ()

class BadItem (py.sprite.Sprite):
    def __init__ (self):
        py.sprite.Sprite.__init__ (self)
        image = py.transform.scale (py.image.load ("L8 | recycle/images/bad1.png"), (40, 50))
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
    screen.blit (bg, (-240, 0))
    allSprites.draw (screen)
    py.display.update ()