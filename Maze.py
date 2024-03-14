import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

x= 75
y= 470

clock = pygame.time.Clock()

Font = pygame.font.SysFont("comicsansms", 40, True, True)

TutFont = pygame.font.SysFont("comicsansms", 30, True, True)

Title = Font.render("Touch the exit sign to win!!", True, (255, 255, 255))

WinTitle = Font.render("Congrats :))", True, (255, 255, 255))

Level1Text = Font.render("Level 1", True, (0, 0, 255))

Level2Text = Font.render("Level 2", True, (0, 0, 255))

Level3Text = Font.render("Level 3", True, (0, 0, 255))

Tutorial = TutFont.render("Press the wasd keys to move around", True, (128, 128, 128))

flag = 0

ButtonSwitch = 0

def level1():
    global x
    global y
    global flag
    global Font
    global TutFont
    global Title
    global Tutorial
    global WinTitle
    global Level1Text

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]: y -=3
    if pressed[pygame.K_s]: y += 3
    if pressed[pygame.K_a]: x -= 3
    if pressed[pygame.K_d]: x += 3

    screen1 = screen.fill((0, 0, 0))

    #screen.blit(Title, (200, 50))

    screen.blit(Level1Text, (350, 550))

    screen.blit(Tutorial, (50, 375))

    path1 = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(50, 450, 650, 100))
    path2 = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(600, 150, 100, 300))
    path3 = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(400, 150, 200, 100))
    path4 = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(400, 250, 100, 100))
    path5 = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(100, 250, 400, 100))
    path6 = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(100, 50, 100, 300))

    #winblock = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 50, 100, 75))

    imp1 = pygame.image.load("Exit.png").convert()
    winblock = imp1.get_rect()
    winblock.topleft = (100, 50)
    pygame.draw.rect(screen, (162, 0, 255), winblock)
    screen.blit(imp1, winblock)

    imp = pygame.image.load("Cube.png").convert()
    box1 = imp.get_rect()
    box1.topleft = (x, y)
    pygame.draw.rect(screen, (162, 0, 255), box1)
    screen.blit(imp, box1)

    #box1 = pygame.draw.rect(screen, (162, 0, 255), pygame.Rect(x, y, 60, 60))

    if box1.colliderect(path1) == False and box1.colliderect(path2) == False and box1.colliderect(path3) == False and box1.colliderect(path4) == False and box1.colliderect(path5) == False and box1.colliderect(path6) == False and box1.colliderect(screen1) == True:
        x = 75
        y = 470
    if box1.colliderect(winblock) == True:
        x = 75
        y = 470
        flag = 1
    elif box1.colliderect(winblock) == False and flag == 0:
        screen.blit(Title, (200, 50))
    if flag == 1:
        screen.blit(WinTitle, (200, 50))

def level2():
    global x
    global y
    global flag
    global Font
    global TutFont
    global Title
    global Tutorial
    global WinTitle
    global Level2Text

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]: y -= 3
    if pressed[pygame.K_s]: y += 3
    if pressed[pygame.K_a]: x -= 3
    if pressed[pygame.K_d]: x += 3

    screen1 = screen.fill((0, 0, 0))

    #screen.blit(Title, (200, 50))

    screen.blit(Level2Text, (350, 550))

    screen.blit(Tutorial, (50, 375))

    path1 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(50, 450, 100, 50))
    path2 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 450, 50, 75))
    path3 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 500, 200, 50))
    path4 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(250, 450, 450, 50))
    path5 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(650, 150, 50, 300))
    path6 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(550, 150, 100, 50))
    path7 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(550, 150, 50, 200))
    path8 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(350, 300, 200, 50))
    path9 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(350, 150, 50, 150))
    path10 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 150, 250, 50))

    #winblock = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(100, 100, 50, 50))

    imp1 = pygame.image.load("Exit1.png").convert()
    winblock = imp1.get_rect()
    winblock.topleft = (100, 100)
    pygame.draw.rect(screen, (162, 0, 255), winblock)
    screen.blit(imp1, winblock)

    imp = pygame.image.load("Cube.png").convert()
    box1 = imp.get_rect()
    box1.topleft = (x, y)
    pygame.draw.rect(screen, (162, 0, 255), box1)
    screen.blit(imp, box1)

    #box1 = pygame.draw.rect(screen, (162, 0, 255), pygame.Rect(x, y, 60, 60))

    if box1.colliderect(path1) == False and box1.colliderect(path2) == False and box1.colliderect(path3) == False and box1.colliderect(path4) == False and box1.colliderect(path5) == False and box1.colliderect(path6) == False and box1.colliderect(path7) == False and box1.colliderect(path8) == False and box1.colliderect(path9) == False and box1.colliderect(path10) == False and box1.colliderect(screen1) == True:
        x = 75
        y = 470
    if box1.colliderect(winblock) == True:
        x = 75
        y = 470
        flag = 2
    elif box1.colliderect(winblock) == False and flag == 1:
        screen.blit(Title, (200, 50))
    if flag == 2:
        screen.blit(WinTitle, (200, 50))

