import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    r = 255
    g = 0
    b = randint(100,255)
    width = WIDTH
    height = HEIGHT-200


    for i in range(20):
        rect = pgzrun.Rect((0,0), (width , height))
        rect.center = 150,150
        pgzrun.screen.draw.rect(rect(r,g,b))
        
        r -=10
        g+=10
        width-=10
        height+=10
        pgzrun.screen.draw.filled_rect(rect(r,g,b))

pgzrun.go()   
