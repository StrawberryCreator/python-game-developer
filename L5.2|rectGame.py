import pygame as py
import random as r

py.init ()
screen = py.display.set_mode ((500, 500))

class block (py.sprite.Sprite):
    def __init__ (self, color):
        super().__init__()
        self.image = py.Surface ((50, 40))
        self.image.fill (color)
        self.rect = self.image.get_rect ()
        self.position ()
    def position (self):
        self.rect.y = r.randint (-300, 0)
        self.rect.x = r.randint (30, 470)
    def update (self):
        self.rect.y += 1
        if self.rect.y >= 500:
            self.position ()

class player (block):
    def update (self):
        pos = py.mouse.get_pos ()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

blocks = py.sprite.Group ()
allBlocks = py.sprite.Group ()

for x in range (20):
    enemy = block ("black")
    blocks.add (enemy)
    allBlocks.add (enemy)
playerBlock = player ("red")
allBlocks.add (playerBlock)

clock = py.time.Clock ()

while True:
    screen.fill ("white")
    allBlocks.update ()
    allBlocks.draw (screen)
    hitlist = py.sprite.spritecollide (playerBlock, blocks, False)
    for hit in hitlist:
        hit.position ()
    clock.tick (30)
    py.display.update ()
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()