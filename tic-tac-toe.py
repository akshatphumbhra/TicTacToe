import pygame
pygame.init()

canvasWidth = 500
canvasHeight = 500

win = pygame.display.set_mode((canvasWidth, canvasHeight))

pygame.display.set_caption("Tic Tac Toe")

pygame.draw.rect(win, (255,255,255), (canvasWidth/3, 0, 2, canvasHeight))
pygame.draw.rect(win, (255,255,255), ((2*canvasWidth)/3, 0, 2, canvasHeight))
pygame.draw.rect(win, (255,255,255), (0, canvasHeight/3, canvasWidth, 2))
pygame.draw.rect(win, (255,255,255), (0, (2*canvasHeight/3), canvasWidth, 2))
    
TOPLEFT = True
TOPRIGHT = True
TOPMIDDLE = True
MIDDLELEFT = True
MIDDLERIGHT = True
MIDDLEMIDDLE = True
BOTTOMLEFT = True
BOTTOMRIGHT = True
BOTTOMMIDDLE = True


def main():
    symbol = 'x'
    run = True
    while run:
        pygame.time.delay(100)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        mouseX, mouseY = pygame.mouse.get_pos()
        
        if (mouseX < canvasWidth/3) and (mouseY < canvasHeight/3) and TOPLEFT:
            TOPLEFT = ""
            drawSymbol(TL, symbol)
            
        
        
        pygame.display.update()
        
def drawSymbol(position, symbol):
    print(position)
    
main()
