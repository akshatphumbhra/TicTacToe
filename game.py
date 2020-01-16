import pygame
import random
import time

pygame.init()

width = 600
height = 600

screen = pygame.display.set_mode((width, height))

#Set caption
pygame.display.set_caption("Tic Tac Toe")

#Set Icon
icon = pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

availableGrid = ['','','','','','','','','']

#Deciding player 1 at random
ran=random.randint(0,1)
if ran == 0:
    currentPlayer = 'X'
else:
    currentPlayer = 'O'

running = True

gameMode = None

#Helper function to create text Objects
def textObjects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

#Helper function to create button functionality
def button(msg,x,y,w,h,ic,ac,action=None):
    global gameMode

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            #print(action)
            gameMode = action
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = textObjects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

#Helper function that returns grid number based on mouse position
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

#Helper function to draw X on the desired grid
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
    pygame.draw.line(screen, (0,0,0), (x2,y1), (x1,y2), 3)

#Helper function to draw O on the desired grid
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

#Helper function that checks if the game is over, if it is, what is the result
def checkWinner(grid):

    tie = True
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

    for grid in availableGrid:
        if grid == '':
            tie = False

    if tie:
        return False, 'tie', ''
    return False, '', ''

#Helper function to quit game
def quitGame():
    pygame.quit()
    quit()

#Helper funciton that uses the minimax algorithm to decide best move
def bestMove():

    global availableGrid
    bestScore = -100
    move = -1

    for i in range(len(availableGrid)):
        if availableGrid[i] == '':
            availableGrid[i] = 'O'
            score = minimax(availableGrid, False);
            availableGrid[i] = ""
            if score > bestScore:
                bestScore = score
                move = i

    #print(move)
    availableGrid[move] = 'O'
    drawO(move)

#Implements minimax algorithm to find the best move for AI
def minimax(grid, isMaximizing):
    hasWon, winner, strikeThrough = checkWinner(grid)

    if hasWon:
        if winner == "X":
            return -1
        elif winner == 'O':
            return 1

    elif winner == 'tie':
        return 0

    if isMaximizing:
        bestScore = -100
        for i in range(len(grid)):
            if grid[i] == "":
                grid[i] = 'O'
                score = minimax(grid, False)
                #print("Score Max", score)
                grid[i] = ""
                #print(score, bestScore)
                if score >= bestScore:
                    bestScore = score
        return bestScore

    else:
        bestScore = 100
        for i in range(len(grid)):
            if grid[i] == '':
                grid[i] = 'X'
                score = minimax(grid, True)
                #print("Score Min", score)
                grid[i] = ''
                if score <= bestScore:
                    bestScore = score
        return bestScore

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

#Runs game introduction.
def gameIntro():

    intro = True
    image = pygame.image.load("bg.png")
    imgRect = image.get_rect()
    imgRect.left, imgRect.top = 44,44

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        screen.fill((228,233,244))
        screen.blit(image, imgRect)
        largeText = pygame.font.SysFont("comicsansms",100)
        TextSurf, TextRect = textObjects("Tic-Tac-Toe", largeText)
        TextRect.center = ((width/2),100)
        screen.blit(TextSurf, TextRect)

        button("Solo",(width/2 - 50),250,100,50,(0, 255, 0),(0, 200, 0),solo)
        button("Duo",(width/2 - 50),350,100,50,(0, 255, 0),(0, 200, 0),duo)
        button("Quit", (width/2 - 50), 450, 100, 50, (255,0,0), (200,0,0), quitGame)

        pygame.display.update()
        clock.tick(30)

#Runs game against AI
def solo():
    time.sleep(0.3)
    global screen, availableGrid, currentPlayer, running
    tie = False
    initializeGame()

    firstMove = True

    while running:
        #print(currentPlayer)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        if currentPlayer == 'X':

            click = pygame.mouse.get_pressed()
            if click[0] == 1:

                mx, my = pygame.mouse.get_pos()
                grid = getGrid(mx, my)
                if availableGrid[grid] == "":
                    drawX(grid)
                    availableGrid[grid] = 'X'
                    currentPlayer = 'O'
                    firstMove = False



        else:
            bestMove()
            currentPlayer = 'X'

        hasWon, winner, strikeThrough = checkWinner(availableGrid)
        if hasWon:
            pygame.draw.line(screen, (255,0,0), strikeThrough[0], strikeThrough[1], 3)
            endScreen(winner)

        elif winner == 'tie':
            endScreen("tie")

        pygame.display.update()
        clock.tick(30)

#Runs game for two players
def duo():
    global screen, availableGrid, currentPlayer, running
    initializeGame()
    currentPlayer = 'X'
    #Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print(event)
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
            endScreen(winner)

        elif winner == 'tie':
            endScreen("tie")

        pygame.display.update()
        clock.tick(30)

#Runs end screen options
def endScreen(result):
    time.sleep(0.1)
    largeText = pygame.font.SysFont("comicsansms",100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        if result == "tie":

            TextSurf, TextRect = textObjects("Draw Game!", largeText)
            TextRect.center = ((width/2),100)
            screen.blit(TextSurf, TextRect)

        else:
            msg = result + " Won!"
            TextSurf, TextRect = textObjects(msg, largeText)
            TextRect.center = ((width/2),100)
            screen.blit(TextSurf, TextRect)


        button("Retry", (width/2 - 50),200,100,50,(0, 255, 0),(0, 200, 0), gameMode)
        button("Menu",(width/2 - 50),300,100,50,(0, 255, 0),(0, 200, 0), gameIntro)
        button("Quit", (width/2 - 50), 400, 100, 50, (255,0,0), (200,0,0), quitGame)

        pygame.display.update()
        clock.tick(30)

gameIntro()
