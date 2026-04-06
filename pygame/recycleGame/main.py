import pygame

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Basics")
run = True

bg = pygame.image.load("python Game development/pygame/basic/images/recycleBg.png").convert_alpha()
bg = pygame.transform.scale(bg , (800,800))
greenBin = pygame.image.load("python Game development/pygame/basic/images/green_dustbin.png").convert_alpha()
redBin = pygame.image.load("python Game development/pygame/basic/images/red_dustbin.png").convert_alpha()
greenBin = pygame.transform.scale(greenBin , (200,200))

battery = pygame.image.load("python Game development/pygame/basic/images/battery.png").convert_alpha()
chipsPacket = pygame.image.load("python Game development/pygame/basic/images/chipsPacket.png").convert_alpha()
paper = pygame.image.load("python Game development/pygame/basic/images/paper.png").convert_alpha()
paperBag = pygame.image.load("python Game development/pygame/basic/images/paperBag.png").convert_alpha()
plasticBottle = pygame.image.load("python Game development/pygame/basic/images/plasticBottle.png").convert_alpha()

battery = pygame.transform.scale(battery , (100,100))
chipsPacket = pygame.transform.scale(chipsPacket , (100,100))
paper = pygame.transform.scale(paper , (100,100))
paperBag = pygame.transform.scale(paperBag , (100,100))
plasticBottle = pygame.transform.scale(plasticBottle , (100,100))

greenBinSprite = greenBin.get_rect()
greenBinSprite.center = (150,600)
redBinSprite = redBin.get_rect()
redBinSprite.center = (650,600)

batterySprite = battery.get_rect()
chipsPacketSprite = chipsPacket.get_rect()
paperSprite = paper.get_rect()
paperBagSprite = paperBag.get_rect()
plasticBottleSprite = plasticBottle.get_rect()

batterySprite.center = (250 , 150)
chipsPacketSprite.center = (370 , 150)
paperSprite.center = (490,150)
paperBagSprite.center = (610, 150)
plasticBottleSprite.center = (730,150)


while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    
    screen.blit(bg , (0,0))
    screen.blit(greenBin , greenBinSprite)
    screen.blit(redBin , redBinSprite)
    screen.blit(battery , batterySprite)
    screen.blit(chipsPacket , chipsPacketSprite)
    screen.blit(paper , paperSprite)
    screen.blit(paperBag , paperBagSprite)
    screen.blit(plasticBottle , plasticBottleSprite)    
    pygame.display.update()

pygame.quit()
