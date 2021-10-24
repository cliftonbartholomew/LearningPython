import pygame
import sys
import os

from settings import *

main_dir = os.path.split(os.path.abspath(__file__))[0]

def loadImage(imageName):
    file = os.path.join(main_dir, "images", imageName)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
    return surface


def drawText(surface, font, text, x, y, hasBackground, foregroundColor = WHITE, backgroundColor = BLACK):
    output = font.render(text, True, foregroundColor)
    background = font.render(text, True, backgroundColor)

    offset = output.get_width()/2

    if hasBackground:
        surface.blit(background, (x-1 - offset, y-1))
        surface.blit(background, (x-1 - offset, y+1))
        surface.blit(background, (x+1 - offset, y-1))
        surface.blit(background, (x+1 - offset, y+1))

    surface.blit(output, (x - offset,y))
