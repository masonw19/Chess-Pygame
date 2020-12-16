import pygame
from board import Board

pygame.init()

win = pygame.display.set_mode((640, 640))
font = pygame.font.Font('freesansbold.ttf', 12)
# write the title and load the bg image
pygame.display.set_caption("Chess") 
bg = pygame.image.load('imgs/Chess_Board.png')

test_img = pygame.image.load('imgs/Queen_White.png')


def redrawGameWindow(board):
    win.blit(bg, (0, 0))

    for i in board.list:

        i.squareClicked()  # set the clicked attribute to be true if the square gets clicked
        
        # highlight squares
        if i.clicked:
            i.highlight_clicked(board)  # highlights the clicked square
        
        i.highlight()                   # highlights all the potential moves
        i.show()                        # shows all the images

    pygame.display.update()


def main():
    run = True
    board = Board(win)
    while run:
        
        redrawGameWindow(board)
        #print(pygame.mouse.get_pressed()[0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        

main()
pygame.quit()

