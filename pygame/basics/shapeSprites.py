import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Sprites")
running = True

triVertex1 = [(100,100) , (200,200) , (0,200)]
pentVertex1 = [(400,400) , (500 , 550) , (450 , 700) , (350 , 700) , (300,550)]

rect1x , rect1y = 350 , 350
circle2x , circle2y = 600,400

def draw():
    global rect1y , rect1x , circle2y , circle2x
    screen.fill("black")
    rect1 = pygame.draw.rect(screen , "White" , (rect1x , rect1y , 50 , 50 ))
    rect2 = pygame.draw.rect(screen , "Blue" , (500 , 500 , 100 , 80))
    circle1 = pygame.draw.circle(screen , "red" , (100,100) , 30)
    circle2 = pygame.draw.circle(screen , "green" , (circle2x , circle2y) , 80)
    tri1 = pygame.draw.polygon(screen , "yellow" , triVertex1)
    pent1 = pygame.draw.polygon(screen , "light blue" , pentVertex1)

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:
        rect1x -= 5
    if keys[pygame.K_RIGHT]:
        rect1x += 5
    if keys[pygame.K_UP]:
        rect1y -= 5
    if keys[pygame.K_DOWN]:
        rect1y += 5
    if keys[pygame.K_a]:
        circle2x -= 5
    if keys[pygame.K_d]:
        circle2x += 5
    if keys[pygame.K_w]:
        circle2y -= 5
    if keys[pygame.K_s]:
        circle2y += 5
    draw()
    pygame.display.update()

pygame.quit()
