import pygame
pygame.init()

canvasWidth = 500
canvasHeight = 500

win = pygame.display.set_mode((canvasWidth, canvasHeight)) #creates the surface for everything to be drawn on

pygame.display.set_caption("Tic Tac Toe")  #sets the name of the window

pygame.draw.rect(win, (255,255,255), (canvasWidth/3, 0, 2, canvasHeight)) #draws the board
pygame.draw.rect(win, (255,255,255), ((2*canvasWidth)/3, 0, 2, canvasHeight))
pygame.draw.rect(win, (255,255,255), (0, canvasHeight/3, canvasWidth, 2))
pygame.draw.rect(win, (255,255,255), (0, (2*canvasHeight/3), canvasWidth, 2))


def main():
    positions = [0,0,0,0,0,0,0,0,0] #list of all positions on the board, 0 = empty, 1 = x, and -1 = o
    symbol = 'x'
    run = True
    while run:
        pygame.time.delay(100) #refresh rate
        
        for event in pygame.event.get(): #allows us to quit when we hit the close button
            if event.type == pygame.QUIT:
                run = False
        
        mouseX, mouseY = pygame.mouse.get_pos() #gets the current x and y of the mouse
        
        if (mouseX < canvasWidth/3 and mouseX > 0) and (mouseY < canvasHeight/3 and mouseY > 0) and positions[0] == 0 and pygame.mouse.get_pressed()[0]: #check if the mouse is clicked and in the top left corner and there is nothing in the top left corner
            position = 1
            drawSymbol(position, symbol)
            if symbol == "x":
                positions[0] = 1
                symbol = 'o'
            else:
                positions[0] = -1
                symbol = 'x'
        elif (mouseX < (2*canvasWidth/3) and mouseX > canvasWidth/3) and (mouseY < canvasHeight/3 and mouseY > 0) and positions[1] == 0 and pygame.mouse.get_pressed()[0]:
            position = 2
            drawSymbol(position, symbol)
            if symbol == "x":
                positions[1] = 1
                symbol = 'o'
            else:
                positions[1] = -1
                symbol = 'x'
        elif (mouseX < (canvasWidth) and mouseX > 2*canvasWidth/3) and (mouseY < canvasHeight/3 and mouseY > 0) and positions[2] == 0 and pygame.mouse.get_pressed()[0]:
            position = 3
            drawSymbol(position, symbol)
            if symbol == "x":
                positions[2] = 1
                symbol = 'o'
            else:
                positions[2] = -1
                symbol = 'x'
        elif (mouseX < canvasWidth/3 and mouseX > 0) and (mouseY < (2*canvasHeight/3) and mouseY > canvasHeight/3) and positions[3] == 0 and pygame.mouse.get_pressed()[0]:
            position = 4
            drawSymbol(position, symbol)
            if symbol == "x":
                positions[3] = 1
                symbol = 'o'
            else:
                positions[3] = -1
                symbol = 'x'
        elif (mouseX < (2*canvasWidth/3) and mouseX > canvasWidth/3) and (mouseY < (2*canvasHeight/3) and mouseY > canvasHeight/3) and positions[4] == 0 and pygame.mouse.get_pressed()[0]:
            position = 5
            drawSymbol(position, symbol)
            if symbol == "x":
                positions[4] = 1
                symbol = 'o'
            else:
                positions[4] = -1
                symbol = 'x'
        elif (mouseX < canvasWidth and mouseX > 2*canvasWidth/3) and (mouseY < (2*canvasHeight/3) and mouseY > canvasWidth/3) and positions[5] == 0 and pygame.mouse.get_pressed()[0]:
            position = 6
            drawSymbol(position, symbol)
            if symbol == "x":
                positions[5] = 1
                symbol = 'o'
            else:
                positions[5] = -1
                symbol = 'x'
        elif (mouseX < (canvasWidth/3) and mouseX > 0) and (mouseY < canvasHeight and mouseY > 2*canvasHeight/3) and positions[6] == 0 and pygame.mouse.get_pressed()[0]:
            position = 7
            drawSymbol(position, symbol)
            if symbol == "x":
                positions[6] = 1
                symbol = 'o'
            else:
                positions[6] = -1
                symbol = 'x'
        elif (mouseX < (2*canvasWidth/3) and mouseX > canvasWidth/3) and (mouseY < canvasHeight and mouseY > 2*canvasHeight/3) and positions[7] == 0 and pygame.mouse.get_pressed()[0]:
            position = 8
            drawSymbol(position, symbol)
            if symbol == "x":
                positions[7] = 1
                symbol = 'o'
            else:
                positions[7] = -1
                symbol = 'x'
        elif (mouseX < canvasWidth and mouseX > 2*canvasWidth/3) and (mouseY < canvasHeight and mouseY > 2*canvasHeight/3) and positions[8] == 0 and pygame.mouse.get_pressed()[0]:
            position = 9
            drawSymbol(position, symbol)
            if symbol == "x":
                positions[8] = 1
                symbol = 'o'
            else:
                positions[8] = -1
                symbol = 'x'
        else:
            continue
        
        run = winner(positions)
        
        done = True
        
        for pos in positions: # loop through positions and go to the next loop if they are not all 0's
            if pos == 0:
                done = False
        
        if done:   
            print("DONE!!!")
        #endScreen() #need to implement function for determining the winner
        
        
        pygame.display.update()
        
