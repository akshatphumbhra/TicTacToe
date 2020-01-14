import pygame

#Initialize game settings
def initializeGame():

    pygame.init()

    screen = pygame.display.set_mode((600, 600))

    #Set caption
    pygame.display.set_caption("Tic Tac Toe")

    #Set Icon
    #icon = pygame.image.load('image url')
    #pygame.display.set_icon(icon)

    #Set background color
    screen.fill((255,255,255))
    pygame.draw.line(screen, (0,0,0), (0,200), (600,200))
    pygame.draw.line(screen, (0,0,0), (0,400), (600,400))
    pygame.draw.line(screen, (0,0,0), (200,0), (200,600))
    pygame.draw.line(screen, (0,0,0), (400,0), (400,600))

    availableGrid = ['','','','','','','','','','']
    currentPlayer = 'X'
    running = True

    pygame.display.update()

    return screen, availableGrid, currentPlayer, running

def getGrid(mx, my):
    if mx <= 200:
        if my <=200:
            return 1
        elif my <=400:
            return 2
        else:
            return 3
    elif mx <=400:
        if my <=200:
            return 4
        elif my <=400:
            return 5
        else:
            return 6
    else:
        if my <=200:
            return 7
        elif my <=400:
            return 8
        else:
            return 9

def drawX(grid, screen):
    x1 = 20
    x2 = 180
    y1 = 20
    y2 = 180
    if grid == 1:
        pass
    elif grid == 2:
        y1+=200
        y2+=200
    elif grid == 3:
        y1+=400
        y2+=400
    elif grid == 4:
        x1+=200
        x2+=200
    elif grid == 5:
        x1+=200
        x2+=200
        y1+=200
        y2+=200
    elif grid ==6:
        x1+=200
        x2+=200
        y1+=400
        y2+=400
    elif grid == 7:
        x1+=400
        x2+=400
    elif grid == 8:
        x1+=400
        x2+=400
        y1+=200
        y2+=200
    elif grid == 9:
        x1+=400
        x2+=400
        y1+=400
        y2+=400

    pygame.draw.line(screen, (0,0,0), (x1,y1), (x2,y2))
    pygame.draw.line(screen, (0,0,0), (x1,y1+1), (x2,y2+1))
    pygame.draw.line(screen, (0,0,0), (x1+1,y1), (x2+1,y2))

    pygame.draw.line(screen, (0,0,0), (x2,y1), (x1,y2))
    pygame.draw.line(screen, (0,0,0), (x2+1,y1), (x1+1,y2))
    pygame.draw.line(screen, (0,0,0), (x2-1,y1), (x1-1,y2))

def drawO(grid, screen):
    x = 100
    y = 100

    if grid == 1:
        pass
    elif grid == 2:
        y +=200
    elif grid == 3:
        y+=400
    elif grid == 4:
        x+=200
    elif grid == 5:
        x+=200
        y+=200
    elif grid == 6:
        x+=200
        y+=400
    elif grid == 7:
        x+=400
    elif grid == 8:
        x+=400
        y+=200
    elif grid ==9 :
        x+=400
        y+=400

    pygame.draw.circle(screen, (0,0,0), (x,y), 80, 3)

def checkWinner(grid):

    #Verical Lines
    if grid[1] == grid[2] and grid[2] == grid[3] and grid[1] != '':
        return True, grid[1], [(100, 0), (100, 600)]
    if grid[4] == grid[5] and grid[5] == grid[6] and grid[4] != '':
        return True, grid[4], [(300, 0), (300, 600)]
    if grid[7] == grid[8] and grid[8] == grid[9] and grid[7] != '':
        return True, grid[7], [(500, 0), (500, 600)]

    #Horizontal Lines
    if grid[1] == grid[4] and grid[4] == grid[7] and grid[1] != '':
        return True, grid[7], [(0, 100), (600, 100)]
    if grid[2] == grid[5] and grid[5] == grid[8] and grid[2] != '':
        return True, grid[2], [(0, 300), (600, 300)]
    if grid[3] == grid[6] and grid[6] == grid[9] and grid[3] != '':
        return True, grid[3], [(0, 500), (600, 500)]

    #Diagonals
    if grid[1] == grid[5] and grid[5] == grid[9] and grid[1] != '':
        return True, grid[5], [(0, 0), (600, 600)]
    if grid[7] == grid[5] and grid[5] == grid[3] and grid[7] != '':
        return True, grid[5], [(600, 0), (0, 600)]

    return False, '', ''

def main():
    screen, availableGrid, currentPlayer, running = initializeGame()

    #Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                grid = getGrid(mx, my)
                if availableGrid[grid] == '':
                    if currentPlayer == 'X':
                        drawX(grid, screen)
                        availableGrid[grid] = 'X'
                        currentPlayer = 'O'
                    else:
                        drawO(grid, screen)
                        availableGrid[grid] = 'O'
                        currentPlayer = 'X'

                    hasWon, winner, strikeThrough = checkWinner(availableGrid)
                    if hasWon:
                        pygame.draw.line(screen, (255,0,0), strikeThrough[0], strikeThrough[1], 3)
            pygame.display.update()



main()
