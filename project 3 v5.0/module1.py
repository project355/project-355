import pygame, time, psycopg2, psycopg2.extras, random
import eztext
import math
import sys
import pie_demo
import barChart
# alle imports

pygame.init() # pygame wordt gestart

display_width = 1300
display_height = 800 # de afmetingen van het scherm
pygame.mixer.music.load("poi.wav") # de muziek wordt ingeladen

# globals
x = (display_width * 0.45)
y = (display_height * 0.8)
pygame.display.set_caption('Roadmap Netherlands') # titel of pygame frame
map_text = ""
map2_text = ""
naam_snelweg = "     "
file_nummer = 0
wegdek_nummer = 0
andere = None
map_x, map_y = 10, 10
Display_map = ""
rating_files = False
rating_wegdek = False
beoordeling_file = 0
beoordeling_wegdek = 0
file_rating_avg = ""
weg_rating_avg = ""
tijd = ''
oordeel = 0

# image 637x750
# alle afbeeldingen worden hier ingeladen
title = pygame.image.load('images/Roadmap.png')
car = pygame.image.load('images/car.png')
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
volle_ster = pygame.image.load('images/volle_ster.png')
lege_ster = pygame.image.load('images/lege_ster.png')
map_berlijn = pygame.image.load('images/A200.jpg')
map_parijs = pygame.image.load('images/A200.jpg')
map_haarlem = pygame.image.load('images/A200.jpg')
map_amsterdam= pygame.image.load('images/A200.jpg')
map_denhaag = pygame.image.load('images/A200.jpg')
map_middelburg = pygame.image.load('images/A200.jpg')
map_utrecht = pygame.image.load('images/A200.jpg')
map_denbosch = pygame.image.load('images/A200.jpg')
map_maastricht = pygame.image.load('images/A200.jpg')
map_arnhem = pygame.image.load('images/A200.jpg')
map_zwolle = pygame.image.load('images/A200.jpg')
map_assen = pygame.image.load('images/A200.jpg')
map_groningen = pygame.image.load('images/A200.jpg')
map_leeuwarden = pygame.image.load('images/A200.jpg')
map_lelystad = pygame.image.load('images/A200.jpg')

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
clock = pygame.time.Clock()     #nodig voor Refresh Rate
_image_library = {}     #global list

#-------------------------------------------------------------------------------------------------------------------------

########## database start ##########

# connextion #
try:
    conn = psycopg2.connect("dbname='project3' user='postgres' password='root'")
except:
    print ("no connection")

# weg -> naam, gemiddelde file teverdenheid, gemiddelde wegdek tevredenheid 
ccw = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    ccw.execute("""SELECT naam, gft, gwt  FROM weg""")
except:
    print("I can't select weg")

# persoon -> id_persoon, file teverdenheid, wegdek tevredenheid, tijd
ccp = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    ccp.execute("""SELECT id_persoon, ft, wt, tijd FROM persoon""")
except:
    print("I can't select persoon")

