import pygame as py
import random as r
import math

py.init ()
screen = py.display.set_mode ((800, 800))
screen.fill ("white")

lives = 5
score = 0
gameOver = False
starMode = False
starTimer = 0

bullets = []

bg = py.image.load ("L9 | asteroids/images/bg.png")
ufo = py.image.load ("L9 | asteroids/images/UFO.png")
star = py.image.load ("L9 | asteroids/images/star.png")
ship = py.image.load ("L9 | asteroids/images/ship.png")

bangSmall = py.mixer.Sound ("L9 | asteroids/sounds/bangSmall.wav")
bangBig = py.mixer.Sound ("L9 | asteroids/sounds/bangLarge.wav")
shoot = py.mixer.Sound ("L9 | asteroids/sounds/shoot.wav")

class Ship:
    def __init__ (self):
        self.image = ship
        self.width = self.image.get_width ()
        self.height = self.image.get_height ()
        self.x = 400
        self.y = 400
        self.angle = 0
        self.updateRotation ()
    def updateRotation (self):
        self.rotatedShip = py.transform.rotate (self.image, self.angle)
        self.rotatedRect = self.rotatedShip.get_rect ()
        self.rotatedRect.center = self.x, self.y
    def draw (self, screen):
        screen.blit (self.rotatedShip, self.rotatedRect)
    def move (self, key):
        if key[py.K_w]:
            if self.y > 0:
                self.y -= 2.5
        if key[py.K_d]:
            if self.x < 800:
                self.x += 2.5
        if key[py.K_s]:
            if self.y < 800:
                self.y += 2.5
        if key[py.K_a]:
            if self.x > 0:
                self.x -= 2.5
        if key[py.K_e]:
            if self.angle <= 5:
                self.angle = 360
            else:
                self.angle -= 2.5
            player.updateRotation ()
        if key[py.K_q]:
            if self.angle >= 355:
                self.angle = 0
            else:
                self.angle += 2.5
            player.updateRotation ()
        self.rotatedRect.center = self.x, self.y

class Bullet:
    def __init__ (self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.radius = 10 
        self.speed = 5
        self.color = "red"
        self.dx = math.cos (math.radians (-self.dir)) * self.speed
        self.dy = math.sin (math.radians (-self.dir)) * self.speed
    def draw (self):
        py.draw.circle (screen, self.color, (self.x, self.y), self.radius)
    def move (self):
        self.x += self.dx
        self.y += self.dy

class Asteroid:
    def __init__ (self):
        self.rock = r.randint (1, 3)
        if self.rock == 1:
           self.image = py.image.load ("L9 | asteroids/images/smallAsteroid.png")
           self.size = 50
        if self.rock == 2:
           self.image = py.image.load ("L9 | asteroids/images/mediumAsteroid.png")
           self.size = 100
        if self.rock == 3:
           self.image = py.image.load ("L9 | asteroids/images/bigAsteroid.png")
           self.size = 150
        self.edge = r.randint (1, 4)
        if self.edge == 1:
            self.x = r.randint (0, 800)
            self.y = -100
        if self.edge == 2:
            self.x = 900
            self.y = r.randint (0, 800)
        if self.edge == 3:
            self.x = r.randint(0, 800)
            self.y = 900
        if self.edge == 4:
            self.x = -100
            self.y = r.randint (0, 800)
        self.rect = py.Rect (self.x, self.y, self.size, self.size)
        self.speed = r.uniform (1.5, 3.0)
    def move (self):
        dx = (self.x - 400) * -1 - self.rect.centerx
        dy = (self.y - 400) * -1 - self.rect.centery
        distance = (dx ** 2 + dy ** 2) ** 0.5
        self.vx = self.speed * dx / distance
        self.vy = self.speed * dy / distance
        self.rect.x += self.vx
        self.rect.y += self.vy
    def draw (self):
        screen.blit (self.image, (self.rect.x, self.rect.y))

asteroids = [Asteroid () for i in range (5)]
player = Ship ()

while True:
    screen.blit (bg, (0, 0))
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                bullet = Bullet (player.rotatedRect.centerx, player.rotatedRect.centery, player.angle + 90)
                bullets.append (bullet)
    for i in asteroids:
        i.move ()
        i.draw ()
    for bul in bullets:
        bul.move ()
        bul.draw ()
    key = py.key.get_pressed ()
    player.move (key)
    player.draw (screen)
    py.display.update ()