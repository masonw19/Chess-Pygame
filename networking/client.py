import pygame
from board import Board
from network import Network
import pickle

pygame.init()

win = pygame.display.set_mode((640, 640))
font = pygame.font.Font('freesansbold.ttf', 12)
# write the title and load the bg image
pygame.display.set_caption("Chess") 
bg = pygame.image.load('imgs/Chess_Board.png')
icon = pygame.image.load('imgs/Queen_White.png')
pygame.display.set_icon(icon)

surface = pygame.Surface((70,70))
surface.set_alpha(128)
surface.fill ((255,0,0))

img_dict = {"Rook_White":pygame.image.load("imgs/Rook_White.png"), "Knight_White":pygame.image.load("imgs/Knight_White.png"), 
            "Bishop_White":pygame.image.load("imgs/Bishop_White.png"), "Queen_White":pygame.image.load("imgs/Queen_White.png"),
            "King_White":pygame.image.load("imgs/King_White.png"), "Pawn_White":pygame.image.load("imgs/Pawn_White.png"),
            "Rook_Black":pygame.image.load("imgs/Rook_Black.png"), "Knight_Black":pygame.image.load("imgs/Knight_Black.png"), 
            "Bishop_Black":pygame.image.load("imgs/Bishop_Black.png"), "Queen_Black":pygame.image.load("imgs/Queen_Black.png"),
            "King_Black":pygame.image.load("imgs/King_Black.png"), "Pawn_Black":pygame.image.load("imgs/Pawn_Black.png"),
            None:None}

def highlight(highlightme, clicked, pos, win):
    if highlightme:
        win.blit(surface, (pos[0]+5,pos[1]+5))
    if clicked:
        win.blit(surface, (pos[0]+5,pos[1]+5))

def show_pieces(valid ,img, pos, win):
    if valid:
            win.blit(img_dict[img], pos)

def redrawGameWindow(board, n, coords, win, surface):
    win.blit(bg, (0, 0))

    for i in board.list:
        
        if coords != None:
            i.squareClicked(coords, board)  # set the clicked attribute to be true if the square gets clicked
        
            # highlight squares
            if i.clicked:
                i.update_squares(board, n)  # highlights the clicked square

        # highlight the squares
        highlightme, clicked, pos = i.get_highlight()            # highlights all the potential moves
        highlight(highlightme, clicked, pos, win)
    
        # show the pieces
        valid,img, pos = i.show()                        # shows all the images
        show_pieces(valid, img, pos, win)

    if board.my_turn == False:
        win.blit(bg, (0, 0))
        for i in board.list:
            # highlight the squares
            highlightme, clicked, pos = i.get_highlight()            # highlights all the potential moves
            highlight(highlightme, clicked, pos, win)
        
            # show the pieces
            valid, img, pos = i.show()                        # shows all the images
            show_pieces(valid, img, pos, win)  

    pygame.display.update()

def main():
    run = True
    n = Network()
    board1 = n.getBoard()
    #clock = pygame.time.Clock()
    coords = None
    redrawGameWindow(board1, n, coords, win, surface) # we might want to send board2.win
    while run:
        #clock.tick(30)
        
        #board1 = n.send(board1) # when we send data through the network we will receive the other boards information
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords = pygame.mouse.get_pos()
                print(board1.turn)
            else:
                coords = None

        if board1.my_turn:
            redrawGameWindow(board1, n, coords, win, surface) # we might want to send board2.win
            data = pickle.dumps(board1)   # object we want to send to other client
            print(len(data))     # length of data
        else:
            board1 = n.send(board1)

        coords = None
        #print(board1.my_turn)
main()
pygame.quit()

