import pygame
from buttonclass import *
import time
import psycopg2
import eztext
pygame.init()
display_width = 1200
display_height = 800
pygame.mixer.music.load("Salty_Ditty.wav")
#colors are in a range of 0-255 (256 different entries)
black = (0,0,0)
white = (255,255,255)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_yellow = (255,255,54)
bright_blue = (64,132,244)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
blue = (11,83,202)
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

def button1(msg,x,y,w,h,ic,ac,action=None):          #functie om een knop te maken (text,x,y,width,height,kleur, hover kleur, actie)
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

#-----------------------------------------------------------------------------------------------------------

def Main_scherm():   #main menu scherm
    Instruction, Intro = False, True
    x, y, mov_x, mov_y = 0,0,6,6
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(map_colour)
        button1("kaart", 50, 230, 700, 50,yellow, red, Kaart_scherm)
        button1("Navigatie", 50, 330, 700, 50, yellow, red, Navigatie_scherm)
        button1("Opties", 50, 430, 700, 50, yellow, red, Opties_scherm)

        clock.tick(60)      #refresh rate
        pygame.display.flip()

def Kaart_scherm():    #kaart scherm
    Instruction, Intro = True, False
    while Instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(map_colour)
        button1("Back", 50, 500, 700, 50, yellow, red, Main_scherm)
        clock.tick(15)  #refresh rate van 15
        pygame.display.flip()

def Navigatie_scherm():    #navigatie scherm
    Instruction, Intro = True, False
    while Instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(map_colour)
        button1("Back", 50, 500, 700, 50, yellow, red, Main_scherm)
        clock.tick(15)  #refresh rate van 15
        pygame.display.flip()
def Opties_scherm():  #opties menu
    Instruction, Intro = True, False
    while Instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(map_colour)
        button1("Sound off", 50, 130, 350, 50, yellow, red, sound_off)
        button1("Sound on", 400, 130, 350, 50, yellow, red, sound_on)
        button1("Volume down", 50, 230, 350, 50, yellow, red, volumedown)
        button1("Volume up", 400, 230, 350, 50, yellow, red, volumeup)
        button1("Back", 50, 500, 700, 50, yellow, red, Main_scherm)
        clock.tick(15)  #refresh rate van 15
        pygame.display.flip()

pygame.mixer.music.play(-1)
Main_scherm()
Kaart_scherm()
Navigatie_scherm()
quit()
