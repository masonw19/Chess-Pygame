import pygame
from board import Board

pygame.init()

win = pygame.display.set_mode((640, 640))
font = pygame.font.Font('freesansbold.ttf', 12)
# write the title and load the bg image
pygame.display.set_caption("Chess") 
bg = pygame.image.load('imgs/Chess_Board.png')

test_img = pygame.image.load('imgs/Queen_White.png')

def redrawGameWindow(board, coords):
    win.blit(bg, (0, 0))

    for i in board.list:
        
        if coords != None:
            i.squareClicked(coords, board)  # set the clicked attribute to be true if the square gets clicked
        
            # highlight squares
            if i.clicked:
                i.update_squares(board)  # highlights the clicked square
                
        i.highlight()                   # highlights all the potential moves
        i.show()                        # shows all the images
    
    pygame.display.update()

def main():
    run = True
    board = Board(win)
    clock = pygame.time.Clock()
    coords = None
    while run:
        # clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords = pygame.mouse.get_pos()
                print(board.turn)
            else:
                coords = None

        redrawGameWindow(board, coords)
        coords = None

main()
pygame.quit()

