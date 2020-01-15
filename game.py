import pygame
import random

#Initialize game settings
def initializeGame():

    global screen, availableGrid, currentPlayer, running

    #Set background color
    screen.fill((255,255,255))
    pygame.draw.line(screen, (0,0,0), (0,height/3), (width,height/3))
    pygame.draw.line(screen, (0,0,0), (0,2*height/3), (width,2*height/3))
    pygame.draw.line(screen, (0,0,0), (width/3,0), (width/3,height))
    pygame.draw.line(screen, (0,0,0), (2*width/3,0), (2*width/3,height))

    for i in range(len(availableGrid)):
        availableGrid[i] = ""

    ran=random.randint(0,1)
    if ran == 0:
        currentPlayer = 'X'
    else:
        currentPlayer = 'O'

    running = True

    pygame.display.update()


def getGrid(mx, my):
    if mx <= width/3:
        if my <=height/3:
            return 0
        elif my <=2*height/3:
            return 1
        else:
            return 2
    elif mx <=2*width/3:
        if my <=height/3:
            return 3
        elif my <=2*height/3:
            return 4
        else:
            return 5
    else:
        if my <=height/3:
            return 6
        elif my <=2*height/3:
            return 7
        else:
            return 8

def drawX(grid):
    global screen

    x1 = int(width/30)
    x2 = int(width/3 - x1)
    y1 = int(height/30)
    y2 = int(height/3 - y1)

    xsize = int(width/3)
    ysize = int(height/3)

    if grid == 0:
        pass
    elif grid == 1:
        y1+=ysize
        y2+=ysize
    elif grid == 2:
        y1+=2*ysize
        y2+=2*ysize
    elif grid == 3:
        x1+=xsize
        x2+=xsize
    elif grid == 4:
        x1+=xsize
        x2+=xsize
        y1+=ysize
        y2+=ysize
    elif grid == 5:
        x1+=xsize
        x2+=xsize
        y1+=2*ysize
        y2+=2*ysize
    elif grid == 6:
        x1+=2*xsize
        x2+=2*xsize
    elif grid == 7:
        x1+=2*xsize
        x2+=2*xsize
        y1+=ysize
        y2+=ysize
    elif grid == 8:
        x1+=2*xsize
        x2+=2*xsize
        y1+=2*ysize
        y2+=2*ysize


    pygame.draw.line(screen, (0,0,0), (x1,y1), (x2,y2), 3)
    #pygame.draw.line(screen, (0,0,0), (x1,y1+1), (x2,y2+1))
    #pygame.draw.line(screen, (0,0,0), (x1+1,y1), (x2+1,y2))

    pygame.draw.line(screen, (0,0,0), (x2,y1), (x1,y2), 3)
    #pygame.draw.line(screen, (0,0,0), (x2+1,y1), (x1+1,y2))
    #pygame.draw.line(screen, (0,0,0), (x2-1,y1), (x1-1,y2))

def drawO(grid):
    global screen

    x = int(width/6)
    y = int(height/6)

    xsize = int(width/3)
    ysize = int(height/3)

    radius = int(x - (xsize/10))

    if grid == 0:
        pass
    elif grid == 1:
        y +=ysize
    elif grid == 2:
        y+=2*ysize
    elif grid == 3:
        x+=xsize
    elif grid == 4:
        x+=xsize
        y+=ysize
    elif grid == 5:
        x+=xsize
        y+=2*ysize
    elif grid == 6:
        x+=2*xsize
    elif grid == 7:
        x+=2*xsize
        y+=ysize
    elif grid == 8 :
        x+=2*xsize
        y+=2*ysize

    pygame.draw.circle(screen, (0,0,0), (x,y), 80, 3)

def checkWinner(grid):

    x = width/6
    y = height/6
    xs = width/3
    ys = height/3

    #Verical Lines
    if grid[0] == grid[1] and grid[1] == grid[2] and grid[0] != '':
        return True, grid[0], [(x, 0), (x, height)]
    if grid[3] == grid[4] and grid[4] == grid[5] and grid[3] != '':
        return True, grid[3], [(x+xs, 0), (x+xs, height)]
    if grid[6] == grid[7] and grid[7] == grid[8] and grid[6] != '':
        return True, grid[6], [(x+2*xs, 0), (x+2*xs, height)]

    #Horizontal Lines
    if grid[0] == grid[3] and grid[3] == grid[6] and grid[0] != '':
        return True, grid[0], [(0, y), (width, y)]
    if grid[1] == grid[4] and grid[4] == grid[7] and grid[1] != '':
        return True, grid[1], [(0, y+ys), (width, y+ys)]
    if grid[2] == grid[5] and grid[5] == grid[8] and grid[2] != '':
        return True, grid[2], [(0, y+2*ys), (width, y+2*ys)]

    #Diagonals
    if grid[0] == grid[4] and grid[4] == grid[8] and grid[0] != '':
        return True, grid[4], [(0, 0), (width, height)]
    if grid[6] == grid[4] and grid[4] == grid[2] and grid[6] != '':
        return True, grid[4], [(width, 0), (0, height)]

    return False, '', ''

def main():
    global screen, availableGrid, currentPlayer, running

    initializeGame()

    #Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                grid = getGrid(mx, my)
                if availableGrid[grid] == '':
                    if currentPlayer == 'X':
                        drawX(grid)
                        availableGrid[grid] = 'X'
                        currentPlayer = 'O'
                    else:
                        drawO(grid)
                        availableGrid[grid] = 'O'
                        currentPlayer = 'X'

                    hasWon, winner, strikeThrough = checkWinner(availableGrid)
                    if hasWon:
                        pygame.draw.line(screen, (255,0,0), strikeThrough[0], strikeThrough[1], 3)
            pygame.display.update()

pygame.init()

width = 600
height = 600

screen = pygame.display.set_mode((width, height))

#Set caption
pygame.display.set_caption("Tic Tac Toe")

#Set Icon
icon = pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(icon)

availableGrid = ['','','','','','','','','']

#Deciding player 1 at random
ran=random.randint(0,1)
if ran == 0:
    currentPlayer = 'X'
else:
    currentPlayer = 'O'

running = True

main()
