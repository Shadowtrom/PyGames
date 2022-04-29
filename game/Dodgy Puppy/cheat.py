from asyncio.windows_events import NULL
from asyncore import loop
from random import randint
bombposx = randint(0, 450)
import pygame, sys
pygame.font.init()
pygame.display.set_caption('Dodgy Puppy')
img = pygame.image.load('background.png')
dog = pygame.image.load('dog.png')
dog2 = pygame.image.load('dog2.png')
bomb = pygame.image.load('bomb.png')
bomb2 = pygame.image.load('bomb.png')
bomb3 = pygame.image.load('bomb.png')
bomb4 = pygame.image.load('bomb.png')
bomb5 = pygame.image.load('bomb.png')
myfont = pygame.font.SysFont('Impact', 35)
font = pygame.font.SysFont('Impact', 25)
hitbox = False
GodMode = False
bombamo = 0
bombspeed = 0.3
speed = 0.3
Ds = font.render(("Bombspeed q and e: " + str(round(speed, 2))), False, (0, 0, 0))
Bs = font.render(("Bombspeed shift and ctrl: " + str(round(bombspeed, 2))), False, (0, 0, 0))
Ba = font.render(("Bomb ammo 'any number': " + str(bombamo + 1)), False, (0, 0, 0))
Gm = font.render(("Godmode G: " + str(GodMode)), False, (0, 0, 0))
Hb = font.render(("Hitbox B: " + str(hitbox)), False, (0, 0, 0))
cheat = myfont.render("Cheat enabled, press 'T' to disable", False, (0, 0, 0))
white = (255, 64, 64)
w = 500
h = 665
pressedCtrl = 0
pressedShift = 0
posx = 250
dogc = dog
score = 0
stage = 0
bombnum = 0
bombpos = 0
Hide = 0
pressedZ = 0
pressedH = 0
pressedF = 0
pressedE = 0 
pressedQ = 0 
pressedG = 0
pressedB = 0
pressedT = 0
screen = pygame.display.set_mode((w, h))
screen.fill((white))
running = 1
pygame.event.pump()
bombposx1 = randint(0, 450)
bombhit1 = pygame.Rect(bombposx1, bombpos, 35, 55)
bombposx2 = randint(0, 450)
bombhit2 = pygame.Rect(bombposx2, bombpos, 35, 55)
bombposx3 = randint(0, 450)
bombhit3 = pygame.Rect(bombposx3, bombpos, 35, 55)
bombposx4 = randint(0, 450)
bombhit4 = pygame.Rect(bombposx4, bombpos, 35, 55)
wallleft = pygame.Rect(0, 615, 1, 50)
wallright = pygame.Rect(500, 615, 1, 50)
dogbox = pygame.Rect(posx, 630, 60, 40)
bombhit = pygame.Rect(bombposx, bombpos, 35, 55)
def chill_over(rect1, rect2):
    collide = rect1.colliderect(rect2)
    return True if collide else False
