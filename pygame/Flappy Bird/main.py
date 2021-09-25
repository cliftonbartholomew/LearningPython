import random
import time

import pygame


from utilities import *
from sprites import *
from settings import *

pygame.init()

#screen
pygame.display.set_caption("FLAPPY BIRD")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()


#############################################################################
##########   SETUP  #########################################################
#############################################################################

#font setup
font = pygame.font.Font("Flappy-Bird.ttf", 60)
font_small = pygame.font.SysFont("Verdana", 20)

background = loadImage("bg.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#setting up sprites
floorOb = floor()
P1 = Player()
num = random.randint(0, TUBE_RANGE)
T1 = Tube(0, num)
T2 = Tube(1, num)

#adding them to groups
tubes = pygame.sprite.Group()
tubes.add(T1)
tubes.add(T2)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(T1)
all_sprites.add(T2)
all_sprites.add(floorOb)

floorGroup = pygame.sprite.Group()
floorGroup.add(floorOb)

dead = False

#############################################################################
##########   GAME LOOP ######################################################
#############################################################################
while True:
    ##########################################
    ########## GAME EVENTS ###################
    ##########################################
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not dead:
                    P1.jump()
                else:
                    num = random.randint(0, TUBE_RANGE)
                    for t in tubes:
                        t.reset(num)
                    P1.reset()
                    SCORE = 0
                    TUBE_VELOCITY = -3
                    dead = False


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ##########################################
    ########## GAME LOGIC ####################
    ##########################################

    #check for collisions
    if pygame.sprite.spritecollideany(P1, tubes) or pygame.sprite.spritecollideany(P1, floorGroup):
        dead = True

    #reset tubes when they move off screen
    if(T1.isOffScreen()):
        num = random.randint(0, TUBE_RANGE)
        for t in tubes:
            t.reset(num)

    #update score when tubes reach certain x value
    #(Note: this must change)
    if(T1.rect.x == SCORE_BARRIER):
        SCORE += 1
        if SCORE > HIGH_SCORE:
            HIGH_SCORE = SCORE

    ##########################################
    ########## DRAW FRAME ####################
    ##########################################

    #draw background
    screen.blit(background, (0,0))

    #draw sprites (and move them)
    for sprite in all_sprites:
        if not dead:
            sprite.move()
        screen.blit(sprite.image, sprite.rect)

    #draw score
    if not dead:
        drawText(screen, font, str(SCORE), WIDTH/2, 10, True)

    if dead:
        pygame.draw.rect(screen, BLACK, (150, 140, 100, 120), 2, 14)
        pygame.draw.rect(screen, (222,216,149), (152, 142, 96, 116), 0, 14)
        drawText(screen, font_small, "SCORE", WIDTH/2, 145, False,foregroundColor = (252,120,88))
        drawText(screen, font_small, str(SCORE), WIDTH/2, 170, True)
        drawText(screen, font_small, "BEST", WIDTH/2, 195, False,foregroundColor = (252,120,88))
        drawText(screen, font_small, str(HIGH_SCORE), WIDTH/2, 220, True)


    pygame.display.update()
    clock.tick(FPS)
