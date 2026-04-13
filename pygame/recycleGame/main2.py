import pygame

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Basics")
running = True
isdragging = False

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

objs = [batterySprite , chipsPacketSprite , paperSprite , paperBagSprite , plasticBottleSprite]
hiddenObj = [False, False, False, False, False]
green = [paperSprite , paperBagSprite]
red = [batterySprite , chipsPacketSprite , plasticBottleSprite ]




while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            isdragging = True
        elif e.type == pygame.MOUSEBUTTONUP:
            isdragging = False

        if isdragging:
            if pygame.MOUSEMOTION:
                for o in objs:
                    if o.collidepoint(pygame.mouse.get_pos()):
                        o.center = e.pos
        
        for i in range(len(objs)):
            for j in range(len(objs)):
                if i != j:
                    if objs[i].colliderect(objs[j]):
                        overlapX = min(objs[i].right , objs[j].right) - max(objs[i].left , objs[j].left)
                        overlapY = min(objs[i].bottom , objs[j].bottom) - max(objs[i].top , objs[j].top)
                        if overlapX < overlapY:
                            if objs[i].centerx < objs[j].centerx:
                                objs[i].centerx -= overlapX
                            else:
                                objs[i].centerx += overlapX
                        else:
                            if objs[i].centery < objs[j].centery:
                                objs[i].centery -= overlapY
                            else:
                                objs[i].centery += overlapY         
        for i in objs:
            if i.centerx - 50 <= 0:
                i.centerx = 50 
            elif i.centerx + 50 >= 800:
                i.centerx = 750
            elif i.centery - 50 <= 0:
                i.centery = 50
            elif i.centery + 50 >= 800:
                i.centery = 750
        
        for i in green:
            if i.colliderect(greenBinSprite):
                for j in range(len(objs)):
                    if objs[j] == i:
                        hiddenObj[j] = True
        for i in red:
            if i.colliderect(redBinSprite):
                for j in range(len(objs)):
                    if objs[j] == i:
                        hiddenObj[j] = True
        batteryHidden = hiddenObj[0]
        chipsPacketHidden = hiddenObj[1]
        paperHidden = hiddenObj[2]
        paperBagHidden = hiddenObj[3]
        plasticBottleHidden = hiddenObj[4]
    if (hiddenObj[0] == True) and (hiddenObj[1] == True) and (hiddenObj[2] == True) and (hiddenObj[3] == True) and (hiddenObj[4] == True) :
        batterySprite.center = (250 , 150)
        chipsPacketSprite.center = (370 , 150)
        paperSprite.center = (490,150)
        paperBagSprite.center = (610, 150)
        plasticBottleSprite.center = (730,150)
        hiddenObj[0] = False
        hiddenObj[1] = False
        hiddenObj[2] = False
        hiddenObj[3] = False
        hiddenObj[4] = False
    print(hiddenObj)
      
    screen.blit(bg , (0,0))
    screen.blit(greenBin , greenBinSprite)
    screen.blit(redBin , redBinSprite)
    if batteryHidden == False:
        screen.blit(battery , batterySprite)
    if chipsPacketHidden == False:
        screen.blit(chipsPacket , chipsPacketSprite)
    if paperHidden == False:
        screen.blit(paper , paperSprite)
    if paperBagHidden == False:
        screen.blit(paperBag , paperBagSprite)
    if plasticBottleHidden == False:
        screen.blit(plasticBottle , plasticBottleSprite)    
    pygame.display.update()

pygame.quit()
