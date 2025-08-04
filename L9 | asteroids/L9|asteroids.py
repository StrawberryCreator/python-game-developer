import pygame as py
import random as r
import math

py.init ()
screen = py.display.set_mode ((800, 800))
screen.fill ("white")

font = py.font.SysFont ("Ariel", 75)

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
        self.corners = [(0,0), (800,0), (800,800), (0,800)]
        self.start = r.choice (self.corners)
        self.target = r.choice([i for i in self.corners if i != self.start])
        self.x, self.y = self.start
        self.tx, self.ty = self.target
        self.rect = py.Rect (self.x, self.y, self.size, self.size)
        self.speed = r.uniform (1.0, 1.5)
        dx = self.tx - self.x
        dy = self.ty - self.y
        distance = math.hypot (dx, dy)
        self.dx = dx / distance * self.speed
        self.dy = dy / distance * self.speed
    def move (self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y
    def draw (self):
        screen.blit (self.image, (self.rect.x, self.rect.y))

asteroids = [Asteroid () for i in range (2)]
player = Ship ()

currentTime = py.time.get_ticks ()
delay = 3000

while True:
    screen.blit (bg, (0, 0))
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                bullet = Bullet (player.rotatedRect.centerx, player.rotatedRect.centery, player.angle + 90)
                bullets.append (bullet)
    lastSpawnTime = py.time.get_ticks ()
    if lastSpawnTime - currentTime >= delay:
        asteroids.extend ([Asteroid () for i in range (r.randint (1,3))])
        currentTime = lastSpawnTime
    if gameOver:
        txt = font.render (f"GAME OVER! score: {score}", True, "red")
        screen.blit (txt, (100, 300))
    elif score >= 20:
        txt = font.render (f"YOU WIN! score: {score}", True, "red")
        screen.blit (txt, (100, 300))
    else:
        scoreTxt = font.render (f"score: {score}", True, "white")
        screen.blit (scoreTxt, (10, 10))
        livesTxt = font.render (f"lives: {lives}", True, "white")
        screen.blit (livesTxt, (10, 75))
        for i in asteroids:
            i.move ()
            i.draw ()
        for bul in bullets:
            bul.move ()
            bul.draw ()
        for i in asteroids:
            for j in bullets:
                if i.rect.collidepoint (j.x, j.y):
                    bullets.remove (j)
                    asteroids.remove (i)
                    if i.size == 50:
                        bangSmall.play ()
                    else:
                        bangBig.play ()
                    score += 1
        for i in asteroids:
            if i.rect.colliderect (player.rotatedRect):
                asteroids.remove (i)
                lives -= 1
                if lives == 0:
                    gameOver = True
        key = py.key.get_pressed ()
        player.move (key)
        player.draw (screen)
    py.display.update ()