def is_over(rect, pos):
  return True if rect.collidepoint(pos[0], pos[1]) else False
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Highscore:", score)
            running = False
    #text updater
    Bs = font.render(("Bombspeed shift and ctrl: " + str(round(bombspeed, 2))), False, (0, 0, 0))
    Hb = font.render(("Hitbox B: " + str(hitbox)), False, (0, 0, 0))
    Gm = font.render(("Godmode G: " + str(GodMode)), False, (0, 0, 0))
    Ba = font.render(("Bomb ammo '1-5': " + str(bombamo + 1)), False, (0, 0, 0))
    Ds = font.render(("Bombspeed q and e: " + str(round(speed, 2))), False, (0, 0, 0))

    screen.fill((white))
    screen.blit(img,(0,0))
    screen.blit(bomb,(bombposx,bombpos))
    if bombamo >= 1:
        screen.blit(bomb2,(bombposx1,bombpos))
        if GodMode == False:
            if chill_over(bombhit1, dogbox):
                print("Highscore:", score)
                running = False
    if bombamo >= 2:
        screen.blit(bomb3,(bombposx2,bombpos))
        if GodMode == False:
            if chill_over(bombhit2, dogbox):
                print("Highscore:", score)
                running = False
    if bombamo >= 3:
        screen.blit(bomb4,(bombposx3,bombpos))
        if GodMode == False:
            if chill_over(bombhit3, dogbox):
                print("Highscore:", score)
                running = False
    if bombamo >= 4:
        screen.blit(bomb5,(bombposx4,bombpos))
        if GodMode == False:
            if chill_over(bombhit4, dogbox):
                print("Highscore:", score)
                running = False


    bombhit1 = pygame.Rect(bombposx1, bombpos, 35, 55)
    bombhit2 = pygame.Rect(bombposx2, bombpos, 35, 55)
    bombhit3 = pygame.Rect(bombposx3, bombpos, 35, 55)
    bombhit4 = pygame.Rect(bombposx4, bombpos, 35, 55)    
    bombhit = pygame.Rect(bombposx, bombpos, 35, 55)


    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        if chill_over(wallleft, dogbox):
            NULL
        else:
            posx = posx - speed
            dogc = dog2
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        if chill_over(wallright, dogbox):
            NULL
        else:
            posx = posx + speed
            dogc = dog
    
    if bombpos <= 675: 
        bombpos = bombpos + bombspeed
    else:
        bombpos = 0
        bombposx = randint(0, 450)
        bombposx1 = randint(0, 450)
        bombnum = bombnum + 0.2
        score = score + 1

    if bombnum >= 1:
        bombnum = 0
        if bombamo <= 4:
            bombamo = bombamo + 1 
        else:
            bombspeed = bombspeed + 0.1
        
    screen.blit(dogc,(posx,630))
    if stage == 1:
        if Hide == 0:
            screen.blit(cheat,(0,0))
            screen.blit(Hb,(0,50))
            screen.blit(Gm,(0,75))
            screen.blit(Ba,(0,100))
            screen.blit(Bs,(0,125))
            screen.blit(Ds,(0,150))
        if hitbox == True:
            pygame.draw.rect(screen, (0, 0, 0), (dogbox))
            pygame.draw.rect(screen, (50, 0, 0), (bombhit))
            if bombamo >= 1:
                pygame.draw.rect(screen, (100, 0, 0), (bombhit1))
            if bombamo >= 2:
                pygame.draw.rect(screen, (150, 0, 0), (bombhit2))
            if bombamo >= 3:
                pygame.draw.rect(screen, (200, 0, 0), (bombhit3))
            if bombamo >= 4:
                pygame.draw.rect(screen, (255, 0, 0), (bombhit4))

    if stage == 1:
        key = pygame.key.get_pressed()
        if key[pygame.K_LSHIFT]:
            if pressedShift == 0:
                bombspeed = bombspeed + 0.05
                pressedShift = 1

    if stage == 1:
        key = pygame.key.get_pressed()
        if key[pygame.K_LCTRL]:
            if pressedCtrl == 0:
                if round(bombspeed, 2) != 0:
                    bombspeed = bombspeed - 0.05
                    pressedCtrl = 1

    if stage == 1:
        key = pygame.key.get_pressed()
        if key[pygame.K_e]:
            if pressedE == 0:
                if round(speed, 2) != 1.5:
                    speed = speed + 0.05
                    pressedE = 1

    if stage == 1:
        key = pygame.key.get_pressed()
        if key[pygame.K_q]:
            if pressedQ == 0:
                if round(speed, 2) != -1.5:
                    speed = speed - 0.05
                    pressedQ = 1

    if stage == 1:
        key = pygame.key.get_pressed()
        if key[pygame.K_f]:
            if pressedF == 0:
                    speed = 0.3
                    pressedF = 1



    if stage == 1:
        key = pygame.key.get_pressed()
        if key[pygame.K_g]:
            if pressedG == 0:
                if GodMode == False:
                    pressedG = 1
                    GodMode = True
                else:
                    pressedG = 1
                    GodMode = False                 

    if stage == 1:
        key = pygame.key.get_pressed()
        if key[pygame.K_z]:
            if pressedZ == 0:
                pressedZ = 1
                bombspeed = 0.3




    if stage == 1:
        key = pygame.key.get_pressed()
        if key[pygame.K_h]:
            if pressedH == 0:
                if Hide == 0:
                    pressedH = 1
                    Hide = 1
                else:
                    pressedH = 1
                    Hide = 0

    key = pygame.key.get_pressed()
    if key[pygame.K_t]:
        if pressedT == 0:
            if stage == 0:
                pressedT = 1
                stage = 1
            else:
                pressedT = 1
                stage = 0
                Hide = 0
                speed = 0.3
                bombspeed = 0.3
                bombamo = 0
                GodMode = False
                hitbox = False
    if stage == 1:
        key = pygame.key.get_pressed()
        if key[pygame.K_1]:
            bombamo = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_2]:
            bombamo = 1
        key = pygame.key.get_pressed()
        if key[pygame.K_3]:
            bombamo = 2
        key = pygame.key.get_pressed()
        if key[pygame.K_4]:
            bombamo = 3
        key = pygame.key.get_pressed()
        if key[pygame.K_5]:
            bombamo = 4
        key = pygame.key.get_pressed()
        if key[pygame.K_b]:
            if pressedB == 0:
                if hitbox == False:
                    hitbox = True
                    pressedB = 1
                else:
                    hitbox = False
                    pressedB = 1

    key = pygame.key.get_pressed()
    if key[pygame.K_b]:
        NULL
    else:
        pressedB = 0    
    
    key = pygame.key.get_pressed()
    if key[pygame.K_t]:
        NULL
    else:
        pressedT = 0  
    M = pygame.mouse.get_pos()

    key = pygame.key.get_pressed()
    if key[pygame.K_g]:
        NULL
    else:
        pressedG = 0  

    key = pygame.key.get_pressed()
    if key[pygame.K_h]:
        NULL
    else:
        pressedH = 0  


    key = pygame.key.get_pressed()
    if key[pygame.K_LSHIFT]:
        NULL
    else:
        pressedShift = 0 

    key = pygame.key.get_pressed()
    if key[pygame.K_LCTRL]:
        NULL
    else:
        pressedCtrl = 0 

    key = pygame.key.get_pressed()
    if key[pygame.K_z]:
        NULL
    else:
        pressedZ = 0 

    key = pygame.key.get_pressed()
    if key[pygame.K_f]:
        NULL
    else:
        pressedF = 0 

    key = pygame.key.get_pressed()
    if key[pygame.K_e]:
        NULL
    else:
        pressedE = 0 

    key = pygame.key.get_pressed()
    if key[pygame.K_q]:
        NULL
    else:
        pressedQ = 0 


    M = pygame.mouse.get_pos()

    M = pygame.mouse.get_pos()


    dogbox = pygame.Rect(posx, 630, 60, 40)
    if GodMode == False:
        if chill_over(bombhit, dogbox):
            print("Highscore:", score)
            running = False


    pygame.display.flip()
#