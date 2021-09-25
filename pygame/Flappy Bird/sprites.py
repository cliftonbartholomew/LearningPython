import pygame

from utilities import *
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = loadImage("bird.png")
        self.surf = pygame.Surface(self.image.get_size())
        self.rect = self.surf.get_rect()

        self.rect.y = HEIGHT/2
        self.rect.x = WIDTH/6
        self.yVelocity = 0

    def move(self):
        self.yVelocity += GRAVITY
        self.rect.move_ip(0, self.yVelocity)

    def jump(self):
        self.yVelocity = JUMP_VELOCITY

    def reset(self):
        self.yVelocity = 0
        self.rect.y = HEIGHT/2

class floor(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = loadImage("ground.png")
        self.image = pygame.transform.scale(self.image, (WIDTH, self.image.get_height()))
        self.surf = pygame.Surface(self.image.get_size())
        self.rect = self.surf.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.top = HEIGHT - self.image.get_height()/4


    def move(self):
        pass

    def reset(self):
        pass

class Tube(pygame.sprite.Sprite):
    #direction 1 - up, 0 - down
    #offset must be less than TUBE_RANGE
    def __init__(self, direction, yOffset):
        super().__init__()

        #down
        if(direction == 0):
            self.image = loadImage("tube1.png")
        #up
        elif(direction == 1):
            self.image = loadImage("tube2.png")
        self.surf = pygame.Surface(self.image.get_size())
        self.rect = self.surf.get_rect()
        self.direction = direction

        if(self.direction == 0):
            self.rect.top = TUBE_Y_BASE + yOffset
        elif(self.direction == 1):
            self.rect.top = TUBE_Y_BASE + yOffset + TUBE_SPACING + TUBE_IMAGE_HEIGHT

        self.rect.x = WIDTH + self.rect.width

    def move(self):
        self.rect.move_ip(TUBE_VELOCITY,0)

    def reset(self, yOffset):
        if (self.direction == 0):
            self.rect.top = TUBE_Y_BASE + yOffset
        elif (self.direction == 1):
            self.rect.top = TUBE_Y_BASE + yOffset + TUBE_SPACING + TUBE_IMAGE_HEIGHT

        self.rect.x = WIDTH + self.rect.width

    def isOffScreen(self):
        return self.rect.right < 0