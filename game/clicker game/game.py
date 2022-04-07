# Simple pygame program

# Import and initialize the pygame library
import pygame, math, sys, os.path
from numerize import numerize
pygame.mixer.init()
spaceimg = pygame.image.load('space.png')
upimg = pygame.image.load('upgrade.png')
wallimg = pygame.image.load('wall.png')
plateimg = pygame.image.load('plate.png')
plate2img = pygame.image.load('plate.png')
plate3img = pygame.image.load('plate.png')
plate4img = pygame.image.load('plate.png')
knifeimg = pygame.image.load('knife.png')
pokalimg = pygame.image.load('pokal.png')
knifesmallimg = pygame.image.load('knifesmall.png')
pizzaimg = pygame.image.load('pizza slice.png')
playimg = pygame.image.load('playing.png')
muteimg = pygame.image.load('mute.png')
knifewav = pygame.mixer.Sound('knifing.wav')
buywav = pygame.mixer.Sound('buy.wav')
clickwav = pygame.mixer.Sound('click.wav')
levelwav = pygame.mixer.Sound('levelup.wav')
errorwav = pygame.mixer.Sound('error.wav')
savewav = pygame.mixer.Sound('save.wav')
pygame.init()

# Set up the drawing window
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
if os.path.isfile('save.txt'):
  yeah = 0
  f = open('save.txt')
  clicks = float(f.readline().strip())
  value = int(f.readline().strip())
  price = int(f.readline().strip())
  price2 = int(f.readline().strip())
  price3 = int(f.readline().strip())
  knife = int(f.readline().strip())
  level = int(f.readline().strip())
  verline1 = float(f.readline().strip())
  verline2 = float(f.readline().strip())

  google = 0
  googleV2 = 0
  click = str(clicks)
  pricetxt = str(price)
  price2txt = str(price2)
  price3txt = str(price3)

  verify = clicks + value + price + price2 + price3 + knife + level * 13 - 3464
  verify1 = clicks + value + price + price2 + price3 + knife + level * 21 + 9856
  if verify == verline1:
    if verify1 == verline2:
        yeah = 1

