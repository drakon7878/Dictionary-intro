import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import time

import pygame
pygame.mixer.init()
pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Birthday Card")

bgSong = pygame.mixer.music.load("H:/Coding/Jetlearn Python Lessons/python Game development/pygame/birthdayCard/sounds/mainSound.mp3")

character = pygame.image.load("H:/Coding/Jetlearn Python Lessons/python Game development/pygame/birthdayCard/images/Character.png")
charSprite = character.get_rect()
charSprite.center = (400,400)

bg1 = pygame.image.load("H:/Coding/Jetlearn Python Lessons/python Game development/pygame/birthdayCard/images/bg1.png")
bg1 = pygame.transform.scale(bg1 , (800,800))
bg2  = pygame.image.load("H:/Coding/Jetlearn Python Lessons/python Game development/pygame/birthdayCard/images/bg2.png")
bg2 = pygame.transform.scale(bg2 , (800,800))
bg3 = pygame.image.load("H:/Coding/Jetlearn Python Lessons/python Game development/pygame/birthdayCard/images/bg3.png")
bg3 = pygame.transform.scale(bg3 , (800,800))
bg4 = pygame.image.load("H:/Coding/Jetlearn Python Lessons/python Game development/pygame/birthdayCard/images/bg4.png")
bg4 = pygame.transform.scale(bg4 , (800,800))
bg5 = pygame.image.load("H:/Coding/Jetlearn Python Lessons/python Game development/pygame/birthdayCard/images/bg5.png")
bg5 = pygame.transform.scale(bg5 , (800,800))
bgList = [bg1 , bg2 , bg3 , bg4, bg5 ]

running = True
def draw():
    screen.blit(bg1 , (0,0))
    time.sleep(2)
    screen.blit(character , charSprite)
    pygame.display.update()
    screen.fill("Black")
    screen.blit(bg2 , (0,0))
    time.sleep(2)
    screen.blit(character , charSprite)
    pygame.display.update()
    screen.fill("Black")
    screen.blit(bg3 , (0,0))
    time.sleep(2)
    screen.blit(character , charSprite)
    pygame.display.update()
    screen.fill("Black")
    screen.blit(bg4 , (0,0))
    time.sleep(2)
    screen.blit(character , charSprite)
    pygame.display.update()
    screen.fill("Black")
    screen.blit(bg5 , (0,0))
    time.sleep(2)
    screen.blit(character , charSprite)
    pygame.display.update()

pygame.mixer.music.play(-1)

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.mixer.music.stop()
            running = False
    
    
    for bg in bgList:
        screen.blit(bg , (0,0))
        time.sleep(2)
        screen.blit(character , charSprite)
        myfont = pygame.font.SysFont("Times New Roman" , 50 )
        text = myfont.render("Happy Birthday" , True , "blue")
        screen.blit(text , ( 400 , 0))
        pygame.display.update()
        screen.fill("Black")

    
pygame.quit()
