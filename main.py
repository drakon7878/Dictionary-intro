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
import random
import time

screen: pgzero.screen.Screen
Actor = pgzero.actor.Actor
Rect = pgzero.rect.Rect
keyboard: pgzero.keyboard.Keyboard
clock: pgzero.clock.Clock

WIDTH = 700
HEIGHT = 700
TITLE = "Pokemon"
score = 0
gameOver = False

player = Actor("player")
player.pos = 667 , 533

pokeball = Actor("pokeball")
pokeball.pos = player.pos

pikachu = Actor("pikachu")
pikachu.pos = 200,200 
text = ""
def changeText():
    global text
    text = ""

pokeballCount = 10


def draw():
    screen.blit("bg", (0,0))
    pikachu.draw()    
    pokeball.draw()
    player.draw()
    screen.draw.text("Your score is: " + str(score), color= "black" , topright = (WIDTH - 10 , 10))
    screen.draw.text(text , fontsize = 50 , center = (350,350), color = "black" )
    screen.draw.text("Pokeballs: " + str(pokeballCount), color= "black" , topright = (WIDTH - 10 , 25))
    
def placePikachu():
    pikachu.x = random.randint( 308 , WIDTH )
    pikachu.y = random.randint(142 , HEIGHT)

def on_mouse_down(pos):
    if pokeballCount > 0:
        if player.distance_to(pos) <= 150:
            pokeball.pos = pos
        else:
            pokeball.pos = player.pos

def update():
    global score,  text , pokeballCount
    if (keyboard.a and keyboard.w) or (keyboard.a and keyboard.s) or (keyboard.d and keyboard.w) or (keyboard.d and keyboard.s):
        player.pos = player.pos

    else:
        if keyboard.a:
            player.x -= 5
            pokeball.pos = player.pos
        if keyboard.d:
            player.x +=5
            pokeball.pos = player.pos
        if keyboard.w:
            player.y -= 5
            pokeball.pos = player.pos
        if keyboard.s:
            player.y += 5
            pokeball.pos = player.pos

    if player.colliderect(pikachu) == False:
        pokeballHit = pokeball.colliderect(pikachu)
        if pokeballHit:
            chance = random.randint(1,3)
            if chance == 1:
                score+=1
                placePikachu()
            else:
                text = "Pkachu was not caught"
                pokeball.pos = player.pos
                pokeballCount -=1
                clock.schedule(changeText , 2.0)

        if pokeballCount == 0:
            text = "Game Over" 
            
    

pgzrun.go()