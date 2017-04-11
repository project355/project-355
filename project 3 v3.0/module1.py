import pygame, time, psycopg2
import eztext
import math

pygame.init()


display_width = 1300
display_height = 800
pygame.mixer.music.load("poi.wav")

# globals
x = (display_width * 0.45)
y = (display_height * 0.8)
pygame.display.set_caption('Roadmap Netherlands') # titel of pygame frame

# image 637x750
title = pygame.image.load('images/Roadmap.png')
map_image = pygame.image.load('images/wegenkaartV2.png')
map_A1 = pygame.image.load('images/A1.jpg')
map_A2 = pygame.image.load('images/A2.jpg')
map_A4 = pygame.image.load('images/A4.jpg')
map_A5 = pygame.image.load('images/A5.jpg')
map_A6 = pygame.image.load('images/A6.jpg')
map_A7 = pygame.image.load('images/A7.jpg')
map_A8 = pygame.image.load('images/A8.jpg')
map_A9 = pygame.image.load('images/A9.jpg')
map_A10 = pygame.image.load('images/A10.jpg')
map_A12 = pygame.image.load('images/A12.jpg')
map_A13 = pygame.image.load('images/A13.jpg')
map_A15 = pygame.image.load('images/A15.jpg')
map_A16 = pygame.image.load('images/A16.jpg')
map_A17 = pygame.image.load('images/A17.jpg')
map_A18 = pygame.image.load('images/A18.jpg')
map_A20 = pygame.image.load('images/A20.jpg')
map_A27 = pygame.image.load('images/A27.jpg')
map_A28 = pygame.image.load('images/A28.jpg')
map_A29 = pygame.image.load('images/A29.jpg')
map_A30 = pygame.image.load('images/A30.jpg')
map_A31 = pygame.image.load('images/A31.jpg')
map_A32 = pygame.image.load('images/A32.jpg')
map_A35 = pygame.image.load('images/A35.jpg')
map_A37 = pygame.image.load('images/A37.jpg')
map_A44 = pygame.image.load('images/A44.jpg')
map_A50 = pygame.image.load('images/A50.jpg')
map_A58 = pygame.image.load('images/A58.jpg')
map_A59 = pygame.image.load('images/A59.jpg')
map_A65 = pygame.image.load('images/A65.jpg')
map_A67 = pygame.image.load('images/A67.jpg')
map_A73 = pygame.image.load('images/A73.jpg')
map_A76 = pygame.image.load('images/A76.jpg')
map_A77 = pygame.image.load('images/A77.jpg')
map_A79 = pygame.image.load('images/A79.jpg')
map_A200 = pygame.image.load('images/A200.jpg')

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



andere = None
map_x, map_y = 10, 10
Display_map = ""

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

