from globals import *
from atari import atari

andere = None
map_x, map_y = 10, 10
Display_map = ""
map_text = ""

#------------------------------------------------------------------------------------------------------------------------

intro, Introduction, gameExit,playing, players, throwdice = True, False, False, False, False, 0
gameDisplay = pygame.display.set_mode((display_width, display_height))  # init resolution
pygame.display.set_caption('Roadmap Netherlands')  # window naam
clock = pygame.time.Clock()     # nodig voor Refresh Rate
_image_library = {}     # global list

#-------------------------------------------------------------------------------------------------------------------------

def button(msg,x,y,w,h,ic,ac,action=None):
    """functie om een knop te maken (text,x,y,width,height,kleur, hover kleur, actie)"""
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

def text(msg, x, y):
    """functie om tekst te maken (text,x,y,width,height)"""
    smallText = pygame.font.SysFont("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
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

def map(naam, x,y):
    gameDisplay.blit(naam, (x,y))
    pygame.draw.rect(gameDisplay, white, (700, 220, 535, 450)) # map_colour
    text(map_text, 700, 220)

def A1():
    global andere
    andere = True
    global Display_map
    Display_map = map_A1
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum 1"

def A2():
    global andere
    andere = True
    global Display_map
    Display_map = map_A2
    map(Display_map, map_x, map_y)
    map_text = "Lorem ipsum 2"


def A4():
    global andere
    andere = True
    global Display_map
    Display_map = map_A4
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum 3"


def A5():
    global andere
    andere = True
    global Display_map
    Display_map = map_A5
    map(Display_map, map_x,map_y)


def A6():
    global andere
    andere = True
    global Display_map
    Display_map = map_A6
    map(Display_map, map_x,map_y)


def A7():
    global andere
    andere = True
    global Display_map
    Display_map = map_A7
    map(Display_map, map_x,map_y)


def A8():
    global andere
    global Display_map
    Display_map = map_A8
    andere = True
    map(Display_map, map_x,map_y)


def A9():
    global andere
    andere = True
    global Display_map
    Display_map = map_A9
    map(Display_map, map_x,map_y)


def A10():
    global andere
    andere = True
    global Display_map
    Display_map = map_A10
    map(Display_map, map_x,map_y)


def A12():
    global andere
    andere = True
    global Display_map
    Display_map = map_A12
    map(Display_map, map_x,map_y)


def A13():
    global andere
    andere = True
    global Display_map
    Display_map = map_A13
    map(Display_map, map_x,map_y)


def A15():
    global andere
    andere = True
    global Display_map
    Display_map = map_A15
    map(Display_map, map_x,map_y)


def A16():
    global andere
    andere = True
    global Display_map
    Display_map = map_A16
    map(Display_map, map_x,map_y)


def A17():
    global andere
    andere = True
    global Display_map
    Display_map = map_A17
    map(Display_map, map_x,map_y)


def A18():
    global andere
    andere = True
    global Display_map
    Display_map = map_A18
    map(Display_map, map_x,map_y)


def A19():
    global andere
    andere = True
    global Display_map
    Display_map = map_A19
    map(Display_map, map_x,map_y)


def A20():
    global andere
    andere = True
    global Display_map
    Display_map = map_A20
    map(Display_map, map_x,map_y)


def A27():
    global andere
    andere = True
    global Display_map
    Display_map = map_A27
    map(Display_map, map_x,map_y)


def A28():
    global andere
    andere = True
    global Display_map
    Display_map = map_A28
    map(Display_map, map_x,map_y)


def A29():
    global andere
    andere = True
    global Display_map
    Display_map = map_A29
    map(Display_map, map_x,map_y)


def A30():
    global andere
    andere = True
    global Display_map
    Display_map = map_A30
    map(Display_map, map_x,map_y)


def A31():
    global andere
    andere = True
    global Display_map
    Display_map = map_A31
    map(Display_map, map_x,map_y)


def A32():
    global andere
    andere = True
    global Display_map
    Display_map = map_A32
    map(Display_map, map_x,map_y)


def A35():
    global andere
    andere = True
    global Display_map
    Display_map = map_A35
    map(Display_map, map_x,map_y)


def A37():
    global andere
    andere = True
    global Display_map
    Display_map = map_A37
    map(Display_map, map_x,map_y)


def A44():
    global andere
    andere = True
    global Display_map
    Display_map = map_A44
    map(Display_map, map_x,map_y)


def A50():
    global andere
    andere = True
    global Display_map
    Display_map = map_A50
    map(Display_map, map_x,map_y)


def A58():
    global andere
    andere = True
    global Display_map
    Display_map = map_A58
    map(Display_map, map_x,map_y)


def A59():
    global andere
    andere = True
    global Display_map
    Display_map = map_A59
    map(Display_map, map_x,map_y)


def A65():
    global andere
    andere = True
    global Display_map
    Display_map = map_A65
    map(Display_map, map_x,map_y)


def A67():
    global andere
    andere = True
    global Display_map
    Display_map = map_A67
    map(Display_map, map_x,map_y)


def A73():
    global andere
    andere = True
    global Display_map
    Display_map = map_A73
    map(Display_map, map_x,map_y)


def A76():
    global andere
    andere = True
    global Display_map
    Display_map = map_A76
    map(Display_map, map_x,map_y)


def A77():
    global andere
    andere = True
    global Display_map
    Display_map = map_A77
    map(Display_map, map_x,map_y)


def A79():
    global andere
    andere = True
    global Display_map
    Display_map = map_A79
    map(Display_map, map_x,map_y)

def A200():
    global andere
    andere = True
    global Display_map
    Display_map = map_A200
    map(Display_map, map_x,map_y)

def reset():
    global andere
    andere = False
    global Display_map
    Display_map = map_image
    map(Display_map, map_x,map_y)
    
#--------------------------------------------------------------------------------------------------------------

def Main_scherm():   #main menu scherm
    Instruction, Intro = False, True
    andere = False
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
        button("X", 1200, 100, 70, 50, yellow, red, quit)

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
        map(map_image,map_x,10)

        # button vars
        x1 = 700
        nextX = 60
        y1 = 15
        nextY = 50
        # button row 1
        button("A1", x1, y1, 53, 30, yellow, red, A1)
        button("A2", x1 + nextX, y1, 53, 30, yellow, red, A2)
        button("A4", x1 + nextX * 2, y1, 53, 30, yellow, red, A4)
        button("A5", x1 + nextX * 3, y1, 53, 30, yellow, red, A5)
        button("A6", x1 + nextX * 4, y1, 53, 30, yellow, red, A6)
        button("A7", x1 + nextX * 5, y1, 53, 30, yellow, red, A7)
        button("A8", x1 + nextX * 6, y1, 53, 30, yellow, red, A8)
        button("A9", x1 + nextX * 7, y1, 53, 30, yellow, red, A9)
        button("A10", x1 + nextX * 8, y1, 53, 30, yellow, red, A10)

        # button row 2
        button("A12", x1, y1 + nextY, 53, 30, yellow, red, A12)
        button("A13", x1 + nextX, y1 + nextY, 53, 30, yellow, red, A13)
        button("A15", x1 + nextX * 2, y1 + nextY, 53, 30, yellow, red, A15)
        button("A16", x1 + nextX * 3, y1 + nextY, 53, 30, yellow, red, A16)
        button("A17", x1 + nextX * 4, y1 + nextY, 53, 30, yellow, red, A17)
        button("A18", x1 + nextX * 5, y1 + nextY, 53, 30, yellow, red, A18)
        button("A20", x1 + nextX * 6, y1 + nextY, 53, 30, yellow, red, A20)
        button("A27", x1 + nextX * 7, y1 + nextY, 53, 30, yellow, red, A27)
        button("A28", x1 + nextX * 8, y1 + nextY, 53, 30, yellow, red, A28)

        # button row 3
        button("A29", x1, y1 + nextY * 2, 53, 30, yellow, red, A29)
        button("A30", x1 + nextX, y1 + nextY * 2, 53, 30, yellow, red, A30)
        button("A31", x1 + nextX * 2, y1 + nextY * 2, 53, 30, yellow, red, A31)
        button("A32", x1 + nextX * 3, y1 + nextY * 2, 53, 30, yellow, red, A32)
        button("A35", x1 + nextX * 4, y1 + nextY * 2, 53, 30, yellow, red, A35)
        button("A37", x1 + nextX * 5, y1 + nextY * 2, 53, 30, yellow, red, A37)
        button("A44", x1 + nextX * 6, y1 + nextY * 2, 53, 30, yellow, red, A44)
        button("A50", x1 + nextX * 7, y1 + nextY * 2, 53, 30, yellow, red, A50)
        button("A58", x1 + nextX * 8, y1 + nextY * 2, 53, 30, yellow, red, A58)

        # button row 4
        button("A59", x1, y1 + nextY * 3, 53, 30, yellow, red, A59)
        button("A65", x1 + nextX, y1 + nextY * 3, 53, 30, yellow, red, A65)
        button("A67", x1 + nextX * 2, y1 + nextY * 3, 53, 30, yellow, red, A67)
        button("A73", x1 + nextX * 3, y1 + nextY * 3, 53, 30, yellow, red, A73)
        button("A76", x1 + nextX * 4, y1 + nextY * 3, 53, 30, yellow, red, A76)
        button("A77", x1 + nextX * 5, y1 + nextY * 3, 53, 30, yellow, red, A77)
        button("A79", x1 + nextX * 6, y1 + nextY * 3, 53, 30, yellow, red, A79)
        button("A200", x1 + nextX * 7, y1 + nextY * 3, 53, 30, yellow, red, A200)
        button("EE_1", x1 + nextX * 8, y1 + nextY * 3, 53, 30, yellow, red, atari)
        
        # button back
        button("back", 1200, 700, 53, 30, yellow, red, Main_scherm)
        button("deselecteer", 800, 700, 70, 30, yellow, red, reset)
        
        if andere == True:
            map(Display_map, map_x,map_y)

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