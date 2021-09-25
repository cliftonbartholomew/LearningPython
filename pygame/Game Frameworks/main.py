#################################################################
################# SETUP #########################################
#################################################################
import pygame
import sprites
from settings import *

pygame.init()

page = pygame.display.set_mode([400 , 400])
pygame.display.set_caption("GAME HEADING")
clock = pygame.time.Clock()

backgroundColor = (255,255,255)
rectColor = (255,255,0)

player = sprites.Player()
tube  = sprites.Tube()

tubes = pygame.sprite.Group()
tubes.add(tube)

running = True
dead = False
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.jump()
          
    #handle all the keydown event states
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_SPACE]:
        player.jump()


      
    #############################################################
    ################## CHECKS AND CHANGES #######################
    #############################################################   
    if not dead:
        player.move()
        tube.move()
        if tube.rect.x < 0:
            tube.reset()
          
    if pygame.sprite.spritecollideany(player, tubes):
        dead = True
    
        
    #############################################################
    ################## REDRAW THE SCREEN ########################
    #############################################################   
    page.fill(backgroundColor)
    pygame.draw.rect(page, rectColor, player.rect)
    pygame.draw.rect(page, rectColor, tube.rect)


    
    pygame.display.flip()
    clock.tick(30)


pygame.quit()
