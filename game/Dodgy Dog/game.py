from asyncio.windows_events import NULL
from random import randint

bombposx = randint(0, 450)
import pygame
pygame.display.set_caption('Dodgy Dog')
img = pygame.image.load('background.png')
dog = pygame.image.load('dog.png')
dog2 = pygame.image.load('dog2.png')
bomb = pygame.image.load('bomb.png')
bomb2 = pygame.image.load('bomb.png')
bomb3 = pygame.image.load('bomb.png')
bomb4 = pygame.image.load('bomb.png')
bomb5 = pygame.image.load('bomb.png')
white = (255, 64, 64)
w = 500
h = 665
posx = 250
dogc = dog
score = 0
bombamo = 0
bombnum = 0
bombpos = 0
bombspeed = 0.3
screen = pygame.display.set_mode((w, h))
screen.fill((white))
running = 1
pygame.event.pump()
bombposx1 = randint(0, 450)
bombhit1 = pygame.Rect(bombposx1, bombpos, 50, 75)
bombposx2 = randint(0, 450)
bombhit2 = pygame.Rect(bombposx2, bombpos, 50, 75)
bombposx3 = randint(0, 450)
bombhit3 = pygame.Rect(bombposx3, bombpos, 50, 75)
bombposx4 = randint(0, 450)
bombhit4 = pygame.Rect(bombposx4, bombpos, 50, 75)
wallleft = pygame.Rect(0, 615, 1, 50)
wallright = pygame.Rect(400, 615, 1, 50)
dogbox = pygame.Rect(posx, 620, 90, 30)
bombhit = pygame.Rect(bombposx, bombpos, 50, 75)
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
    screen.fill((white))
    screen.blit(img,(0,0))
    screen.blit(bomb,(bombposx,bombpos))
    if bombamo >= 1:
        screen.blit(bomb2,(bombposx1,bombpos))
        if chill_over(bombhit1, dogbox):
            print("Highscore:", score)
            running = False

    if bombamo >= 2:
        screen.blit(bomb3,(bombposx2,bombpos))
        if chill_over(bombhit2, dogbox):
            print("Highscore:", score)
            running = False

    if bombamo >= 3:
        screen.blit(bomb4,(bombposx3,bombpos))
        if chill_over(bombhit3, dogbox):
            print("Highscore:", score)
            running = False

    if bombamo >= 4:
        screen.blit(bomb5,(bombposx4,bombpos))
        if chill_over(bombhit4, dogbox):
            print("Highscore:", score)
            running = False


    bombhit1 = pygame.Rect(bombposx1, bombpos, 50, 75)
    bombhit2 = pygame.Rect(bombposx2, bombpos, 50, 75)
    bombhit3 = pygame.Rect(bombposx3, bombpos, 50, 75)
    bombhit4 = pygame.Rect(bombposx4, bombpos, 50, 75)    
    bombhit = pygame.Rect(bombposx, bombpos, 50, 75)
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
        

    M = pygame.mouse.get_pos()
    screen.blit(dogc,(posx,610))
    dogbox = pygame.Rect(posx, 620, 90, 50)
    if chill_over(bombhit, dogbox):
        print("Highscore:", score)
        running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        if is_over(wallleft, dogbox):
            NULL
        else:
            posx = posx + -0.3
            dogc = dog2
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        if is_over(wallright, dogbox):
            NULL
        else:
            posx = posx + 0.3
            dogc = dog
    pygame.display.flip()
#