def winner(positions):
    if (positions[0]+positions[1]+positions[2]) == 3:
        XWin()
        return False
    elif (positions[0]+positions[1]+positions[2]) == -3:
        OWin()
        return False
    if (positions[3]+positions[4]+positions[5]) == 3:
        XWin()
        return False
    elif (positions[3]+positions[4]+positions[5]) == -3:
        OWin()
        return False
    if (positions[6]+positions[7]+positions[8]) == 3:
        XWin()
        return False
    elif (positions[6]+positions[7]+positions[8]) == -3:
        OWin()
        return False
    if (positions[0]+positions[3]+positions[6]) == 3:
        XWin()
        return False
    elif (positions[0]+positions[3]+positions[6]) == -3:
        OWin()
        return False
    if (positions[1]+positions[4]+positions[7]) == 3:
        XWin()
        return False
    elif (positions[1]+positions[4]+positions[7]) == -3:
        OWin()
        return False
    if (positions[2]+positions[5]+positions[8]) == 3:
        XWin()
        return False
    elif (positions[2]+positions[5]+positions[8]) == -3:
        OWin()
        return False
    if (positions[0]+positions[4]+positions[8]) == 3:
        XWin()
        return False
    elif (positions[0]+positions[4]+positions[8]) == -3:
        OWin()
        return False
    if (positions[2]+positions[4]+positions[6]) == 3:
        XWin()
        return False
    elif (positions[2]+positions[4]+positions[6]) == -3:
        OWin()
        return False
    else:
        return True
    
def XWin():
    print ("X's won")

def OWin():
    print ("O's won")
        
def drawSymbol(position, symbol):
    switcher = {
        1: (0,0),
        2: ((canvasWidth/3), 0),
        3: ((2*canvasWidth/3), 0),
        4: (0, (canvasHeight/3)),
        5: ((canvasWidth/3),(canvasHeight/3)),
        6: ((2*canvasWidth/3),(canvasHeight/3)),
        7: (0, (2*canvasHeight/3)),
        8: ((canvasWidth/3),(2*canvasHeight/3)),
        9: ((2*canvasWidth/3),(2*canvasHeight/3)),
    }
    x,y = switcher.get(position, "error")
    if symbol == 'x':
        drawX(x,y)
    else:
        drawO(x,y)


def drawX(x,y):
    endX = (x+(canvasWidth/3))
    endY = (y+(canvasHeight/3))
    pygame.draw.line(win,(255,255,255),(x,y),(endX,endY),5)
    pygame.draw.line(win,(255,255,255),(endX,y),(x,endY),5)
    pygame.display.update()
    
    
    
def drawO(x,y):
    centerX = int(x+((canvasWidth/3)/2))
    centerY = int(y+((canvasHeight/3)/2))
    pygame.draw.circle(win,(255,255,255), (centerX,centerY), int((canvasHeight/3)/2), 5 )
    

main()