def level3():
    global x
    global y
    global flag
    global Font
    global TutFont
    global Title
    global Tutorial
    global WinTitle
    global Level3Text
    global ButtonSwitch



    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]: y -= 3
    if pressed[pygame.K_s]: y += 3
    if pressed[pygame.K_a]: x -= 3
    if pressed[pygame.K_d]: x += 3

    screen1 = screen.fill((0, 0, 0))

    #screen.blit(Title, (200, 50))

    screen.blit(Level3Text, (350, 550))

    screen.blit(Tutorial, (50, 375))

    path1 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(50, 450, 80, 30))
    path2 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(100, 450, 30, 50))
    path3 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(100, 500, 600, 30))
    path4 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(670, 300, 30, 150))
    path5 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(130, 300, 500, 30))

    WinButton = pygame.draw.rect(screen, (162, 0, 255), pygame.Rect(100, 300, 30, 30))

    # winblock = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(100, 100, 30, 30))

    if ButtonSwitch == 1:
        path6 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(600, 100, 30, 150))
        path7 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(150, 100, 400, 30))



    imp1 = pygame.image.load("Exit2.png").convert()
    winblock = imp1.get_rect()
    winblock.topleft = (100, 100)
    pygame.draw.rect(screen, (162, 0, 255), winblock)
    screen.blit(imp1, winblock)

    imp = pygame.image.load("Cube.png").convert()
    box1 = imp.get_rect()
    box1.topleft=(x,y)
    pygame.draw.rect(screen, (162, 0, 255),box1)
    screen.blit(imp,box1)

    #box1 = pygame.draw.rect(screen, (162, 0, 255), pygame.Rect(x, y, 60, 60))

    if box1.colliderect(WinButton) == True:
        ButtonSwitch = 1


#NEED TO ADD A LEVER TO MAKE PATH6 AND PATH7 SHOW UP AND BE USEABLE


    if box1.colliderect(path1) == False and box1.colliderect(path2) == False and box1.colliderect(path3) == False and box1.colliderect(path4) == False and box1.colliderect(path5) == False and box1.colliderect(path6) == False and box1.colliderect(path7) == False and box1.colliderect(WinButton) == False and box1.colliderect(screen1) == True:
        x = 75
        y = 470
    if box1.colliderect(winblock) == True:
        x = 75
        y = 470
        flag = 3
    elif box1.colliderect(winblock) == False and flag == 2:
        screen.blit(Title, (200, 50))
    if flag == 3:
        screen.blit(WinTitle, (200, 50))
        imp1 = pygame.image.load("YouWin!.png").convert()
        winblock = imp1.get_rect()
        winblock.topleft = (0, 0)
        pygame.draw.rect(screen, (162, 0, 255), winblock)
        screen.blit(imp1, winblock)


while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if flag == 0:
        level1()
    if flag == 1:
        level2()
    if flag == 2:
        level3()
    if flag == 3:
        imp1 = pygame.image.load("YouWin!.png").convert()
        winblock = imp1.get_rect()
        winblock.topleft = (0, 0)
        pygame.draw.rect(screen, (162, 0, 255), winblock)
        screen.blit(imp1, winblock)

    pygame.display.flip()
    clock.tick(60)
