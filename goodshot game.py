import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import pgzrun
import pgzero.screen
import pgzero.actor
import pgzero.rect

screen: pgzero.screen.Screen
Actor = pgzero.actor.Actor
Rect = pgzero.rect.Rect

from random import randint

TITLE = "Good Shot"
WIDTH = 500
HEIGHT = 500
message = ""
count = 0
alien = Actor("alien")
alien.pos = 50,50

def draw():
    screen.clear()
    screen.fill(color = (100,0,100))
    place_alien()
    alien.draw()
    screen.draw.text(message + " " + str(count) if count !=0 else message +"", center = (400,10), fontsize = 30)


def place_alien():
    alien.x = randint(50, WIDTH-50)
    alien.y = randint(50, HEIGHT-50)

def on_mouse_down(pos):
    global message, count

    if alien.collidepoint(pos):
        message = "Good Shot"
        count+=1
        place_alien()
    else:
        message = "You missed"
    
place_alien()

pgzrun.go()