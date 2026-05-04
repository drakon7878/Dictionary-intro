import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import pygame

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Shape Sprites HW - Moving a Polygon")

hex1x , hex1y = 400 , 170
hex1Vertex = [
                    (hex1x , hex1y) , 
                    (hex1x + 150 , hex1y + 80) , 
                    (hex1x + 150 , hex1y + 235) , 
                    (hex1x , hex1y+ 312) , 
                    (hex1x - 150 , hex1y + 235) ,
                    (hex1x - 150 , hex1y + 80) 
                ]

def draw():
    global hex1Vertex
    screen.fill("Black")
    hex1 = pygame.draw.polygon(screen , "White" , hex1Vertex)
    hex1Vertex = [
                    (hex1x , hex1y) , 
                    (hex1x + 150 , hex1y + 80) , 
                    (hex1x + 150 , hex1y + 235) , 
                    (hex1x , hex1y+ 312) , 
                    (hex1x - 150 , hex1y + 235) ,
                    (hex1x - 150 , hex1y + 80) 
                ]
    
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_i]:
        hex1y -= 5
    if keys[pygame.K_k]:
        hex1y += 5
    if keys[pygame.K_j]:
        hex1x -= 5
    if keys[pygame.K_l]:
        hex1x += 5
    draw()
    pygame.display.update()

pygame.quit()
