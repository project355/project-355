import pygame, time, psycopg2
import eztext

pygame.init()

display_width = 1300
display_height = 800
pygame.mixer.music.load("Salty_Ditty.wav")

# globals
x = (display_width * 0.45)
y = (display_height * 0.8)
pygame.display.set_caption('roadmap netherlands') # titel of pygame frame

# image
map_image = pygame.image.load('images/wegenkaartV2.png')

#colors are in a range of 0-255 (256 different entries)
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
turquoise = [0, 255, 255]
purple = [255, 0, 255]
yellow = [255, 255, 0]
white = [255, 255, 255]
black = [0, 0, 0]
map_colour = [0, 148, 255]
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_yellow = (255,255,54)
bright_blue = (64,132,244)
mudgreen = (51,125,2)
mudyellow = (119,117,19)
mudred = (112,46,27)
mudblue = (1,66,137)
map_colour = (0, 148, 255)

#------------------------------------------------------------------------------------------------------------------------

intro, Introduction, gameExit,playing, players, throwdice = True, False, False, False, False, 0
gameDisplay = pygame.display.set_mode((display_width, display_height))  #init resolution
pygame.display.set_caption('Name')  #window naam
clock = pygame.time.Clock()     #nodig voor Refresh Rate
_image_library = {}     #global list

#-------------------------------------------------------------------------------------------------------------------------

def button(msg,x,y,w,h,ic,ac,action=None):          #functie om een knop te maken (text,x,y,width,height,kleur, hover kleur, actie)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:   #als de muis over de knop hovert, verander de kleur
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:        #als je er op klikt, doe actie
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def text_objects(text, font):   #functie om tekst te tonen
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def sound_off():
    pygame.mixer.music.stop()
def sound_on():
    pygame.mixer.music.play(-1)
def volumedown():
    volume = pygame.mixer.music.get_volume()
    volume = volume - 0.1
    pygame.mixer.music.set_volume(volume)

def volumeup():
    volume = pygame.mixer.music.get_volume()
    volume = volume + 0.1
    pygame.mixer.music.set_volume(volume)
    
def map(x,y):
    gameDisplay.blit(map_image, (x,y))