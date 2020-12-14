import pygame
from board import Board

pygame.init()

win = pygame.display.set_mode((640, 640))
font = pygame.font.Font('freesansbold.ttf', 12)
# write the title and load the bg image
pygame.display.set_caption("Chess") 
bg = pygame.image.load('imgs/Chess_Board.png')

test_img = pygame.image.load('imgs/Queen_White.png')

def redrawGameWindow(boardList):
    win.blit(bg, (0, 0))

    # we will show all the pieces that are on the board
    for i in boardList:
        if i.isFull:
            i.show(win)

    pygame.display.update()

def main():
    run = True
    board = Board(win)
    boardList = board.getList()
    while run:
        redrawGameWindow(boardList)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        

main()
pygame.quit()