def atari():
    block_width = 23
    block_height = 15
    class Block(pygame.sprite.Sprite):
        """This class represents each block that will get knocked out by the ball
        It derives from the "Sprite" class in Pygame """

        def __init__(self, color, x, y):
            """ Constructor. Pass in the color of the block,
                and its x and y position. """

            # Call the parent class (Sprite) constructor
            super().__init__()

            # Create the image of the block of appropriate size
            # The width and height are sent as a list for the first parameter.
            self.image = pygame.Surface([block_width, block_height])

            # Fill the image with the appropriate color
            self.image.fill(color)

            # Fetch the rectangle object that has the dimensions of the image
            self.rect = self.image.get_rect()

            # Move the top left of the rectangle to x,y.
            # This is where our block will appear..
            self.rect.x = x
            self.rect.y = y


    class Ball(pygame.sprite.Sprite):
        """ This class represents the ball
            It derives from the "Sprite" class in Pygame """

        # Speed in pixels per cycle
        speed = 10.0

        # Floating point representation of where the ball is
        x = 0.0
        y = 240.0

        # Direction of ball (in degrees)
        direction = 200

        width = 10
        height = 10

        # Constructor. Pass in the color of the block, and its x and y position
        def __init__(self):
            # Call the parent class (Sprite) constructor
            super().__init__()

            # Create the image of the ball
            self.image = pygame.Surface([self.width, self.height])

            # Color the ball
            self.image.fill(white)

            # Get a rectangle object that shows where our image is
            self.rect = self.image.get_rect()

            # Get attributes for the height/width of the screen
            self.screenheight = pygame.display.get_surface().get_height()
            self.screenwidth = pygame.display.get_surface().get_width()

        def bounce(self, diff):
            """ This function will bounce the ball
                off a horizontal surface (not a vertical one) """

            self.direction = (180 - self.direction) % 360
            self.direction -= diff

        def update(self):
            """ Update the position of the ball. """
            # Sine and Cosine work in degrees, so we have to convert them
            direction_radians = math.radians(self.direction)

            # Change the position (x and y) according to the speed and direction
            self.x += self.speed * math.sin(direction_radians)
            self.y -= self.speed * math.cos(direction_radians)

            # Move the image to where our x and y are
            self.rect.x = self.x
            self.rect.y = self.y

            # Do we bounce off the top of the screen?
            if self.y <= 0:
                self.bounce(0)
                self.y = 1

            # Do we bounce off the left of the screen?
            if self.x <= 0:
                self.direction = (360 - self.direction) % 360
                self.x = 1

            # Do we bounce of the right side of the screen?
            if self.x > self.screenwidth - self.width:
                self.direction = (360 - self.direction) % 360
                self.x = self.screenwidth - self.width - 1

            # Did we fall off the bottom edge of the screen?
            if self.y > 800:
                return True
            else:
                return False


    class Player(pygame.sprite.Sprite):
        """ This class represents the bar at the bottom that the
        player controls. """

        def __init__(self):
            """ Constructor for Player. """
            # Call the parent's constructor
            super().__init__()

            self.width = 75
            self.height = 15
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill((white))

            # Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.screenheight = pygame.display.get_surface().get_height()
            self.screenwidth = pygame.display.get_surface().get_width()

            self.rect.x = 0
            self.rect.y = self.screenheight-self.height

        def update(self):
            """ Update the player position. """
            # Get where the mouse is
            pos = pygame.mouse.get_pos()
            # Set the left side of the player bar to the mouse position
            self.rect.x = pos[0]
            # Make sure we don't push the player paddle
            # off the right side of the screen
            if self.rect.x > self.screenwidth - self.width:
                self.rect.x = self.screenwidth - self.width

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([1300, 800])

    # Set the title of the window
    pygame.display.set_caption('Breakout')

    # Enable this to make the mouse disappear when over our window

    # This is a font we use to draw text on the screen (size 36)
    font = pygame.font.Font(None, 36)

    # Create a surface we can draw on
    background = pygame.Surface(screen.get_size())

    # Create sprite lists
    blocks = pygame.sprite.Group()
    balls = pygame.sprite.Group()
    allsprites = pygame.sprite.Group()

    # Create the player paddle object
    player = Player()
    allsprites.add(player)

    # Create the ball
    ball = Ball()
    allsprites.add(ball)
    balls.add(ball)

    # The top of the block (y position)
    top = 80

    # Number of blocks to create
    blockcount = 64

    # --- Create blocks

    # Five rows of blocks
    for row in range(10):
        # 32 columns of blocks
        for column in range(0, blockcount):
            # Create a block (color,x,y)
            block = Block(blue, column * (block_width + 2) + 1, top)
            blocks.add(block)
            allsprites.add(block)
        # Move the top of the next row down
        top += block_height + 2

    # Clock to limit speed
    clock = pygame.time.Clock()

    # Is the game over?
    game_over = False

    # Exit the program?
    exit_program = False

    # Main program loop
    while not exit_program:

        # Limit to 30 fps
        clock.tick(30)

        # Clear the screen
        screen.fill(black)

        # Process the events in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_program = True

        # Update the ball and player position as long
        # as the game is not over.
        if not game_over:
            # Update the player and ball positions
            player.update()
            game_over = ball.update()

        # If we are done, print game over
        if game_over:
            text = font.render("Game Over", True, white)
            textpos = text.get_rect(centerx=background.get_width()/2)
            textpos.top = 300
            screen.blit(text, textpos)

        # See if the ball hits the player paddle
        if pygame.sprite.spritecollide(player, balls, False):
            # The 'diff' lets you try to bounce the ball left or right
            # depending where on the paddle you hit it
            diff = (player.rect.x + player.width/2) - (ball.rect.x+ball.width/2)

            # Set the ball's y position in case
            # we hit the ball on the edge of the paddle
            ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
            ball.bounce(diff)

        # Check for collisions between the ball and the blocks
        deadblocks = pygame.sprite.spritecollide(ball, blocks, True)

        # If we actually hit a block, bounce the ball
        if len(deadblocks) > 0:
            ball.bounce(0)

            # Game ends if all the blocks are gone
            if len(blocks) == 0:
                game_over = True

        # Draw Everything
        allsprites.draw(screen)
        # Flip the screen and show what we've drawn
        pygame.display.flip()

    if game_over == True:
        start()

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

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (820, 250)
    gameDisplay.blit(TextSurf, TextRect)

