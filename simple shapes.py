import pgzrun
import pgzero.screen
import pgzero.actor
import pgzero.rect
from random import randint



screen: pgzero.screen.Screen
Actor  = pgzero.actor.Actor
Rect = pgzero.rect.Rect

WIDTH = 300
HEIGHT = 300

def draw():
    r = 255
    g = 0
    b = randint(100,255)
    width = WIDTH
    height = HEIGHT-200


    for i in range(20):
        rect = Rect(0,150,width, height)
        rect.center = 150,150
        screen.draw.rect(rect=rect , color=(r,g,b))
        
        r -=10
        g+=10
        width-=10
        height+=10
        screen.draw.rect(rect=rect , color=(r,g,b))

pgzrun.go()   
