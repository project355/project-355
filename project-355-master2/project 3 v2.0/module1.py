import pygame, time, psycopg2
import eztext

pygame.init()

display_width = 1300
display_height = 800
pygame.mixer.music.load("poi.wav")

# globals
x = (display_width * 0.45)
y = (display_height * 0.8)
pygame.display.set_caption('Roadmap Netherlands') # titel of pygame frame

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
pygame.display.set_caption('Roadmap Netherlands')  #window naam
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
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Main_scherm():   #main menu scherm
    Instruction, Intro = False, True
    x, y, mov_x, mov_y = 0,0,6,6
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(map_colour)
        button("kaart", 50, 230, 700, 50,yellow, red, Kaart_scherm)
        button("Navigatie", 50, 330, 700, 50, yellow, red, Navigatie_scherm)
        button("Opties", 50, 430, 700, 50, yellow, red, Opties_scherm)

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
        map(10,10)

        # button vars
        x1 = 700
        nextX = 60
        y1 = 15
        nextY = 50
        # button row 1
        button("A1", x1, y1, 53, 30, yellow, red)
        button("A2", x1 + nextX, y1, 53, 30, yellow, red)
        button("A4", x1 + nextX * 2, y1, 53, 30, yellow, red)
        button("A5", x1 + nextX * 3, y1, 53, 30, yellow, red)
        button("A6", x1 + nextX * 4, y1, 53, 30, yellow, red)
        button("A7", x1 + nextX * 5, y1, 53, 30, yellow, red)
        button("A8", x1 + nextX * 6, y1, 53, 30, yellow, red)
        button("A9", x1 + nextX * 7, y1, 53, 30, yellow, red)
        button("A10", x1 + nextX * 8, y1, 53, 30, yellow, red)

        # button row 2
        button("A12", x1, y1 + nextY, 53, 30, yellow, red)
        button("A13", x1 + nextX, y1 + nextY, 53, 30, yellow, red)
        button("A15", x1 + nextX * 2, y1 + nextY, 53, 30, yellow, red)
        button("A16", x1 + nextX * 3, y1 + nextY, 53, 30, yellow, red)
        button("A17", x1 + nextX * 4, y1 + nextY, 53, 30, yellow, red)
        button("A18", x1 + nextX * 5, y1 + nextY, 53, 30, yellow, red)
        button("A20", x1 + nextX * 6, y1 + nextY, 53, 30, yellow, red)
        button("A27", x1 + nextX * 7, y1 + nextY, 53, 30, yellow, red)
        button("A28", x1 + nextX * 8, y1 + nextY, 53, 30, yellow, red)

        # button row 3
        button("A29", x1, y1 + nextY * 2, 53, 30, yellow, red)
        button("A30", x1 + nextX, y1 + nextY * 2, 53, 30, yellow, red)
        button("A31", x1 + nextX * 2, y1 + nextY * 2, 53, 30, yellow, red)
        button("A32", x1 + nextX * 3, y1 + nextY * 2, 53, 30, yellow, red)
        button("A35", x1 + nextX * 4, y1 + nextY * 2, 53, 30, yellow, red)
        button("A37", x1 + nextX * 5, y1 + nextY * 2, 53, 30, yellow, red)
        button("A44", x1 + nextX * 6, y1 + nextY * 2, 53, 30, yellow, red)
        button("A50", x1 + nextX * 7, y1 + nextY * 2, 53, 30, yellow, red)
        button("A58", x1 + nextX * 8, y1 + nextY * 2, 53, 30, yellow, red)

        # button row 4
        button("A59", x1, y1 + nextY * 3, 53, 30, yellow, red)
        button("A65", x1 + nextX, y1 + nextY * 3, 53, 30, yellow, red)
        button("A67", x1 + nextX * 2, y1 + nextY * 3, 53, 30, yellow, red)
        button("A73", x1 + nextX * 3, y1 + nextY * 3, 53, 30, yellow, red)
        button("A76", x1 + nextX * 4, y1 + nextY * 3, 53, 30, yellow, red)
        button("A77", x1 + nextX * 5, y1 + nextY * 3, 53, 30, yellow, red)
        button("A79", x1 + nextX * 6, y1 + nextY * 3, 53, 30, yellow, red)
        button("A200", x1 + nextX * 7, y1 + nextY * 3, 53, 30, yellow, red)
        button("EE_1", x1 + nextX * 8, y1 + nextY * 3, 53, 30, yellow, red)
        
        # button back
        button("back", 1200, 700, 53, 30, yellow, red, Main_scherm)
        
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
        button("Back", 50, 500, 700, 50, yellow, red, Main_scherm)
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
        button("Sound off", 50, 130, 350, 50, yellow, red, sound_off)
        button("Sound on", 400, 130, 350, 50, yellow, red, sound_on)
        button("Volume down", 50, 230, 350, 50, yellow, red, volumedown)
        button("Volume up", 400, 230, 350, 50, yellow, red, volumeup)
        button("Back", 50, 500, 700, 50, yellow, red, Main_scherm)
        clock.tick(15)  #refresh rate van 15
        pygame.display.flip()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pygame.mixer.music.play(-1)
Main_scherm()
Kaart_scherm()
Navigatie_scherm()
quit()
