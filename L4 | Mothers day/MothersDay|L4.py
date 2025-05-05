import pgzrun as pg

WIDTH = 600
HEIGHT = 600

love = 0
lpc = 1
lps = 0
biggerHearts = 0
friends = 0

heart = Actor ("heart.png")
heart.pos = (300, 275)

biggerHeart = Actor ("biggerheart.png")
biggerHeart.pos = (90, 70)

friend = Actor ("friend.png")
friend.pos = (110, 510)

def draw ():
    screen.clear
    screen.blit ("bg.png", (0, 0))
    heart.draw ()
    biggerHeart.draw ()
    friend.draw ()
    screen.draw.text ("bigger heart | +1 love/click | $10 | owned: " + str(biggerHearts), midtop = (400, 70), color = "black")
    screen.draw.text ("mother | +100 love/s | $100 | owned: " + str(friends), midtop = (400, 530), color = "black")
    screen.draw.text ("love: " + str(love), midtop = (300, 350), color = "black")
    screen.draw.text ("love/click: " + str(lpc), midtop = (300, 375), color = "black")
    screen.draw.text ("love/second: " + str(lps), midtop = (300, 400), color = "black")

def on_mouse_down (pos):
    global love, lpc, lps, biggerHearts, friends
    if heart.collidepoint (pos):
        love += lpc
    if biggerHeart.collidepoint (pos):
        if love >= 10:
            love -= 10
            biggerHearts += 1
            lpc += 1
    if friend.collidepoint (pos):
        if love >= 100:
            love -= 100
            friends += 1
            lps += 100

def lovePerSecond ():
    global love
    love += lps
    clock.schedule (lovePerSecond, 1)

clock.schedule (lovePerSecond, 1)

pg.go ()