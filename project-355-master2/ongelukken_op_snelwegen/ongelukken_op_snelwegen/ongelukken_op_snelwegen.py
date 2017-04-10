from globals import *
from button import *

crash = False

def map(x,y):
    screen.blit(map_image, (x,y))

# quit the whole program
while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            quit()

    screen.fill(map_color) # background

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
    pygame.display.update()
