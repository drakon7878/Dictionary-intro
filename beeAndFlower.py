import os
os.environ['SDL_VIDEO_CENTERED'] = '1'


import pgzrun
import pgzero.screen
import pgzero.actor
import pgzero.rect
import pgzero.keyboard
import pgzero.clock
from random import randint

screen: pgzero.screen.Screen
Actor = pgzero.actor.Actor
Rect = pgzero.rect.Rect
keyboard: pgzero.keyboard.Keyboard
clock = pgzero.clock.Clock

WIDTH = 600
HEIGHT = 500

score = 0

gameOver = False

bee = Actor("bee")
bee.pos = 100,100

flower = Actor("flower")
flower.pos = 200,200

def draw():
    screen.blit("bg", (0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score: " + str(score), color = "black" , topleft = (10,10))

    if gameOver:
        screen.fill("red")
        screen.draw.text("Time is up, your final score is: " + str(score), midtop = (WIDTH/2, 10), fontsize = 40, color = "white")

    
def place_flower():
        flower.x = randint(70,(WIDTH-70))
        flower.y = randint(70, (HEIGHT-70))

def timeup():
    global gameOver
    gameover = True
    
def update():
        global score

        if keyboard.a:
            bee.x -= 2
        if keyboard.d:
            bee.x += 2
        if keyboard.w:
            bee.y -= 2
        if keyboard.s:
            bee.y += 2

        flowerCollected = bee.colliderect(flower)
        if flowerCollected:
            score += 10
            place_flower()

clock.schedule(clock, timeup , 0)      


pgzrun.go()