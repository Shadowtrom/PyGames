# Simple pygame program

# Import and initialize the pygame library
import pygame, math, sys, os.path, random
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
plate5img = pygame.image.load('plate.png')
colorimg = pygame.image.load('colorrand.png')
colorwav = pygame.mixer.Sound('colorchange.wav')
res = pygame.image.load('reset.png')
pygame.init()
pygame.display.set_caption('pineapple clicker')
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
  r = int(f.readline().strip())
  g = int(f.readline().strip())
  b = int(f.readline().strip())
  verline1 = float(f.readline().strip())
  verline2 = float(f.readline().strip())

  google = 0
  googleV2 = 0
  click = str(clicks)
  pricetxt = str(price)
  price2txt = str(price2)
  price3txt = str(price3)

  verify = clicks + value + price + price2 + price3 + knife + level + r + g + b * 13 - 3464
  verify1 = clicks + value + price + price2 + price3 + knife + level + r + g + b * 21 + 9856
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
  r = 255
  g = 255
  b = 255
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode([1920, 1080])
M = pygame.mouse.get_pos()
posyknife = 450
minuser = -2
volume = True
colorprice = 'Color change: ' + str(numerize.numerize((clicks / 10), 0))
colorcost = (clicks / 10)
co = (r,g,b)
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

    co = (r,g,b)
    colorcost = (clicks / 10)
    colorprice = 'Color change: ' + str(numerize.numerize((clicks / 10), 0))
    screen.fill(co)
    if clicks < 10 :
      colorcost = 30
      colorprice = 'NULL'
    pricetxt = str(numerize.numerize(price))
    price2txt = str(numerize.numerize(price2))
    price3txt = str(numerize.numerize(price3))
    click = str(numerize.numerize(round(clicks, 1), 2))
    #quit
    rectangle = pygame.Rect(1830,0,200,60)
    quity = myfont.render("quit", False, (0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0),(1830,0,200,60))
    screen.blit(quity,(1850,5))
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
    txtcolor = myfont.render(str(colorprice), False, (0, 0, 0))
    screen.blit(textsurface,(950,255))
    screen.blit(spaceimg,(810,300))
    screen.blit(wallimg,(0,0))
    screen.blit(plateimg,(55,20))
    screen.blit(txtpinapple,(275,25))
    screen.blit(upimg,(275,55))
    screen.blit(txtprice,(400,25))
    screen.blit(plate2img,(55,225))
    screen.blit(txtprice2,(370,230))
    screen.blit(txtknife,(275,230))
    screen.blit(knifesmallimg,(275,300))
    screen.blit(plate3img,(55,425))
    screen.blit(pizzaimg,(300,495))
    screen.blit(txtpizza,(275,435))
    screen.blit(txtprice3,(370,435))
    screen.blit(plate4img,(55,625))
    screen.blit(pokalimg,(200,665))
    screen.blit(txtpokal,(325,650))
    screen.blit(txtpokal1,(325,725))
    screen.blit(txtpokal2,(410,725))
    screen.blit(plate5img,(55,825))
    screen.blit(colorimg,(150,875))
    screen.blit(txtcolor,(250,865))
    screen.blit(res,(250,875))

    

    mute = pygame.Rect(1830, 990, 100, 100)
    if event.type == pygame.MOUSEBUTTONDOWN:
      if is_over(mute, M):
        if google == 0:
          google = 1
          if volume == False:
            volume = True
          else:
            volume = False


    if volume == True:
      screen.blit(playimg,(1840,1000))
    else:
      screen.blit(muteimg,(1840,1000))



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
          
    
    buyananas = pygame.Rect(55, 30, 500, 175)
    buyknife = pygame.Rect(55, 235, 500, 175)
    buypizza = pygame.Rect(55, 433, 500, 175)
    buypokal = pygame.Rect(55, 635, 500, 175)
    buycolor = pygame.Rect(55, 835, 500, 175)
    buyreset = pygame.Rect(250, 920, 150, 55)
    #pygame.draw.rect(screen, (255, 255, 255), (buyananas))
    #pygame.draw.rect(screen, (255, 255, 255), (buyknife))
    #pygame.draw.rect(screen, (255, 255, 255), (buypizza))
    #pygame.draw.rect(screen, (255, 255, 255), (buypokal))
    #pygame.draw.rect(screen, (255, 255, 255), (buycolor))
    #pygame.draw.rect(screen, (255, 255, 255), (buyreset))

    #upgrade
    if event.type == pygame.MOUSEBUTTONDOWN:
      if is_over(buyananas, M):
        if clicks >= price:
          pygame.draw.rect(screen, (0, 255, 0), (buyananas))
          if googleV2 == 0:
            value = value + 1
            googleV2 = 1
            clicks = clicks - price
            price = price + (50 * level)
            if volume == True:
              buywav.play()   
        else:
          pygame.draw.rect(screen, (255, 0, 0), (buyananas))
          googleV2 = 1
          if volume == True:
            errorwav.play()   
    
    #buy knife
    if event.type == pygame.MOUSEBUTTONDOWN:
      if is_over(buyknife, M):
        if clicks >= price2:
          pygame.draw.rect(screen, (0, 255, 0), (buyknife))
          if googleV2 == 0:
            knife = knife + 1
            googleV2 = 1
            clicks = clicks - price2
            price2 = price2 + (100 * level)
            if volume == True:
              buywav.play()   
        else:
          pygame.draw.rect(screen, (255, 0, 0), (buyknife))
          googleV2 = 1
          if volume == True:
            errorwav.play() 
    #buy pizza
    if event.type == pygame.MOUSEBUTTONDOWN:
      if is_over(buypizza, M):
        if clicks >= price3:
          pygame.draw.rect(screen, (0, 255, 0), (buypizza))
          if googleV2 == 0:
              clicks = clicks - price3
              googleV2 = 1
              price3 = price3 + 500
              verify = float(clicks) + value + price + price2 + price3 + knife + level + r + g + b * 13 - 3464
              verify1 = float(clicks) + value + price + price2 + price3 + knife + level + r + g + b * 21 + 9856
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
              f.write(str(r))
              f.write('\n')
              f.write(str(g))
              f.write('\n')
              f.write(str(b))
              f.write('\n')
              f.write(str(verify))
              f.write('\n')
              f.write(str(verify1))
              f.close()
              if volume == True:
                savewav.play() 
        else:
          pygame.draw.rect(screen, (255, 0, 0), (buypizza))
          googleV2 = 1
          if volume == True:
            errorwav.play() 

    #buy level
    if event.type == pygame.MOUSEBUTTONDOWN:
      if is_over(buypokal, M):
        if clicks >= 999000000000000:
          pygame.draw.rect(screen, (0, 255, 0), (buypokal))
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
          pygame.draw.rect(screen, (255, 0, 0), (buypokal))
          googleV2 = 1
          if volume == True:
            errorwav.play()


        #buy color
    if event.type == pygame.MOUSEBUTTONDOWN:
      if is_over(buycolor, M):
        if is_over(buyreset, M):
          if googleV2 == 0:
            r = 255
            g = 255
            b = 255
            colorwav.play()
            pygame.draw.rect(screen, (0, 255, 0), (buyreset))
            googleV2 = 1
        else:
          if clicks >= colorcost:
            pygame.draw.rect(screen, (0, 255, 0), (buycolor))
            if googleV2 == 0:
              r = random.randint(0, 255)
              g = random.randint(0, 255)
              b = random.randint(0, 255)
              clicks = clicks - colorcost
              googleV2 = 1
              if volume == True:
                colorwav.play() 
          else:
            pygame.draw.rect(screen, (255, 0, 0), (buycolor))
            googleV2 = 1
            if volume == True:
              errorwav.play()

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()