def map(naam, x,y):
    gameDisplay.blit(naam, (x,y))
    pygame.draw.rect(gameDisplay, white, (700, 220, 535, 450)) # map_colour, vlak
    message_display(map_text)

def A1():
    global andere
    andere = True
    global Display_map
    Display_map = map_A1
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"

def A2():
    global andere
    andere = True
    global Display_map
    Display_map = map_A2
    global map_text
    map(Display_map, map_x, map_y)
    map_text = "Lorem ipsum"


def A4():
    global andere
    andere = True
    global Display_map
    Display_map = map_A4
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A5():
    global andere
    andere = True
    global Display_map
    Display_map = map_A5
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"

def A6():
    global andere
    andere = True
    global Display_map
    Display_map = map_A6
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A7():
    global andere
    andere = True
    global Display_map
    Display_map = map_A7
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A8():
    global andere
    andere = True
    global Display_map
    Display_map = map_A8
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A9():
    global andere
    andere = True
    global Display_map
    Display_map = map_A9
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A10():
    global andere
    andere = True
    global Display_map
    Display_map = map_A10
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A12():
    global andere
    andere = True
    global Display_map
    Display_map = map_A12
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A13():
    global andere
    andere = True
    global Display_map
    Display_map = map_A13
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"

def A15():
    global andere
    andere = True
    global Display_map
    Display_map = map_A15
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A16():
    global andere
    andere = True
    global Display_map
    Display_map = map_A16
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A17():
    global andere
    andere = True
    global Display_map
    Display_map = map_A17
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A18():
    global andere
    andere = True
    global Display_map
    Display_map = map_A18
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A19():
    global andere
    andere = True
    global Display_map
    Display_map = map_A19
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A20():
    global andere
    andere = True
    global Display_map
    Display_map = map_A20
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A27():
    global andere
    andere = True
    global Display_map
    Display_map = map_A27
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A28():
    global andere
    andere = True
    global Display_map
    Display_map = map_A28
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A29():
    global andere
    andere = True
    global Display_map
    Display_map = map_A29
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A30():
    global andere
    andere = True
    global Display_map
    Display_map = map_A30
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A31():
    global andere
    andere = True
    global Display_map
    Display_map = map_A31
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A32():
    global andere
    andere = True
    global Display_map
    Display_map = map_A32
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A35():
    global andere
    andere = True
    global Display_map
    Display_map = map_A35
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A37():
    global andere
    andere = True
    global Display_map
    Display_map = map_A37
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A44():
    global andere
    andere = True
    global Display_map
    Display_map = map_A44
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A50():
    global andere
    andere = True
    global Display_map
    Display_map = map_A50
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A58():
    global andere
    andere = True
    global Display_map
    Display_map = map_A58
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A59():
    global andere
    andere = True
    global Display_map
    Display_map = map_A59
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A65():
    global andere
    andere = True
    global Display_map
    Display_map = map_A65
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A67():
    global andere
    andere = True
    global Display_map
    Display_map = map_A67
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A73():
    global andere
    andere = True
    global Display_map
    Display_map = map_A73
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A76():
    global andere
    andere = True
    global Display_map
    Display_map = map_A76
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A77():
    global andere
    andere = True
    global Display_map
    Display_map = map_A77
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"


def A79():
    global andere
    andere = True
    global Display_map
    Display_map = map_A79
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"

def A200():
    global andere
    andere = True
    global Display_map
    Display_map = map_A200
    global map_text
    map(Display_map, map_x,map_y)
    map_text = "Lorem ipsum"

def reset():
    global andere
    andere = False
    global Display_map
    Display_map = map_image
    map(Display_map, map_x,map_y)
    global map_text
    map(Display_map, map_x, map_y)
    map_text = ""









#--------------------------------------------------------------------------------------------------------------