### weg (uit)###
def count_weg(naam):
    """select count(weg.naam)"""
    try:
        ccw.execute("SELECT count(naam) FROM weg where naam = '"+naam+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccw.fetchall()
    for row in result:
        return row[0]

def weg_naam():
    """select weg.naam"""
    try:
        ccw.execute("SELECT naam FROM weg")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccw.fetchall()
    for row in result:
        return row[0]

def weg_gft(naam):
    """select weg.gft on roadname"""
    try:
        ccw.execute("SELECT gft FROM weg WHERE naam = '"+naam+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccw.fetchall()
    for row in result:
        return row[0]

def weg_gwt(naam):
    """select weg.gwt on roadname"""
    try:
        ccw.execute("SELECT gwt FROM weg WHERE naam = '"+naam+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccw.fetchall()
    for row in result:
        return row[0]

### persoon (uit)###
def count_persoon(weg):
    """select count(persoon.id_persoon)"""
    try:
        ccp.execute("SELECT count(id_persoon) FROM persoon WHERE weg = '"+weg+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccp.fetchall()
    for row in result:
        return row[0]

def persoon_id_persoon():
    """select persoon.id_persoon"""
    try:
        ccp.execute("SELECT id_persoon FROM persoon")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccp.fetchall()
    for row in result:
        return row[0]

def persoon_ft(weg):
    """select persoon.ft on id_persoon"""
    try:
        ccp.execute("SELECT ft FROM persoon WHERE weg = '"+weg+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccp.fetchall()
    for row in result:
        return row[0]

def persoon_wt(weg):
    """select persoon.wt on id_persoon"""
    try:
        ccp.execute("SELECT wt FROM persoon WHERE weg = '"+weg+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccp.fetchall()
    for row in result:
        return row[0]

def persoon_tijd(weg):
    """select persoon.wt on id_persoon"""
    try:
        ccp.execute("SELECT tijd FROM persoon WHERE weg = '"+weg+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccp.fetchall()
    for row in result:
        return row[0]

### weg (in)###
def update_weg(weg, gft, gwt):
    """gemiddelde beoordeling importeren"""
    try:
        ccw.execute("""UPDATE weg SET gft = %s, gwt = %s WHERE naam === %s""" "'"+weg+"'", (gft, gwt))
    except Exception as error:
        return(error)
    conn.commit()

### persoon (in)###
def insert_into_persoon(weg, ft, wt, tijd):
    """beoordeling persoon importeren"""
    try:
        ccp.execute("""insert into persoon(id_persoon,weg, ft,wt, tijd) Values (nextval('id_persoon_sequence'),%s, %s,%s, %s) """, (weg,ft, wt, tijd))
    except Exception as error:
        return(error)
    conn.commit()

### avg persoon ###

def avg_p_file(weg, p_count):
    """select count(persoon.id_persoon)"""
    global file_rating_avg
    global weg_rating_avg
    if(p_count < 1):
        file_rating_avg = "%0.1f" % 0
        weg_rating_avg = "%0.1f" % 0
        print(0, 0)
        #return None
    else:
        try:
            ccp.execute("SELECT * FROM persoon WHERE weg = '"+weg+"'")
        except Exception as error:
            return(error)
        conn.commit()
        result = ccp.fetchall()

        file_rating, weg_rating = 0, 0
        for row in result:
            #print(row[1]) # weg
            #print(row[2]) # file rating
            #print(row[3]) # weg rating
            file_rating = file_rating + row[2]
            weg_rating = weg_rating + row[3]
        print(file_rating, weg_rating)
        if (file_rating < 1 | weg_rating < 1):
            file_rating_avg = "%0.1f" % 0
            weg_rating_avg = "%0.1f" % 0
            #return None
        else:
            file_rating_avg = "%0.1f" % (file_rating / p_count)
            weg_rating_avg = "%0.1f" % (weg_rating / p_count)
            #return None

########## database end ##########

def pop_up(): # het pop_up scherm  kan met deze functie aangeroepen worden
    if oordeel == 1:
        quit()
    else:
        pygame.display.set_mode((display_width,display_height))
        pygame.display.set_caption('Wilt u nog wat voor ons doen?')
        Instruction, Intro = False, True
        x, y, mov_x, mov_y = 0,0,6,6
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            gameDisplay.fill(map_colour)
        
            button("ja", 50, 230, 700, 50,yellow, red, beoordeling_scherm)
            button("nee", 50, 330, 700, 50, yellow, red, quit)
            message_display2('Wilt u de wegen beoordelen?:', 650, 100, 75)
            pygame.display.flip()

def grafiek1(): # hiermee wordt de grafiek over meest verongelukte voertuigen aangeroepen
    pie_demo.poi()

def grafiek2(): # hiermee wordt de grafiek over de meest gevaarlijke a-wegen aangeroepen
    barChart.poi()

def button(msg,x,y,w,h,ic,ac,action=None): # dit is de function die een button aanmaakt (text,x,y,width,height,kleur, hover kleur, actie)
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
            time.sleep(3)
            screen.blit(text, textpos)
            Kaart_scherm()

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
        Kaart_scherm()

def text_objects(text, font):   #functie om tekst te tonen
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def sound_off(): #de function die het geluid uit zet
    """turn sound off"""
    pygame.mixer.music.stop()

def sound_on(): #de functie die het geluid aan zet
    """turn sound on"""
    pygame.mixer.music.play(-1)

def volumedown(): #de functie die het volume lager zet
    volume = pygame.mixer.music.get_volume()
    volume = volume - 0.1
    pygame.mixer.music.set_volume(volume)

def volumeup(): #de functie die het volume hoger zet
    volume = pygame.mixer.music.get_volume()
    volume = volume + 0.1
    pygame.mixer.music.set_volume(volume)

def message_display2(text, x, y, h): #een functie om een stuk tekst in op een bepaalde plek zet
    largeText = pygame.font.Font('freesansbold.ttf',h)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def message_display(text): #een functie om een stuk tekst te tonen
    largeText = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (925, 250)
    gameDisplay.blit(TextSurf, TextRect)

def map(naam, x,y): #de functie die bij de kaart pagina de afbeelding en tekst veranderd
    gameDisplay.blit(naam, (x,y))
    pygame.draw.rect(gameDisplay, map_colour, (700, 220, 535, 450)) # vlak
    message_display2(map_text, 850, 250, 20) #bovenste stuk tekst, de niet dodelijke ongevallen
    message_display2(map2_text, 815, 300, 20) #onderste stuk tekst, de dodelijke ongevallen
    message_display2(file_rating_avg, 805, 350, 20)
    message_display2(weg_rating_avg, 810, 400, 20)

def sec(naam, x, y):
    gameDisplay.blit(naam, (x,y))
    message_display(map2_text)

class snelweg:#de class met alle dingen omtrent alle snelwegen
#de functions die de tekst en afbeelding aangeven bij de kaart pagina
    def A1():
        global andere
        andere = True
        global Display_map
        Display_map = map_A1 #welke afbeelding het moet worden
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:9638" #het bovenste stuk tekst
        map2_text = "Dodelijke ongevallen:52" #het onderste stuk tekst
        p_count = count_persoon("A1")
        avg_p_file("A1", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A2():
        global andere
        andere = True
        global Display_map
        Display_map = map_A2
        global map_text
        global map2_text
        map(Display_map, map_x, map_y)
        map_text = "Niet-dodelijke ongevallen:2003"
        map2_text = "Dodelijke ongevallen:21"
        p_count = count_persoon("A2")
        avg_p_file("A2", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A4():
        global andere
        andere = True
        global Display_map
        Display_map = map_A4
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:3456"
        map2_text = "Dodelijke ongevallen:25"
        p_count = count_persoon("A4")
        avg_p_file("A4", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A5():
        global andere
        andere = True
        global Display_map
        Display_map = map_A5
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:2090"
        map2_text = "Dodelijke ongevallen:18"
        p_count = count_persoon("A5")
        avg_p_file("A5", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A6():
        global andere
        andere = True
        global Display_map
        Display_map = map_A6
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:1195"
        map2_text = "Dodelijke ongevallen:8"
        p_count = count_persoon("A6")
        avg_p_file("A6", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A7():
        global andere
        andere = True
        global Display_map
        Display_map = map_A7
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7687"
        map2_text = "Dodelijke ongevallen:28"
        p_count = count_persoon("A7")
        avg_p_file("A7", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A8():
        global andere
        andere = True
        global Display_map
        Display_map = map_A8
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:6859"
        map2_text = "Dodelijke ongevallen:15"
        p_count = count_persoon("A8")
        avg_p_file("A8", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A9():
        global andere
        andere = True
        global Display_map
        Display_map = map_A9
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:6512’"
        map2_text = "Dodelijke ongevallen:19"
        p_count = count_persoon("A9")
        avg_p_file("A9", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A10():
        global andere
        andere = True
        global Display_map
        Display_map = map_A10
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:17"
        p_count = count_persoon("A10")
        avg_p_file("A10", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A12():
        global andere
        andere = True
        global Display_map
        Display_map = map_A12
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:10267"
        map2_text = "Dodelijke ongevallen:32"
        p_count = count_persoon("A12")
        avg_p_file("A12", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A13():
        global andere
        andere = True
        global Display_map
        Display_map = map_A13
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:6159"
        map2_text = "Dodelijke ongevallen:16"
        p_count = count_persoon("A13")
        avg_p_file("A13", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A15():
        global andere
        andere = True
        global Display_map
        Display_map = map_A15
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:9412"
        map2_text = "Dodelijke ongevallen:25"
        p_count = count_persoon("A15")
        avg_p_file("A15", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A16():
        global andere
        andere = True
        global Display_map
        Display_map = map_A16
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:8641"
        map2_text = "Dodelijke ongevallen:28"
        p_count = count_persoon("A16")
        avg_p_file("A16", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A17():
        global andere
        andere = True
        global Display_map
        Display_map = map_A17
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:3244"
        map2_text = "Dodelijke ongevallen:8"
        p_count = count_persoon("A17")
        avg_p_file("A17", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A18():
        global andere
        andere = True
        global Display_map
        Display_map = map_A18
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7749"
        map2_text = "Dodelijke ongevallen:23"
        p_count = count_persoon("A18")
        avg_p_file("A18", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A19():
        global andere
        andere = True
        global Display_map
        Display_map = map_A19
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:5121"
        map2_text = "Dodelijke ongevallen:14"
        p_count = count_persoon("A19")
        avg_p_file("A19", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A20():
        global andere
        andere = True
        global Display_map
        Display_map = map_A20
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:5121"
        map2_text = "Dodelijke ongevallen:17"
        p_count = count_persoon("A20")
        avg_p_file("A20", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A27():
        global andere
        andere = True
        global Display_map
        Display_map = map_A27
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:6489"
        map2_text = "Dodelijke ongevallen:32"
        p_count = count_persoon("A27")
        avg_p_file("A27", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A28():
        global andere
        andere = True
        global Display_map
        Display_map = map_A28
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:4654"
        map2_text = "Dodelijke ongevallen:36"
        p_count = count_persoon("A28")
        avg_p_file("A28", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A29():
        global andere
        andere = True
        global Display_map
        Display_map = map_A29
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:4755"
        map2_text = "Dodelijke ongevallen:15"
        p_count = count_persoon("A29")
        avg_p_file("A29", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A30():
        global andere
        andere = True
        global Display_map
        Display_map = map_A30
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:2322"
        map2_text = "Dodelijke ongevallen:18"
        p_count = count_persoon("A30")
        avg_p_file("A30", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A31():
        global andere
        andere = True
        global Display_map
        Display_map = map_A31
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:2429"
        map2_text = "Dodelijke ongevallen:8"
        p_count = count_persoon("A31")
        avg_p_file("A31", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A32():
        global andere
        andere = True
        global Display_map
        Display_map = map_A32
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7400"
        map2_text = "Dodelijke ongevallen:10"
        p_count = count_persoon("A32")
        avg_p_file("A32", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A35():
        global andere
        andere = True
        global Display_map
        Display_map = map_A35
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:2107"
        map2_text = "Dodelijke ongevallen:21"
        p_count = count_persoon("A35")
        avg_p_file("A35", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A37():
        global andere
        andere = True
        global Display_map
        Display_map = map_A37
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:5533"
        map2_text = "Dodelijke ongevallen:9"
        p_count = count_persoon("A37")
        avg_p_file("A37", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A44():
        global andere
        andere = True
        global Display_map
        Display_map = map_A44
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:8727"
        map2_text = "Dodelijke ongevallen:17"
        p_count = count_persoon("A44")
        avg_p_file("A44", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A50():
        global andere
        andere = True
        global Display_map
        Display_map = map_A50
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:5874"
        map2_text = "Dodelijke ongevallen:23"
        p_count = count_persoon("A50")
        avg_p_file("A50", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A58():
        global andere
        andere = True
        global Display_map
        Display_map = map_A58
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:2779"
        map2_text = "Dodelijke ongevallen:15"
        p_count = count_persoon("A58")
        avg_p_file("A58", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A59():
        global andere
        andere = True
        global Display_map
        Display_map = map_A59
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:4381"
        map2_text = "Dodelijke ongevallen:14"
        p_count = count_persoon("A59")
        avg_p_file("A59", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A65():
        global andere
        andere = True
        global Display_map
        Display_map = map_A65
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:2729"
        map2_text = "Dodelijke ongevallen:8"
        p_count = count_persoon("A65")
        avg_p_file("A65", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A67():
        global andere
        andere = True
        global Display_map
        Display_map = map_A67
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:4381"
        map2_text = "Dodelijke ongevallen:13"
        p_count = count_persoon("A67")
        avg_p_file("A67", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A73():
        global andere
        andere = True
        global Display_map
        Display_map = map_A73
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:2592"
        map2_text = "Dodelijke ongevallen:8"
        p_count = count_persoon("A73")
        avg_p_file("A73", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A76():
        global andere
        andere = True
        global Display_map
        Display_map = map_A76
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:3719"
        map2_text = "Dodelijke ongevallen:10"
        p_count = count_persoon("A76")
        avg_p_file("A76", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A77():
        global andere
        andere = True
        global Display_map
        Display_map = map_A77
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:3449"
        map2_text = "Dodelijke ongevallen:8"
        p_count = count_persoon("A77")
        avg_p_file("A77", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A79():
        global andere
        andere = True
        global Display_map
        Display_map = map_A79
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:3716"
        map2_text = "Dodelijke ongevallen:10"
        p_count = count_persoon("A79")
        avg_p_file("A79", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def A200():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"
        p_count = count_persoon("A200")
        avg_p_file("A200", p_count)
        global file_rating_avg
        file_rating_avg = "File tevredenheid: " + str(file_rating_avg)
        global weg_rating_avg
        weg_rating_avg = "Weg tevredenheid: " + str(weg_rating_avg)

    def nav_berlijn():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"

    def nav_parijs():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"

    def nav_haarlem():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"

    def nav_amsterdam():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"

    def nav_denhaag():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"

    def nav_maastricht():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"

    def nav_arnhem():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"

    def nav_zwolle():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"

    def nav_assen():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"

    def nav_groningen():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"

    def nav_leeuwarden():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"

    def nav_lelystad():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"


    def nav_utrecht():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"


    def nav_middelburg():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"

    def nav_denbosch():
        global andere
        andere = True
        global Display_map
        Display_map = map_A200
        global map_text
        global map2_text
        map(Display_map, map_x,map_y)
        map_text = "Niet-dodelijke ongevallen:7102"
        map2_text = "Dodelijke ongevallen:14"

def reset(): #de functie die de kaart pagina laat terug springen naar de orignele afbeelding en tekst
    global andere
    andere = False
    global Display_map
    global naam_snelweg
    global tijd
    naam_snelweg = "     "
    Display_map = map_image #de afbeelding
    map(Display_map, map_x,map_y)
    global map_text
    global map2_text
    map(Display_map, map_x, map_y)
    map_text = "" #de tekst wordt weer leeg
    map2_text = "" #de tekst wordt weer leeg
    global file_nummer
    file_nummer = 0
    global wegdek_nummer
    wegdeknummer = 0
    tijd = ''
    global file_rating_avg
    file_rating_avg = ""
    global weg_rating_avg
    weg_rating_avg = ""
    global beoordeling_wegdek
    beoordeling_wegdek = 0

def snek(): #de functie die de game "snake" opstart
    def collide(x1, x2, y1, y2, w1, w2, h1, h2):
        if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:return True
        else:return False
    def die(screen, score):  #het dood gaan scherm
        f=pygame.font.SysFont('Arial', 30);t=f.render('Your score was: '+str(score), True, (0, 0, 0));screen.blit(t, (10, 270));pygame.display.update();pygame.time.wait(2000);Main_scherm()
    xs = [290, 290, 290, 290, 290];ys = [290, 270, 250, 230, 210];dirs = 0;score = 0;applepos = (random.randint(0, 590), random.randint(0, 590));pygame.init();s=pygame.display.set_mode((600, 600));pygame.display.set_caption('Snek');appleimage = pygame.Surface((10, 10));appleimage.fill((0, 255, 0));img = pygame.Surface((20, 20));img.fill((255, 0, 0));f = pygame.font.SysFont('Arial', 20);clock = pygame.time.Clock()
    while True:
        clock.tick(10)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                Main_scherm()
                #pygame.display.set_mode((500,500)
           #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_ESCAPE

            elif e.type == pygame.KEYDOWN: #de bewegingen
                if e.key == pygame.K_UP and dirs != 0:dirs = 2
                elif e.key == pygame.K_DOWN and dirs != 2:dirs = 0
                elif e.key == pygame.K_LEFT and dirs != 1:dirs = 3
                elif e.key == pygame.K_RIGHT and dirs != 3:dirs = 1
        i = len(xs)-1
        while i >= 2:
            if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):die(s, score)
            i-= 1
        if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10):score+=1;xs.append(700);ys.append(700);applepos=(random.randint(0,590),random.randint(0,590))
        if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580: die(s, score)
        i = len(xs)-1
        
        while i >= 1:
            xs[i] = xs[i-1];ys[i] = ys[i-1];i -= 1
        
        if dirs==0:ys[0] += 20
        elif dirs==1:xs[0] += 20
        elif dirs==2:ys[0] -= 20
        elif dirs==3:xs[0] -= 20  
              
        s.fill((255, 255, 255))        
        for i in range(0, len(xs)):
            s.blit(img, (xs[i], ys[i]))
        s.blit(appleimage, applepos);t=f.render(str(score), True, (0, 0, 0));s.blit(t, (10, 10));pygame.display.update()

def message_display2(text, x, y, h):
    largeText = pygame.font.Font('freesansbold.ttf',h)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def button2(msg,x,y,w,h,ic,ac,action=None): #de button die wordt gebruikt als je een onzichtbare button wilt
    """functie om een knop te maken (text,x,y,width,height,kleur, hover kleur, actie)"""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:   #als de muis over de knop hovert

        if click[0] == 1 and action != None:        #als je er op klikt, doe actie
            action()

    smallText = pygame.font.SysFont("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def rating(): #de buttons die horen bij het beoordelingen scherm
    gameDisplay.blit(lege_ster, (550,500))
    gameDisplay.blit(lege_ster, (550,300))
    message_display2('welke rating geeft u over de ' + naam_snelweg + ":", 600, 150, 70)
    message_display2('files:', 250, 550, 100)
    #buttons file
    button2("", 550, 500, 100, 100, yellow, red, set.set_file1)
    button2("", 650, 500, 100, 100, yellow, red, set.set_file2)
    button2("", 750, 500, 100, 100, yellow, red, set.set_file3)
    button2("", 850, 500, 100, 100, yellow, red, set.set_file4)
    button2("", 950, 500, 100, 100, yellow, red, set.set_file5)
    #buttons wegdek
    button2("", 550, 300, 100, 100, yellow, red, set.set_wegdek1)
    button2("", 650, 300, 100, 100, yellow, red, set.set_wegdek2)
    button2("", 750, 300, 100, 100, yellow, red, set.set_wegdek3)
    button2("", 850, 300, 100, 100, yellow, red, set.set_wegdek4)
    button2("", 950, 300, 100, 100, yellow, red, set.set_wegdek5)

    message_display2('wegdek:', 250, 350, 100)
    
    button("Ochtend",1220, 300, 50, 30, yellow, red, set.ochtend)
    button("Middag",1220, 400, 50, 30, yellow, red, set.middag)
    button("Avond",1220, 500, 50, 30, yellow, red, set.avond)
    button("Nacht",1220, 600, 50, 30, yellow, red, set.nacht)

class set: #de class die alle functies heeft die de rating knoppen werkende maken
    def set_file1():
        global beoordeling_file
        beoordeling_file = 1
        print(beoordeling_file)
        set.rating_file_1()

    def set_file2():
        global beoordeling_file
        beoordeling_file = 2
        print(beoordeling_file)
        set.rating_file_2()

    def set_file3():
        global beoordeling_file
        beoordeling_file = 3
        print(beoordeling_file)
        set.rating_file_3()

    def set_file4():
        global beoordeling_file
        beoordeling_file = 4
        print(beoordeling_file)
        set.rating_file_4()

    def set_file5():
        global beoordeling_file
        beoordeling_file = 5
        print(beoordeling_file)
        set.rating_file_5()

    def rating_file_1():
        global rating_files
        rating_files = True
        gameDisplay.blit(volle_ster, (550,500))
        global file_nummer
        file_nummer = 1

    def rating_file_2():
        global rating_files
        rating_files = True
        gameDisplay.blit(volle_ster, (650,500))
        set.rating_file_1()
        global file_nummer
        file_nummer = 2

    def rating_file_3():
        global rating_files
        rating_files = True
        gameDisplay.blit(volle_ster, (750,500))
        set.rating_file_2()
        global file_nummer
        file_nummer = 3

    def rating_file_4():
        global rating_files
        rating_files = True
        gameDisplay.blit(volle_ster, (850,500))
        set.rating_file_3()
        global file_nummer
        file_nummer = 4

    def rating_file_5():
        global rating_files
        rating_files = True
        gameDisplay.blit(volle_ster, (950,500))
        set.rating_file_4()
        global file_nummer
        file_nummer = 5

    def set_wegdek1():
        global beoordeling_wegdek
        beoordeling_wegdek = 1
        print(beoordeling_wegdek)
        set.rating_wegdek_1()

    def set_wegdek2():
        global beoordeling_wegdek
        beoordeling_wegdek = 2
        print(beoordeling_wegdek)
        set.rating_wegdek_2()

    def set_wegdek3():
        global beoordeling_wegdek
        beoordeling_wegdek = 3
        print(beoordeling_wegdek)
        set.rating_wegdek_3()

    def set_wegdek4():
        global beoordeling_wegdek
        beoordeling_wegdek = 4
        print(beoordeling_wegdek)
        set.rating_wegdek_4()

    def set_wegdek5():
        global beoordeling_wegdek
        beoordeling_wegdek = 5
        print(beoordeling_wegdek)
        set.rating_wegdek_5()

    def rating_wegdek_1():
        global rating_wegdek
        rating_wegdek = True
        gameDisplay.blit(volle_ster, (550,300))
        global wegdek_nummer
        wegdek_nummer = 1

    def rating_wegdek_2():
        global rating_wegdek
        rating_wegdek = True
        gameDisplay.blit(volle_ster, (650,300))
        set.rating_wegdek_1()
        global wegdek_nummer
        wegdek_nummer = 2

    def rating_wegdek_3():
        global rating_wegdek
        rating_wegdek = True
        gameDisplay.blit(volle_ster, (750,300))
        set.rating_wegdek_2()
        global wegdek_nummer
        wegdek_nummer = 3

    def rating_wegdek_4():
        global rating_wegdek
        rating_wegdek = True
        gameDisplay.blit(volle_ster, (850,300))
        set.rating_wegdek_3()
        global wegdek_nummer
        wegdek_nummer = 4

    def rating_wegdek_5():
        global rating_wegdek
        rating_wegdek = True
        gameDisplay.blit(volle_ster, (950,300))
        set.rating_wegdek_4()
        global wegdek_nummer
        wegdek_nummer = 5
        
    def ochtend():
        global tijd 
        tijd = 'O'
    def middag():
        global tijd
        tijd = 'M'
    def avond():
        global tijd
        tijd = 'A'
    def nacht():
        global tijd
        tijd = 'N'

############################################################################################

#beoordeling_wegdek & beoordeling_file & naam_snelweg & tijd moeten naar de database.
def sent_data(): # de function die de beoordeling in de database verwerkt
    if naam_snelweg != "     " and beoordeling_file != 0 and beoordeling_wegdek != 0 and tijd != '':
        insert_into_persoon(naam_snelweg, beoordeling_file, beoordeling_wegdek, tijd)
        global oordeel
        oordeel = 1
        Main_scherm()
    else:
        message_display2("selecteer een snelweg en beoordeel het wegdek en het aantal files", 630, 650, 35)

class snelweg_query: #de queries over welke snelweg geselecteerd is bij de beoordeling
    def A1_query():
        global naam_snelweg
        naam_snelweg = "A1"

    def A2_query():
        global naam_snelweg
        naam_snelweg = "A2"

    def A4_query():
        global naam_snelweg
        naam_snelweg = "A4"

    def A5_query():
        global naam_snelweg
        naam_snelweg = "A5"

    def A6_query():
        global naam_snelweg
        naam_snelweg = "A6"

    def A7_query():
        global naam_snelweg
        naam_snelweg = "A7"

    def A8_query():
        global naam_snelweg
        naam_snelweg = "A8"

    def A9_query():
        global naam_snelweg
        naam_snelweg = "A9"

    def A10_query():
        global naam_snelweg
        naam_snelweg = "A10"

    def A12_query():
        global naam_snelweg
        naam_snelweg = "A12"

    def A13_query():
        global naam_snelweg
        naam_snelweg = "A13"

    def A15_query():
        global naam_snelweg
        naam_snelweg = "A15"

    def A16_query():
        global naam_snelweg
        naam_snelweg = "A16"

    def A17_query():
        global naam_snelweg
        naam_snelweg = "A17"

    def A18_query():
        global naam_snelweg
        naam_snelweg = "A18"

    def A20_query():
        global naam_snelweg
        naam_snelweg = "A20"

    def A27_query():
        global naam_snelweg
        naam_snelweg = "A27"

    def A28_query():
        global naam_snelweg
        naam_snelweg = "A28"

    def A29_query():
        global naam_snelweg
        naam_snelweg = "A29"

    def A30_query():
        global naam_snelweg
        naam_snelweg = "A30"

    def A31_query():
        global naam_snelweg
        naam_snelweg = "A31"

    def A32_query():
        global naam_snelweg
        naam_snelweg = "A32"

    def A35_query():
        global naam_snelweg
        naam_snelweg = "A35"

    def A37_query():
        global naam_snelweg
        naam_snelweg = "A37"

    def A44_query():
        global naam_snelweg
        naam_snelweg = "A44"

    def A50_query():
        global naam_snelweg
        naam_snelweg = "A50"

    def A58_query():
        global naam_snelweg
        naam_snelweg = "A58"


    def A59_query():
        global naam_snelweg
        naam_snelweg = "A59"

    def A65_query():
        global naam_snelweg
        naam_snelweg = "A65"

    def A67_query():
        global naam_snelweg
        naam_snelweg = "A67"

    def A73_query():
        global naam_snelweg
        naam_snelweg = "A73"

    def A76_query():
        global naam_snelweg
        naam_snelweg = "A76"

    def A77_query():
        global naam_snelweg
        naam_snelweg = "A77"

    def A79_query():
        global naam_snelweg
        naam_snelweg = "A79"

    def A200_query():
        global naam_snelweg
        naam_snelweg = "A200"

#--------------------------------------------------------------------------------------------------------------

def Main_scherm():   #main menu scherm
    pygame.display.set_mode((display_width,display_height)) # de afmeting van het scherm
    pygame.display.set_caption('Roadmap Netherlands') # de titel op de bovenbalk
    Instruction, Intro = False, True # het start op als het programma start
    reset()
    x, y, mov_x, mov_y = 0,0,6,6
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pop_up()

        gameDisplay.fill(map_colour)
        map(title, 50, 52)
        #de knoppen van het main scherm
        button("kaart", 50, 230, 700, 50,yellow, red, Kaart_scherm)
        button("Navigatie", 50, 330, 700, 50, yellow, red, Navigatie_scherm)
        button("Opties", 50, 430, 700, 50, yellow, red, Opties_scherm)
        button("Beoordeling", 50, 530, 700, 50, yellow, red, beoordeling_scherm)
        button("grafieken", 50, 630, 700, 50, yellow, red, Grafieken_scherm)
        button("X", 1200, 100, 70, 50, yellow, red, pop_up)
        pygame.display.flip()

def Kaart_scherm():    #kaart scherm
    Instruction, Intro = True, False # het start niet direct op als het programma opstart
    pygame.display.set_caption('Roadmap Netherlands')
    while Instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pop_up()
                     
        gameDisplay.fill(map_colour)
        map(map_image,map_x,10)

        # button vars
        x1 = 700
        nextX = 60
        y1 = 15
        nextY = 50
        # button row 1
        button("A1", x1, y1, 53, 30, yellow, red, snelweg.A1)
        button("A2", x1 + nextX, y1, 53, 30, yellow, red, snelweg.A2)
        button("A4", x1 + nextX * 2, y1, 53, 30, yellow, red, snelweg.A4)
        button("A5", x1 + nextX * 3, y1, 53, 30, yellow, red, snelweg.A5)
        button("A6", x1 + nextX * 4, y1, 53, 30, yellow, red, snelweg.A6)
        button("A7", x1 + nextX * 5, y1, 53, 30, yellow, red, snelweg.A7)
        button("A8", x1 + nextX * 6, y1, 53, 30, yellow, red, snelweg.A8)
        button("A9", x1 + nextX * 7, y1, 53, 30, yellow, red, snelweg.A9)
        button("A10", x1 + nextX * 8, y1, 53, 30, yellow, red, snelweg.A10)

        # button row 2
        button("A12", x1, y1 + nextY, 53, 30, yellow, red, snelweg.A12)
        button("A13", x1 + nextX, y1 + nextY, 53, 30, yellow, red, snelweg.A13)
        button("A15", x1 + nextX * 2, y1 + nextY, 53, 30, yellow, red, snelweg.A15)
        button("A16", x1 + nextX * 3, y1 + nextY, 53, 30, yellow, red, snelweg.A16)
        button("A17", x1 + nextX * 4, y1 + nextY, 53, 30, yellow, red, snelweg.A17)
        button("A18", x1 + nextX * 5, y1 + nextY, 53, 30, yellow, red, snelweg.A18)
        button("A20", x1 + nextX * 6, y1 + nextY, 53, 30, yellow, red, snelweg.A20)
        button("A27", x1 + nextX * 7, y1 + nextY, 53, 30, yellow, red, snelweg.A27)
        button("A28", x1 + nextX * 8, y1 + nextY, 53, 30, yellow, red, snelweg.A28)

        # button row 3
        button("A29", x1, y1 + nextY * 2, 53, 30, yellow, red, snelweg.A29)
        button("A30", x1 + nextX, y1 + nextY * 2, 53, 30, yellow, red, snelweg.A30)
        button("A31", x1 + nextX * 2, y1 + nextY * 2, 53, 30, yellow, red, snelweg.A31)
        button("A32", x1 + nextX * 3, y1 + nextY * 2, 53, 30, yellow, red, snelweg.A32)
        button("A35", x1 + nextX * 4, y1 + nextY * 2, 53, 30, yellow, red, snelweg.A35)
        button("A37", x1 + nextX * 5, y1 + nextY * 2, 53, 30, yellow, red, snelweg.A37)
        button("A44", x1 + nextX * 6, y1 + nextY * 2, 53, 30, yellow, red, snelweg.A44)
        button("A50", x1 + nextX * 7, y1 + nextY * 2, 53, 30, yellow, red, snelweg.A50)
        button("A58", x1 + nextX * 8, y1 + nextY * 2, 53, 30, yellow, red, snelweg.A58)

        # button row 4
        button("A59", x1, y1 + nextY * 3, 53, 30, yellow, red, snelweg.A59)
        button("A65", x1 + nextX, y1 + nextY * 3, 53, 30, yellow, red, snelweg.A65)
        button("A67", x1 + nextX * 2, y1 + nextY * 3, 53, 30, yellow, red, snelweg.A67)
        button("A73", x1 + nextX * 3, y1 + nextY * 3, 53, 30, yellow, red, snelweg.A73)
        button("A76", x1 + nextX * 4, y1 + nextY * 3, 53, 30, yellow, red, snelweg.A76)
        button("A77", x1 + nextX * 5, y1 + nextY * 3, 53, 30, yellow, red, snelweg.A77)
        button("A79", x1 + nextX * 6, y1 + nextY * 3, 53, 30, yellow, red, snelweg.A79)
        button("A200", x1 + nextX * 7, y1 + nextY * 3, 53, 30, yellow, red, snelweg.A200)
        button("EE_1", x1 + nextX * 8, y1 + nextY * 3, 53, 30, yellow, red, atari)

        # button back
        button("Terug", 1200, 700, 53, 30, yellow, red, Main_scherm)
        button("deselecteer", 800, 700, 70, 30, yellow, red, reset)

        if andere == True:
            map(Display_map, map_x,map_y)

        clock.tick(15)  #refresh rate van 15
        pygame.display.flip()

def beoordeling_scherm(): # het beoordeling scherm
    Instruction, Intro = True, False # het start niet direct op als het programma start
    while Instruction:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pop_up()

        gameDisplay.fill(map_colour)

        # button vars
        y1 = 15
        y2 = 50

        # button row 1
        button("A1", 43, y1, 50, 30, yellow, red, snelweg_query.A1_query)
        button("A2", 115, y1, 50, 30, yellow, red, snelweg_query.A2_query)
        button("A4", 185, y1, 50, 30, yellow, red, snelweg_query.A4_query)
        button("A5", 255, y1, 50, 30, yellow, red, snelweg_query.A5_query)
        button("A6", 325, y1, 50, 30, yellow, red, snelweg_query.A6_query)
        button("A7", 395, y1, 50, 30, yellow, red, snelweg_query.A7_query)
        button("A8", 465, y1, 50, 30, yellow, red, snelweg_query.A8_query)
        button("A9", 535, y1, 50, 30, yellow, red, snelweg_query.A9_query)
        button("A10",605, y1, 50, 30, yellow, red, snelweg_query.A10_query)
        button("A12", 675, y1, 50, 30, yellow, red, snelweg_query.A12_query)
        button("A13", 745, y1, 50, 30, yellow, red, snelweg_query.A13_query)
        button("A15", 815, y1, 50, 30, yellow, red, snelweg_query.A15_query)
        button("A16", 885, y1, 50, 30, yellow, red, snelweg_query.A16_query)
        button("A17", 955, y1, 50, 30, yellow, red, snelweg_query.A17_query)
        button("A18", 1025, y1, 50, 30, yellow, red, snelweg_query.A18_query)
        button("A20", 1090, y1, 50, 30, yellow, red, snelweg_query.A20_query)
        button("A27", 1155, y1, 50, 30, yellow, red, snelweg_query.A27_query)
        button("A28", 1220, y1, 50, 30, yellow, red, snelweg_query.A28_query)

        # button row 2
        button("A29", 43, y2, 50, 30, yellow, red, snelweg_query.A29_query)
        button("A30", 115, y2, 50, 30, yellow, red, snelweg_query.A30_query)
        button("A31", 185, y2, 50, 30, yellow, red, snelweg_query.A31_query)
        button("A32", 255, y2, 50, 30, yellow, red, snelweg_query.A32_query)
        button("A35", 325, y2, 50, 30, yellow, red, snelweg_query.A35_query)
        button("A37", 395, y2, 50, 30, yellow, red, snelweg_query.A37_query)
        button("A44", 465, y2, 50, 30, yellow, red, snelweg_query.A44_query)
        button("A50", 535, y2, 50, 30, yellow, red, snelweg_query.A50_query)
        button("A58", 605, y2, 50, 30, yellow, red, snelweg_query.A58_query)
        button("A59", 675, y2, 50, 30, yellow, red, snelweg_query.A59_query)
        button("A65", 745, y2, 50, 30, yellow, red, snelweg_query.A65_query)
        button("A67", 815, y2, 50, 30, yellow, red, snelweg_query.A67_query)
        button("A73", 885, y2, 50, 30, yellow, red, snelweg_query.A73_query)
        button("A76", 955, y2, 50, 30, yellow, red, snelweg_query.A76_query)
        button("A77", 1025, y2, 50, 30, yellow, red, snelweg_query.A77_query)
        button("A79", 1090, y2, 50, 30, yellow, red, snelweg_query.A79_query)
        button("A200",1155, y2, 50, 30, yellow, red, snelweg_query.A200_query)
        button("EE_1",1220, y2, 50, 30, yellow, red, snek)

        button("Verstuur", 150, 700, 300, 50, yellow, red, sent_data)
        button("Terug", 850, 700, 300, 50, yellow, red, Main_scherm)

        rating() # hetgeen wat er voor zorgt dat de steren zichzelf op de goede manier tonen
        if rating_files == True:
            if file_nummer == 1:
                set.rating_file_1()
            elif file_nummer == 2:
                set.rating_file_2()
            elif file_nummer == 3:
                set.rating_file_3()
            elif file_nummer == 4:
                set.rating_file_4()
            elif file_nummer == 5:
                set.rating_file_5()

        if rating_wegdek == True:
            if wegdek_nummer == 1:
                set.rating_wegdek_1()
            elif wegdek_nummer == 2:
                set.rating_wegdek_2()
            elif wegdek_nummer == 3:
                set.rating_wegdek_3()
            elif wegdek_nummer == 4:
                set.rating_wegdek_4()
            elif wegdek_nummer == 5:
                set.rating_wegdek_5()

        # hetgeen wat zorgt dat het selecteren van de tijd goed verloopt
        if tijd == 'O':
            pygame.draw.rect(gameDisplay, red, (1220, 300, 50, 30))
            message_display2('Ochtend', 1245, 315, 12)
        if tijd == 'M':
            pygame.draw.rect(gameDisplay, red, (1220, 400, 50, 30))
            message_display2('Middag', 1245, 415, 12)
        if tijd == 'A':
            pygame.draw.rect(gameDisplay, red, (1220, 500, 50, 30))
            message_display2('Avond', 1245, 515, 12)
        if tijd == 'N':
            pygame.draw.rect(gameDisplay, red, (1220, 600, 50, 30))
            message_display2('Nacht', 1245, 615, 12)

        clock.tick(15)  #refresh rate van 15
        pygame.display.flip()
        
def Navigatie_scherm():    #navigatie scherm
    Instruction, Intro = True, False # het start niet direct op als het programma opstart
    while Instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pop_up()
        gameDisplay.fill(map_colour)
        map(map_image,map_x,10)
        y1 = 15
        message_display2("Van Rotterdam naar:", 950, 40, 30)
        button("Berlijn", 700, 90, 100, 30, yellow, red,snelweg.nav_berlijn)
        button("Parijs", 810, 90, 100, 30, yellow, red, snelweg.nav_parijs)
        button("Haarlem", 920, 90, 100, 30, yellow, red, snelweg.nav_haarlem)
        button("Amsterdam", 1030, 90, 100, 30, yellow, red,snelweg.nav_amsterdam )
        button("Den Haag", 1140, 90, 100, 30, yellow, red, snelweg.nav_denhaag)

        button("Middelburg", 700, 130, 100, 30, yellow, red, snelweg.nav_middelburg)
        button("Utrecht", 810, 130, 100, 30, yellow, red, snelweg.nav_utrecht)
        button("Den Bosch", 920, 130, 100, 30, yellow, red, snelweg.nav_denbosch)
        button("Maastricht",1030, 130, 100, 30, yellow, red, snelweg.nav_maastricht)
        button("Arnhem", 1140, 130, 100, 30, yellow, red, snelweg.nav_arnhem)

        button("Zwolle", 700, 170, 100, 30, yellow, red, snelweg.nav_zwolle)
        button("Assen", 810, 170, 100, 30, yellow, red, snelweg.nav_assen)
        button("Groningen", 920, 170, 100, 30, yellow, red, snelweg.nav_groningen)
        button("Leeuwarden", 1030, 170, 100, 30, yellow, red, snelweg.nav_leeuwarden)
        button("Lelystad", 1140, 170, 100, 30, yellow, red, snelweg.nav_lelystad)

        button("Terug", 1200, 700, 53, 30, yellow, red, Main_scherm)
        button("deselecteer", 800, 700, 70, 30, yellow, red, reset)

        if andere == True:
            map(Display_map, map_x,map_y)

        clock.tick(15)  #refresh rate van 15
        pygame.display.flip()

def Opties_scherm():  #opties menu
    Instruction, Intro = True, False
    while Instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pop_up()
        gameDisplay.fill(map_colour)
        button("Sound off", 50, 130, 350, 50, yellow, red, sound_off)
        button("Sound on", 400, 130, 350, 50, yellow, red, sound_on)
        button("Volume down", 50, 230, 350, 50, yellow, red, volumedown)
        button("Volume up", 400, 230, 350, 50, yellow, red, volumeup)
        button("terug", 50, 500, 700, 50, yellow, red, Main_scherm)
        clock.tick(15)  #refresh rate van 15
        pygame.display.flip()

def Grafieken_scherm():    #grafieken scherm
    Instruction, Intro = True, False
    while Instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pop_up()
        gameDisplay.fill(map_colour)
        button("Grafiek 1", 50, 130, 650, 50,yellow, red, grafiek1) # dit roept de grafiek op over het soort voertuig
        button("Grafiek 2", 50, 230, 650, 50, yellow, red, grafiek2)# dit roept de grafiek op over de gevaarlijkste a-wegen
        button("X", 1200, 100, 70, 50, yellow, red, Main_scherm)
        map(car, 50, 400)
        clock.tick(15)  #refresh rate van 15
        pygame.display.flip()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#dit roept alle schermen op
pygame.mixer.music.play(-1)
Main_scherm()
Kaart_scherm()
Navigatie_scherm()
Opties_scherm()
Grafieken_scherm()
quit()
