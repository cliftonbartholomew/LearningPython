##################SETUP##########################################
import pygame
pygame.init()


WIDTH = 800
HEIGHT = 600
page = pygame.display.set_mode([WIDTH , HEIGHT])
pygame.display.set_caption("MyGame")


background = pygame.image.load("Resources\\dungeon.png")


egg = pygame.image.load("Resources\\one-egg.png")
eggX = 300
eggY = 300

char = pygame.image.load("Resources\\hero.png")
charX = 100
charY = 100
charYVel = 0
charXVel = 0


running = True
##################FOREVER LOOP###################################
while running:


##################CHECKS AND CHANGES#############################
    #event checking
    for event in pygame.event.get():
        #if the red x is clicked
        if event.type == pygame.QUIT:
          running = False
          
        #if a key is being pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
              charYVel = -1
            if event.key == pygame.K_DOWN:
              charYVel = 1
            if event.key == pygame.K_LEFT:
              charXVel = -1
            if event.key == pygame.K_RIGHT:
              charXVel = 1

        #if a key is being released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
              charYVel = 0
            if event.key == pygame.K_DOWN:
              charYVel = 0
            if event.key == pygame.K_LEFT:
              charXVel = 0
            if event.key == pygame.K_RIGHT:
              charXVel = 0

    #other checks
    if charX == eggX or charY == eggY:
        eggX = 5
        eggY = 5
    
    #other changes
    charX = charX + charXVel
    charY = charY + charYVel

    
        

##################PAINT ONTO AND REDRAW SCREEN###################
    page.blit(background, (0,0))
    page.blit(char, (charX,charY))
    page.blit(egg, (eggX,eggY))


    pygame.display.flip()


pygame.quit()
