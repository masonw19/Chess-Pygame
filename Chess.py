import pygame
from board import Board

pygame.init()

win = pygame.display.set_mode((640, 640))
font = pygame.font.Font('freesansbold.ttf', 12)
# write the title and load the bg image
pygame.display.set_caption("Chess") 
bg = pygame.image.load('imgs/Chess_Board.png')

test_img = pygame.image.load('imgs/Queen_White.png')

def update(i, board):
    print("hello")
    i.piece = board.clickedSquare.piece 
    i.isFull = True         # set that the square is now full
    i.clicked = False       # clicked is false
    
    board.clickedSquare.piece = None
    board.clickedSquare.clicked = False
    board.clickedSquare.isFull = False
    
    board.clickedSquare = i
    i.clicked=False

def redrawGameWindow(boardList, board):
    win.blit(bg, (0, 0))

    # we will show pieces on the board. show if the person clicks
    for i in boardList:
        if i.isFull:        # here we show the pieces
            i.show()

        i.squareClicked()  # set the clicked attribute to be true if the square gets clicked

        # if the square is clicked. highlight the most recent square
        if i.clicked:
            if i == board.clickedSquare:
                board.pot_moves = i.highlight()
            elif i.pos in board.pot_moves:
                update(i, board)
                print(i.pos)
            else:
                board.clickedSquare.clicked = False
                board.pot_moves = i.highlight()
                board.clickedSquare = i

    #print(board.pot_moves)
    pygame.display.update()


def main():
    run = True
    board = Board(win)
    boardList = board.getList()
    while run:
        redrawGameWindow(boardList, board)
        #print(pygame.mouse.get_pressed()[0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        

main()
pygame.quit()

