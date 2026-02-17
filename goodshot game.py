import pgzero
from random import randint

title = "Good Shot"
WIDTH = 500
HEIGHT = 500
message = ""
alien = pgzero.actor('alien')
alien.pos = 50,50

def draw():
    pgzero.screen.clear()
    pgzero.screen.fill(color = (100,0,100))
    place_alien()
    alien.draw()
    pgzero.screen.draw.text(message, centre = (400,10), fontsize = 30)


def place_alien():
    alien.x = randint(50, WIDTH-50)
    alien.y = randint(50, HEIGHT-50)

def on_mouse_down(pos):
    global message

    if alien.collidepoint(pos):
        message = "Good Shot"
        place_alien()
    else:
        message = "You missed"
    
place_alien()

pgzero.runner()