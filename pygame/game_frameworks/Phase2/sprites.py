from settings import *
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0,0,50,50) #(x, y, width, height)
        self.rect.y = HEIGHT/2
        self.rect.x = WIDTH/6
        self.yVelocity = 0

    def move(self):
        self.yVelocity = self.yVelocity + GRAVITY
        self.rect.move_ip(0, self.yVelocity)

    def jump(self):
        self.yVelocity = JUMP_VELOCITY

class Tube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0,0,10,200) #(x, y, width, height)
        self.rect.y = HEIGHT/2
        self.rect.x = WIDTH
        self.xVelocity = -5

    def move(self):
        self.rect.move_ip(self.xVelocity, 0)

    def reset(self):
        self.rect.y = HEIGHT/2
        self.rect.x = WIDTH        






