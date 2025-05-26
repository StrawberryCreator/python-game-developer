import pygame as py

py.init ()
screen = py.display.set_mode ((800, 800))
screen.fill ("white")

bullets1 = []
bullets2 = []

gameOver = False
health1 = 10
health2 = 10
winner = ""
bg = py.image.load ("L6 | SpaceInvaders/images/bg.png")
p1 = py.transform.rotate (py.transform.scale (py.image.load ("L6 | SpaceInvaders/images/red.png"), (50, 50)), 90)
p1Rect = py.Rect (75, 175, 50, 50)
p2 = py.transform.rotate (py.transform.scale (py.image.load ("L6 | SpaceInvaders/images/yellow.png"), (50, 50)), 270)
p2Rect = py.Rect (675, 575, 50, 50)
border = py.Rect (375, 0, 50, 800)

font = py.font.SysFont ("Calibri", 50)

def draw ():
    for i in bullets1:
        py.draw.rect (screen, "red", i)
    for i in bullets2:
        py.draw.rect (screen, "yellow", i)
    healthTxt1 = font.render (f"Health: {health1}", True, "white")
    healthTxt2 = font.render (f"Health: {health2}", True, "white")
    winTxt = font.render (f"Game over, {winner} won!", True, "white")
    screen.blit (healthTxt1, (10, 10))
    screen.blit (healthTxt2, (555, 10))
    if gameOver:
        screen.blit (bg, (0, 0))
        screen.blit (winTxt, (150, 225))

def p1Control (keys):
    if keys[py.K_w] and p1Rect.y > 10:
        p1Rect.y -= 1
    if keys[py.K_a] and p1Rect.x > 10:
        p1Rect.x -= 1
    if keys[py.K_s] and p1Rect.y < 735:
        p1Rect.y += 1
    if keys[py.K_d] and p1Rect.x < 315:
        p1Rect.x += 1

def p2Control (keys):
    if keys[py.K_UP] and p2Rect.y > 10:
        p2Rect.y -= 1
    if keys[py.K_LEFT] and p2Rect.x > 435:
        p2Rect.x -= 1
    if keys[py.K_DOWN] and p2Rect.y < 735:
        p2Rect.y += 1
    if keys[py.K_RIGHT] and p2Rect.x < 740:
        p2Rect.x += 1

def bulletsMove (bullets1, bullets2):
    global health1, health2, winner, gameOver
    for i in bullets1:
        i.x += 1
        if p2Rect.colliderect (i):
            bullets1.remove (i)
            health2 -= 1
            if health2 == 0:
                winner = "red"
                gameOver = True
                draw ()
        elif i.x >= 800:
            bullets1.remove (i)
    for i in bullets2:
        i.x -= 1
        if p1Rect.colliderect (i):
            bullets2.remove (i)
            health1 -= 1
            if health1 == 0:
                winner = "yellow"
                gameOver = True
                draw ()
        elif i.x <= 0:
            bullets2.remove (i)

while True:
    for event in py.event.get ():
        if event.type == py.QUIT:
            exit ()
        if event.type == py.KEYDOWN:
            if event.key == py.K_RSHIFT:
                bulletRect = py.Rect (p2Rect.x, p2Rect.y + 25, 10, 5)
                bullets2.append (bulletRect)
            if event.key == py.K_LSHIFT:
                bulletRect = py.Rect (p1Rect.x + 50, p1Rect.y + 25, 10, 5)
                bullets1.append (bulletRect)
    if not(gameOver):
        screen.blit (bg, (0, 0))
        screen.blit (p1, (p1Rect.x, p1Rect.y))
        screen.blit (p2, (p2Rect.x, p2Rect.y))
        py.draw.rect (screen, "black", border)
        keys = py.key.get_pressed ()
        p1Control (keys)
        p2Control (keys)
        draw ()
    bulletsMove (bullets1, bullets2)
    py.display.update ()