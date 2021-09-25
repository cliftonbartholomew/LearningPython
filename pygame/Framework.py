#################################################################
################# SETUP #########################################
#################################################################
import pygame
pygame.init()

page = pygame.display.set_mode([500 , 500])
pygame.display.set_caption("GAME HEADING")
clock = pygame.time.Clock()

backgroundColor = (255,255,255)
rectColor = (255,255,0)

rectSize = 50
rectX = 100
rectY = 100

rectSize2 = 50
rectX2 = 100
rectY2 = 100

running = True
#################################################################
################## GAME LOOP ####################################
#################################################################
while running:

    #############################################################
    ################# EVENT HANDLING ############################
    #############################################################   
    #event handling in the main loop
    for event in pygame.event.get():
        #handle the exit event
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.MOUSEMOTION:
            rectX2 = event.pos[0]
            rectY2 = event.pos[1]
          
    #handle all the keydown event states
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        rectX = rectX - 5
    if pressed_keys[pygame.K_RIGHT]:
        rectX = rectX + 5
    if pressed_keys[pygame.K_UP]:
        rectY = rectY - 5
    if pressed_keys[pygame.K_DOWN]:
        rectY = rectY + 5

      
    #############################################################
    ################## CHECKS AND CHANGES #######################
    #############################################################   

 
    #############################################################
    ################## REDRAW THE SCREEN ########################
    #############################################################   
    page.fill(backgroundColor)
    pygame.draw.rect(page, rectColor, (rectX,rectY,rectSize,rectSize))
    pygame.draw.rect(page, rectColor, (rectX2,rectY2,rectSize2,rectSize2))

    
    pygame.display.flip()
    clock.tick(30)


pygame.quit()
