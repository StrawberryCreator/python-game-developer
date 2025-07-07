import pygame as py

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
asteroidSmall = py.image.load ("L9 | asteroids/images/smallAsteroid.png")
asteroidMedium = py.image.load ("L9 | asteroids/images/bigAsteroid.png")
asteroidBig = py.image.load ("L9 | asteroids/images/megaAsteroid.png")
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
                self.y -= 5
        if key[py.K_d]:
            if self.x < 800:
                self.x += 5
        if key[py.K_s]:
            if self.y < 800:
                self.y += 5
        if key[py.K_a]:
            if self.x > 0:
                self.x -= 5
        if key[py.K_e]:
            if self.angle <= 5:
                self.angle = 360
            else:
                self.angle -= 2
            player.updateRotation ()
        if key[py.K_q]:
            if self.angle >= 355:
                self.angle = 0
            else:
                self.angle += 2
            player.updateRotation ()
        if key[py.K_SPACE]:
                bullet = Bullet (self.rotatedRect.x, self.rotatedRect.y, self.angle)
                bullets.append (bullet)
        self.rotatedRect.center = self.x, self.y

class Bullet:
    def __init__ (self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.radius = 10
        self.speed = 5
        self.color = "red"
    def draw (self):
        py.draw.circle (screen, self.color, (self.x, self.y), self.radius)
    def move (self):
        

player = Ship ()

while True:
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
    key = py.key.get_pressed ()
    player.move (key)
    screen.blit (bg, (0, 0))
    player.draw (screen)
    py.display.update ()