else:
  level = 1
  yeah = 1
  clicks = 0
  click = str(numerize.numerize(clicks, 2))
  google = 0
  googleV2 = 0
  value = 1
  price = 50
  price2 = 100
  price3 = 500
  knife = 0
  pricetxt = str(price)
  price2txt = str(price2)
  price3txt = str(price3)
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode([1920, 1080])
M = pygame.mouse.get_pos()
posyknife = 450
minuser = -2
volume = True
# Run until the user asks to quit
def is_over(rect, pos):
  return True if rect.collidepoint(pos[0], pos[1]) else False
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if yeah != 1:
      print("STOP CHEATIN. delete save file you must")
      running = False


    screen.fill((255, 255, 255))
    pricetxt = str(numerize.numerize(price))
    price2txt = str(numerize.numerize(price2))
    price3txt = str(numerize.numerize(price3))
    click = str(numerize.numerize(round(clicks, 1), 2))
    #quit
    rectangle = pygame.Rect(1650, 100, 200, 50)
    quity = myfont.render("quit", False, (0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0),(1650,100,200,50))
    screen.blit(quity,(1665,100))
    if event.type == pygame.MOUSEBUTTONDOWN:
      if is_over(rectangle, M):
        running = False




    #standard
    if event.type == pygame.MOUSEBUTTONUP:
      googleV2 = 0
      google = 0
    txtpinapple = myfont.render("Pinapple:", False, (0, 0, 0))
    txtknife = myfont.render("Knife:", False, (0, 0, 0))
    txtpizza = myfont.render("Pizza:", False, (0, 0, 0))
    txtpokal = myfont.render("Price: 999T", False, (0, 0, 0))
    txtpokal1 = myfont.render("Level:", False, (0, 0, 0))
    txtpokal2 = myfont.render(str(numerize.numerize(level)), False, (0, 0, 0))
    txtprice3 = myfont.render(price3txt, False, (0, 0, 0))
    txtprice2 = myfont.render(price2txt, False, (0, 0, 0))
    txtprice = myfont.render(pricetxt, False, (0, 0, 0))
    textsurface = myfont.render(click, False, (0, 0, 0))
    screen.blit(textsurface,(950,255))
    screen.blit(spaceimg,(810,300))
    screen.blit(wallimg,(0,100))
    screen.blit(plateimg,(55,125))
    screen.blit(txtpinapple,(275,130))
    screen.blit(upimg,(275,170))
    screen.blit(txtprice,(400,130))
    screen.blit(plate2img,(55,325))
    screen.blit(txtprice2,(370,330))
    screen.blit(txtknife,(275,330))
    screen.blit(knifesmallimg,(275,400))
    screen.blit(plate3img,(55,525))
    screen.blit(pizzaimg,(300,600))
    screen.blit(txtpizza,(275,535))
    screen.blit(txtprice3,(370,535))
    screen.blit(plate4img,(55,725))
    screen.blit(pokalimg,(200,765))
    screen.blit(txtpokal,(325,750))
    screen.blit(txtpokal1,(325,825))
    screen.blit(txtpokal2,(410,825))

    mute = pygame.Rect(1650, 900, 75, 75)
    if event.type == pygame.MOUSEBUTTONDOWN:
      if is_over(mute, M):
        if google == 0:
          google = 1
          if volume == False:
            volume = True
          else:
            volume = False


    if volume == True:
      screen.blit(playimg,(1650,900))
    else:
      screen.blit(muteimg,(1650,900))



    if knife >= 1:
      screen.blit(knifeimg,(970,posyknife))
      clicks = clicks + (knife / 25)
      posyknife = posyknife + minuser
      if posyknife >= 600:
        minuser = -5
      if posyknife <= 400:
        minuser = 20
        if volume == True:
          knifewav.play()
    
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    sqx = (x - 965)**2
    sqy = (y - 805)**2

    #click
    M = pygame.mouse.get_pos()
    ananasrect = pygame.Rect(870, 315, 175, 350)
    if event.type == pygame.MOUSEBUTTONDOWN:
      if is_over(ananasrect, M):
        if google == 0:
          clicks = (clicks + value)
          google = 1
          if volume == True:
            clickwav.play()
          
    
    buyananas = pygame.Rect(55, 137, 500, 175)
    buyknife = pygame.Rect(55, 330, 500, 175)
    buypizza = pygame.Rect(55, 533, 500, 175)
    buypokal = pygame.Rect(55, 735, 500, 175)
    #upgrade
    if event.type == pygame.MOUSEBUTTONDOWN:
      if is_over(buyananas, M):
        if clicks >= price:
          pygame.draw.rect(screen, (0, 255, 0), (55, 137, 500, 175))
          if googleV2 == 0:
            value = value + 1
            googleV2 = 1
            clicks = clicks - price
            price = price + (50 * level)
            if volume == True:
              buywav.play()   
        else:
          pygame.draw.rect(screen, (255, 0, 0), (55, 137, 500, 175))
          googleV2 = 1
          if volume == True:
            errorwav.play()   
    
    #buy knife
    if event.type == pygame.MOUSEBUTTONDOWN:
      if is_over(buyknife, M):
        if clicks >= price2:
          pygame.draw.rect(screen, (0, 255, 0), (55, 330, 500, 175))
          if googleV2 == 0:
            knife = knife + 1
            googleV2 = 1
            clicks = clicks - price2
            price2 = price2 + (100 * level)
            if volume == True:
              buywav.play()   
        else:
          pygame.draw.rect(screen, (255, 0, 0), (55, 330, 500, 175))
          googleV2 = 1
          if volume == True:
            errorwav.play() 
    #buy pizza
    if event.type == pygame.MOUSEBUTTONDOWN:
      if is_over(buypizza, M):
        if clicks >= price3:
          pygame.draw.rect(screen, (0, 255, 0), (55, 533, 500, 175))
          if googleV2 == 0:
            clicks = clicks - price3
            price3 = price3 + 500
            verify = float(clicks) + value + price + price2 + price3 + knife + level * 13 - 3464
            verify1 = float(clicks) + value + price + price2 + price3 + knife + level * 21 + 9856
            with open("save.txt", "w") as file: # xyz.txt is filename, w means write format
              file.write("save") # write text xyz in the file
            f= open("save.txt", "w")
            f.write(str(clicks))
            f.write('\n')
            f.write(str(value))
            f.write('\n')
            f.write(str(price))
            f.write('\n')
            f.write(str(price2))
            f.write('\n')
            f.write(str(price3))
            f.write('\n')
            f.write(str(knife))
            f.write('\n')
            f.write(str(level))
            f.write('\n')
            f.write(str(verify))
            f.write('\n')
            f.write(str(verify1))
            f.close()
            if volume == True:
              savewav.play() 
        else:
          pygame.draw.rect(screen, (255, 0, 0), (55, 533, 500, 175))
          googleV2 = 1
          if volume == True:
            errorwav.play() 

    #buy level
    if event.type == pygame.MOUSEBUTTONDOWN:
      if is_over(buypokal, M):
        if clicks >= 999000000000000:
          pygame.draw.rect(screen, (0, 255, 0), (55, 735, 500, 175))
          if googleV2 == 0:
            level = level + 1
            googleV2 = 1
            clicks = 0
            click = str(numerize.numerize(clicks, 2))
            value = 1
            price = 50 * level
            price2 = 100 * level
            price3 = 500
            knife = 0
            pricetxt = str(price)
            price2txt = str(price2)
            price3txt = str(price3)
            if volume == True:
              levelwav.play() 
        else:
          pygame.draw.rect(screen, (255, 0, 0), (55, 735, 500, 175))
          googleV2 = 1
          if volume == True:
            errorwav.play()



    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()