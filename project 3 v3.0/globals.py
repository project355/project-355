import pygame, time, psycopg2, math
import eztext

display_width = 1300
display_height = 800
x = (display_width * 0.45)
y = (display_height * 0.8)

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))  # init resolution
pygame.mixer.music.load("poi.wav")                                      # music file
pygame.display.set_caption('roadmap netherlands')                       # titel of pygame frame
clock = pygame.time.Clock()                                             # nodig voor Refresh Rate
_image_library = {}                                                     # global list

# image 637x750
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