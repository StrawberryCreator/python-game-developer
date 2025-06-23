import pygame as py

py.init ()
screen = py.display.set_mode ((800, 800))
screen.fill ("white")

lives = 5
score = 0
gameOver = False
starMode = False
starTimer = 0

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
        self.direction = "up"
        self.update_rotation ()
    def update_rotation (self):
        if self.direction == "up":
            self.angle = 0
            self.head = (self.x, self.y)
        if self.direction == "right":
            self.angle = 90
            self.head = (self.x, self.y)
        if self.direction == "down":
            self.angle = 180
            self.head = (self.x, self.y)
        if self.direction == "left":
            self.angle = 270
            self.head = (self.x, self.y)
        self.rotatedShip = py.transform.rotate (self.image, self.angle)
        self.rotatedRect = self.rotatedShip.get_rect ()
        self.rotatedRect.center = self.x, self.y
    def draw (self, screen):
        screen.blit (self.rotatedShip, self.rotatedRect)
    def turnLeft (self):
        directions = ["up", "left", "down", "right"]
        index = directions.index (self.direction)
        self.direction = directions [(index+1)%4]
        self.update_rotation
    def turnRight (self):
        directions = ["up", "right", "down", "left"]
        index = directions.index (self.direction)
        self.direction = directions [(index+1)%4]
        self.update_rotation
    def move (self):
        if self.direction == "up":
            if self.y > 0:
                self.y -= 5
        if self.direction == "right":
            if self.x < 800:
                self.x += 5
        if self.direction == "down":
            if self.y < 800:
                self.y += 5
        if self.direction == "left":
            if self.x > 0:
                self.x -= 5

player = Ship ()

while True:
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
    screen.blit (bg, (0, 0))
    player.draw (screen)
    py.display.update ()