# random stuff

import pygame, sys
import random
import time
import csv

from pygame.locals import *

fpsClock = pygame.time.Clock()

# create the black and white colours

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# put them into a dictionary so they can be used to create the rows of the board

colors = {
    "BLACKTILE": BLACK,
    "WHITETILE": WHITE,
}


# 3 lists we will write in in a minute

tilemap = []
whiterow = []
blackrow = []


# write a white tile row first and write it to the whiterow list

for individual_row in range(4):
    whiterow.append("WHITETILE")
    whiterow.append("BLACKTILE")

# then write a black tile first row and write it to blackrow list

for individual_row in range(4):
    blackrow.append("BLACKTILE")
    blackrow.append("WHITETILE")

# create the board, and write it into tilemap list

for the_eight_rows in range(8):
    tilemap.append(whiterow)
    tilemap.append(blackrow)

# set the tilesize, width and height
# note: these are not mutable as we have carefully created a set number of rows, so you can't just change these

TILESIZE = 100
MAPWIDTH = 8
MAPHEIGHT = 8



# create a piece class

#Piece class
class Piece:
    pass

# create the pawn class

#Pawn class
class Pawn(Piece):
    def load_image(self):
        return pygame.image.load('whitepawn.png').convert_alpha()
    def givePositionX(self): 
        pawnPositionX = [0,1,2,3,4,5,6,7]
        return pawnPositionX
    def givePositionY(self):
        pawnPositionY = [0,1,2,3,4,5,6,7]
        return pawnPositionY
    def move_one(self):
        pass
    def move_two(self):
        pass
        # 
        # 
        # 
        # 
        # 
        # 
        # 
        # elif selectorPosition[0] == WHITEPAWN1.givePositionX()[0] and selectorPosition[1] == WHITEPAWN1.givePositionY()[6]:
        #     if (event.key == K_SPACE):
        #         print ("we can go here")
    def print_hi(self):
        print ("hi")

# set up display - you need this to display anything
pygame.init()

# give the game window a title
pygame.display.set_caption("Chess")


# display the map
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))


#display selector
SELECTOR = pygame.image.load('selector.png').convert_alpha()
# the starting position of the selectors [x, y]
# the first number refers to the x axis, or horizontal position. the second number refers to the y axis, or vertical position
selectorPosition = [3,3]










 # 
        # 
        # 
        # 
        #  # 
        # 
        # 
        # 
        #  # 
        # 
        # 
        # 
        #  # 
        # 
        # 
        # 
        #  # 
        # 
        # 
        # 
        #  # 
        # 
        # 
        # 
        # 

# 
# TEST OUT PAWN LIST IDEA OF POPULATE LIST TO SEE WHY ITS NOT WORKING!!!!




pawnlist = ['WHITEPAWN1', 'WHITEPAWN2'] 

WHITEPAWN = 'WHITEPAWN'

# THIS IS ALL MY TRYING TO WORK OUT HOW THE CODE WORKS...abs

# dicttest = {
#     'z': moooz
# }


# listy = []

# for y in range(8):
#     listy.append(dicttest['z'])

# print ("printing listy")
# print (listy)


# pawns = {
#     "WHITEPAWN": WHITEPAWN,
# }

# for i in range(8):
#     pawnlist.append(pawns['WHITEPAWN'] + str(i))

# for i in range(8):
#     pawnlist.append('WHITEPAWN' + str(i))

# pawnlist2 = []

# for i in range(8):
#     pawnlist2.append(pawns['WHITEPAWN'])

# print ("this is pawnlist2")
# print (pawnlist2)

# print("this is pawnlist ")
# print(pawnlist)


# for pawn in range(8):
#     print (pawnlist[pawn])
#     pawnlist[pawn] = Pawn()



WHITEPAWN0 = Pawn()
WHITEPAWN1 = Pawn()
WHITEPAWN2 = Pawn()
WHITEPAWN3 = Pawn()
WHITEPAWN4 = Pawn()
WHITEPAWN5 = Pawn()
WHITEPAWN6 = Pawn()
WHITEPAWN7 = Pawn()




def draw_the_board():
# draw the board
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            pygame.draw.rect(DISPLAYSURF, colors[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

L = []
while True:
# listen to events
    for event in pygame.event.get():
        # if red box to close window is pressed, this will quit the programme
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # this is how you move around
        elif event.type == KEYDOWN:
            if (event.key == K_RIGHT) and selectorPosition[0] <= 6:
                selectorPosition[0] += 1
                print (selectorPosition[0])
                draw_the_board()
            elif (event.key == K_LEFT) and selectorPosition[0] >= 1:
                selectorPosition[0] -= 1
                print (selectorPosition[0])
                draw_the_board()
            elif (event.key == K_UP) and selectorPosition[1] >= 1 :
                selectorPosition[1] -= 1
                print (selectorPosition[1])
                draw_the_board()
            elif (event.key ==K_DOWN ) and selectorPosition[1] <=6:
                selectorPosition[1] += 1
                print (selectorPosition[1])
                draw_the_board()
#  this is the starting of selecting a pawn
            elif selectorPosition[0] == WHITEPAWN1.givePositionX()[0] and selectorPosition[1] == WHITEPAWN1.givePositionY()[6]:
                if (event.key == K_SPACE):
                    print ("Space bar pressed")
                    DISPLAYSURF.blit(WHITEPAWN1.load_image(), ((WHITEPAWN1.givePositionX()[0])*TILESIZE, WHITEPAWN1.givePositionY()[4]*TILESIZE))

    # for row in range(MAPHEIGHT):
    #     for column in range(MAPWIDTH):
    #         pygame.draw.rect(DISPLAYSURF, colors[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))



# this displays the selector
        DISPLAYSURF.blit(SELECTOR, (selectorPosition[0]*TILESIZE, selectorPosition[1]*TILESIZE))


# this displays the pawns
        DISPLAYSURF.blit(WHITEPAWN0.load_image(), (WHITEPAWN0.givePositionX()[7]*TILESIZE, WHITEPAWN0.givePositionY()[6]*TILESIZE))
        DISPLAYSURF.blit(WHITEPAWN1.load_image(), (WHITEPAWN1.givePositionX()[0]*TILESIZE, WHITEPAWN1.givePositionY()[6]*TILESIZE))
        DISPLAYSURF.blit(WHITEPAWN2.load_image(), (WHITEPAWN2.givePositionX()[1]*TILESIZE, WHITEPAWN2.givePositionY()[6]*TILESIZE))
        DISPLAYSURF.blit(WHITEPAWN3.load_image(), (WHITEPAWN3.givePositionX()[2]*TILESIZE, WHITEPAWN3.givePositionY()[6]*TILESIZE))
        DISPLAYSURF.blit(WHITEPAWN4.load_image(), (WHITEPAWN4.givePositionX()[3]*TILESIZE, WHITEPAWN4.givePositionY()[6]*TILESIZE))
        DISPLAYSURF.blit(WHITEPAWN5.load_image(), (WHITEPAWN5.givePositionX()[4]*TILESIZE, WHITEPAWN5.givePositionY()[6]*TILESIZE))
        DISPLAYSURF.blit(WHITEPAWN6.load_image(), (WHITEPAWN6.givePositionX()[5]*TILESIZE, WHITEPAWN6.givePositionY()[6]*TILESIZE))
        DISPLAYSURF.blit(WHITEPAWN7.load_image(), (WHITEPAWN7.givePositionX()[6]*TILESIZE, WHITEPAWN7.givePositionY()[6]*TILESIZE))







    pygame.display.update()
    fpsClock.tick(240)