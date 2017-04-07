import sys, pygame, time, psycopg2

pygame.init()

# colors
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
turquoise = [0, 255, 255]
purple = [255, 0, 255]
yellow = [255, 255, 0]
white = [255, 255, 255]
black = [0, 0, 0]
map_color = [0, 148, 255]


# Globals
width = 1300
height = 800
screen = pygame.display.set_mode((width, height)) # sreen size
x = (width * 0.45)
y = (height * 0.8)
pygame.display.set_caption('roadmap netherlands') # titel of pygame frame

# images
map_image = pygame.image.load('images/wegenkaartV2.png')