def Main_scherm():   #main menu scherm
    Instruction, Intro = False, True
    reset()
    x, y, mov_x, mov_y = 0,0,6,6
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(map_colour)

        map(title, 50, 52)
        button("kaart", 50, 230, 700, 50,yellow, red, Kaart_scherm)
        button("Navigatie", 50, 330, 700, 50, yellow, red, Navigatie_scherm)
        button("Opties", 50, 430, 700, 50, yellow, red, Opties_scherm)
        button("Beoordeling", 50, 530, 700, 50, yellow, red, beoordeling_scherm)
        button("X", 1200, 100, 70, 50, yellow, red, quit)


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
        button("Terug", 1200, 700, 53, 30, yellow, red, Main_scherm)
        button("deselecteer", 800, 700, 70, 30, yellow, red, reset)


        if andere == True:
            map(Display_map, map_x,map_y)

        clock.tick(15)  #refresh rate van 15
        pygame.display.flip()

def beoordeling_scherm():
    Instruction, Intro = True, False
    while Instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(map_colour)

        # Connect to an existing database
        #conn = psycopg2.connect("dbname=project3 user=postgres password=wachtwoord")

        # Open a cursor to perform database operations
        #cur = conn.cursor()
        #cur.execute("UPDATE Players SET wins = wins +1 WHERE naam = 'Penkie'")
        #cur.execute("SELECT * FROM Players")
        # fetch all of the rows from the query
        #data = cur.fetchall ()
    # print the rows
        #for row in data :
        #    print("Naam",row[0], "Wins",row[1], "Losses",row[2])
        #    pygame.display.flip()
        #    cur.close()

        #conn.commit()

        # Close communication with the database
        #cur.close()
        #conn.close()

            # button vars
        x1 = 700
        nextX = 60
        y1 = 15
        nextY = 50
        y2 = 50

        button("A1", 43, y1, 50, 30, yellow, red, A1)
        button("A2", 115, y1, 50, 30, yellow, red, A2)
        button("A4", 185, y1, 50, 30, yellow, red, A4)
        button("A5", 255, y1, 50, 30, yellow, red, A5)
        button("A6", 325, y1, 50, 30, yellow, red, A6)
        button("A7", 395, y1, 50, 30, yellow, red, A7)
        button("A8", 465, y1, 50, 30, yellow, red, A8)
        button("A9", 535, y1, 50, 30, yellow, red, A9)
        button("A10",605, y1, 50, 30, yellow, red, A10)

        # button row 2
        button("A12", 675, y1, 50, 30, yellow, red, A12)
        button("A13", 745, y1, 50, 30, yellow, red, A13)
        button("A15", 815, y1, 50, 30, yellow, red, A15)
        button("A16", 885, y1, 50, 30, yellow, red, A16)
        button("A17", 955, y1, 50, 30, yellow, red, A17)
        button("A18", 1025, y1, 50, 30, yellow, red, A18)
        button("A20", 1090, y1, 50, 30, yellow, red, A20)
        button("A27", 1155, y1, 50, 30, yellow, red, A27)
        button("A28", 1220, y1, 50, 30, yellow, red, A28)

        # button row 3
        button("A29", 43, y2, 50, 30, yellow, red, A29)
        button("A30", 115, y2, 50, 30, yellow, red, A30)
        button("A31", 185, y2, 50, 30, yellow, red, A31)
        button("A32", 255, y2, 50, 30, yellow, red, A32)
        button("A35", 325, y2, 50, 30, yellow, red, A35)
        button("A37", 395, y2, 50, 30, yellow, red, A37)
        button("A44", 465, y2, 50, 30, yellow, red, A44)
        button("A50", 535, y2, 50, 30, yellow, red, A50)
        button("A58", 605, y2, 50, 30, yellow, red, A58)

        # button row 4
        button("A59", 675, y2, 53, 30, yellow, red, A59)
        button("A65", 745, y2, 53, 30, yellow, red, A65)
        button("A67", 815, y2, 53, 30, yellow, red, A67)
        button("A73", 885, y2, 53, 30, yellow, red, A73)
        button("A76", 955, y2, 53, 30, yellow, red, A76)
        button("A77", 1025, y2, 53, 30, yellow, red, A77)
        button("A79", 1090, y2, 53, 30, yellow, red, A79)
        button("A200",1155, y2, 53, 30, yellow, red, A200)
        button("EE_1",1220, y2, 53, 30, yellow, red, atari)

        button("Terug", 150, 700, 300, 50, yellow, red, Main_scherm)
        button("Verstuur", 850, 700, 300, 50, yellow, red, Main_scherm)
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
        button("Terug", 50, 500, 700, 50, yellow, red, Main_scherm)
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
