import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import pgzrun
import pgzero.screen
import pgzero.actor
import pgzero.rect
import pgzero.keyboard
import pgzero.clock
from random import randint
from time import time

screen: pgzero.screen.Screen
Actor = pgzero.actor.Actor
Rect = pgzero.rect.Rect
keyboard: pgzero.keyboard.Keyboard
clock = pgzero.clock.Clock

WIDTH = 800
HEIGHT= 600

satellites = []
lines = []

next_satellite = -1

start_time = 0
total_time = 0
end_time = 0

noOfSatellites = 8

def createSatellites():
    global start_time

    for count in range(0, noOfSatellites):
        satellite = Actor("satellite")
        satellite.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)

        satellites.append(satellite)

        start_time = time()

def draw():
    global total_time
    screen.blit("bg", (0,0))
    number =  1
    for satellite in satellites:
        screen.draw.text(str(number), (satellite.pos[0], satellite.pos[1]+20))

        satellite.draw()
        number+=1

    for line in lines:
        screen.draw.line(line[0], line[1], "#ffffff" )
    
    if next_satellite < noOfSatellites:
        total_time = time()-start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)

def update():
    pass

def on_mouse_down(pos):
    global lines, next_satellite

    if next_satellite < noOfSatellites:
        if satellites[next_satellite].collidepoint(pos):
            lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
            next_satellite += 1

    else:
        lines = []
        next_satellite = 0



createSatellites()

pgzrun.go()

