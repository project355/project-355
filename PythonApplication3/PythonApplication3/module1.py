import pygame
from buttonclass import *

#colors are in a range of 0-255 (256 different entries)
black = (0,0,0)
white = (255,255,255)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_yellow = (239,254,54)
bright_blue = (64,132,244)
red = (200,0,0)
green = (0,200,0)
yellow = (236,220,26)
blue = (11,83,202)
mudgreen = (51,125,2)
mudyellow = (119,117,19)
mudred = (112,46,27)
mudblue = (1,66,137)

background_colour = (255,255,255)
(width, height) = (1120, 950)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Leuke titel')
screen.fill(mudred)
pygame.display.flip()

program = True


while program == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    program = False
               

quit()