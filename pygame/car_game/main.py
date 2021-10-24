import sys
import os
import random
import time

import pygame

pygame.init()

WIDTH = 400
HEIGHT = 600
FPS = 40
ENEMY_SPEED = 10
PLAYER_SPEED = 5
SCORE = 0

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

#screen
pygame.display.set_caption("Car Game")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

main_dir = os.path.split(os.path.abspath(__file__))[0]

def loadImage(imageName):
    file = os.path.join(main_dir, "Resources", imageName)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
    return surface

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = loadImage("Enemy.png")
        self.surf = pygame.Surface(self.image.get_size())
        self.rect = self.surf.get_rect(center = (random.randint(40, WIDTH - 40), 0))

    def move(self):
        global SCORE
        self.rect.move_ip(0,ENEMY_SPEED)
        if(self.rect.bottom > HEIGHT):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = loadImage("Player.png")
        self.surf = pygame.Surface(self.image.get_size())
        self.rect = self.surf.get_rect()

        self.rect.y = HEIGHT - self.rect.height

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-1*PLAYER_SPEED, 0)
        if self.rect.right < 600:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(PLAYER_SPEED, 0)

#font setup
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = loadImage("AnimatedStreet.png")

#setting up sprites
P1 = Player()
E1 = Enemy()

#adding them to groups
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#creating your own user events
INCREASE_SPEED = pygame.USEREVENT + 1 #userevent is the last enum defined (just keep adding one to make multiple new events)
pygame.time.set_timer(INCREASE_SPEED, 1000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == INCREASE_SPEED:
            ENEMY_SPEED +=2

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10,10))

    for sprite in all_sprites:
        sprite.move()
        screen.blit(sprite.image, sprite.rect)

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("Resources\\crash.wav").play()
        time.sleep(0.5)

        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        for sprite in all_sprites:
            sprite.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(FPS)
