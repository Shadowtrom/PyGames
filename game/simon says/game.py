import pygame, time
from random import randint
pygame.mixer.init()
bluewav = pygame.mixer.Sound('blue.wav')
redwav = pygame.mixer.Sound('red.wav')
greenwav = pygame.mixer.Sound('green.wav')
yellowwav = pygame.mixer.Sound('yellow.wav')
background_colour = (255,255,255)
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('simon says')
pygame.draw.rect(screen, (0, 200, 0), (0, 0, 250, 250))
pygame.draw.rect(screen, (0, 0, 200), (250, 250, 250, 250))
pygame.draw.rect(screen, (200, 0, 0), (250, 0, 250, 250))
pygame.draw.rect(screen, (200, 200, 0), (0, 250, 250, 250))
clicked = 0
helping = 'true'
helpnum = 0
pro = 0
promax = 1
helppro = 0
speed = 1
code = str(randint(1, 4))
next = code[0]
pygame.display.flip()
def colorres():
  pygame.draw.rect(screen, (0, 200, 0), (0, 0, 250, 250))
  pygame.draw.rect(screen, (0, 0, 200), (250, 250, 250, 250))
  pygame.draw.rect(screen, (200, 0, 0), (250, 0, 250, 250))
  pygame.draw.rect(screen, (200, 200, 0), (0, 250, 250, 250))
  return


def is_over(rect, pos):
  return True if rect.collidepoint(pos[0], pos[1]) else False
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
    
  
  hitboxred = pygame.Rect(250, 0, 250, 250)
  hitboxgreen = pygame.Rect(0, 0, 250, 250)
  hitboxblue = pygame.Rect(250, 250, 250, 250)
  hitboxyellow = pygame.Rect(0, 250, 250, 250)
  M = pygame.mouse.get_pos()
  next = code[pro]

  #screen.fill(background_colour)

  colorres()


  #if not clicking
  if event.type != pygame.MOUSEBUTTONDOWN:
    clicked = 0
  #if red clicked
  if event.type == pygame.MOUSEBUTTONDOWN:
    if helping == 'false':
      if is_over(hitboxred, M):
        if clicked == 0:
          if next == '1':
            clicked = 1
            #print('good')
            pro = pro + 1
            code = code + str(randint(1, 4))
            next = code[pro]
            pygame.draw.rect(screen, (0, 0, 0), (250, 0, 250, 250))
            pygame.display.flip()
            redwav.play()
            time.sleep(0.25)
            colorres()
            if promax == pro:
              helping = 'true'
              promax = promax + 1
              pro = 0
              time.sleep(0.05)
          else:
            print('high score:', promax)
            running = False
  
  if event.type == pygame.MOUSEBUTTONDOWN:
    if helping == 'false':
      if is_over(hitboxgreen, M):
        if clicked == 0:
          if next == '2':
            clicked = 1
            #print('good')
            pro = pro + 1
            code = code + str(randint(1, 4))
            next = code[pro]
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, 250, 250))
            pygame.display.flip()
            greenwav.play()
            time.sleep(0.25)
            colorres()
            if promax == pro:
              helping = 'true'
              promax = promax + 1
              pro = 0
              time.sleep(0.05)
          else:
            print('high score:', promax)
            running = False

  if event.type == pygame.MOUSEBUTTONDOWN:
    if helping == 'false':
      if is_over(hitboxyellow, M):
        if clicked == 0:
          if next == '3':
            clicked = 1
            #print('good')
            pro = pro + 1
            code = code + str(randint(1, 4))
            next = code[pro]
            pygame.draw.rect(screen, (0, 0, 0), (0, 250, 250, 250))
            pygame.display.flip()
            yellowwav.play()
            time.sleep(0.25)
            colorres()
            if promax == pro:
              helping = 'true'
              promax = promax + 1
              pro = 0
              time.sleep(0.05)
          else:
            print('high score:', promax)
            running = False

  if event.type == pygame.MOUSEBUTTONDOWN:
    if helping == 'false':
      if is_over(hitboxblue, M):
        if clicked == 0:
          if next == '4':
            clicked = 1
            #print('good')
            pro = pro + 1
            code = code + str(randint(1, 4))
            next = code[pro]
            pygame.draw.rect(screen, (0, 0, 0), (250, 250, 250, 250))
            pygame.display.flip()
            bluewav.play()
            time.sleep(0.25)
            colorres()
            if promax == pro:
              helping = 'true'
              promax = promax + 1
              pro = 0
              time.sleep(0.05)
          else:
            print('high score:', promax)
            running = False
  
  
  if helping == 'true':
    
    if helpnum == 0:
      if helppro < promax:
        helpnum = code[helppro]
      else:
        helppro = 0
        helping = 'false'
        speed = speed - 0.075
        print('-')

      if speed <= 0:
        speed = 0.0005

  if helping == 'true':
    if int(helpnum) == 1:
      helppro = int(helppro) + 1
      helpnum = 0
      pygame.draw.rect(screen, (255, 255, 255), (250, 0, 250, 250))
      pygame.display.flip()
      redwav.play()
      print('red')
      time.sleep(speed)
      colorres()
      pygame.display.flip()
      time.sleep(0.2)
    if int(helpnum) == 2:
      helpnum = 0
      helppro = int(helppro) + 1
      pygame.draw.rect(screen, (255, 255, 255), (0, 0, 250, 250))
      pygame.display.flip()
      greenwav.play()
      print('green')
      time.sleep(speed)
      colorres()
      pygame.display.flip()
      time.sleep(0.2)
    if int(helpnum) == 3:
      helpnum = 0
      helppro = int(helppro) + 1
      pygame.draw.rect(screen, (255, 255, 255), (0, 250, 250, 250))
      pygame.display.flip()
      yellowwav.play()
      print('yellow')
      time.sleep(speed)
      colorres()
      pygame.display.flip()
      time.sleep(0.2)
    if int(helpnum) == 4:
      helpnum = 0
      helppro = int(helppro) + 1
      pygame.draw.rect(screen, (255, 255, 255), (250, 250, 250, 250))
      pygame.display.flip()
      bluewav.play()
      print('blue')
      time.sleep(speed)
      colorres()
      pygame.display.flip()
      time.sleep(0.2)




#num 1 is red
#num 2 is green
#num 3 is yellow
#num 4 is blue

  pygame.display.flip()

pygame.quit()
