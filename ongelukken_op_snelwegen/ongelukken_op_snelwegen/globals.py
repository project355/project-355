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

# button
def text_objects(text, font):   #functie om tekst te tonen
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    """functie om een knop te maken (text,x,y,width,height,kleur, hover kleur, actie)"""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:   #als de muis over de knop hovert, verander de kleur
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:        #als je er op klikt, doe actie
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)