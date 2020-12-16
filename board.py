import pygame
from pygame.locals import Rect
from pieces import Rook, Knight, Bishop, Queen, King, Pawn

WHITE = 0
BLACK = 1

class Square:

    def __init__(self, pos, piece, win, isIt):
        self.pos = pos
        self.piece = piece
        self.isFull = isIt
        self.clicked = False
        self.highlightme = False
        self.win = win

        self.square = Rect(self.pos[0], self.pos[1], 80, 80)
        self.surface = pygame.Surface((70,70))
        self.surface.set_alpha(128)
        self.surface.fill ((255,0,0))

    def show(self):
        if self.piece:
            self.win.blit(self.piece.img, self.pos)

    # turn on the highlightme of all potential spots and return a list of the potiential spots
    def show_moves(self, boardDict):
        if self.isFull:
            return self.piece.moves(self.pos, self.win, boardDict)
        return []

    # highlight the square   
    def highlight(self):
        if self.highlightme:
            self.win.blit(self.surface, (self.pos[0]+5,self.pos[1]+5))

    # highlight potential move squares
    def highlight_pot_moves(self, board):
        for move in board.pot_moves:
            if board.dict[move].highlightme and not self.isFull:
                self.win.blit(self.surface, (board.dict[move].pos[0]+5, board.dict[move].pos[1]+5))

    # when we click a square we need to highlight the clicked square and then get info on potential moves
    def highlight_clicked(self, board):
        self.win.blit(self.surface, (self.pos[0]+5,self.pos[1]+5))
        
        # if the square we clicked is the same as the previous, just keep the square highglighted
        if self.pos == board.clickedSquare.pos:
            board.pot_moves = self.show_moves(board.dict)

        # if the square we clicked is a potential move square, we need to update our clicked square and move our piece
        elif self.pos in board.pot_moves:
            self.update_board(board)
            print(self.pos)

            self.release_highlight(board)   # release all old highlights

        # else do ....
        else:
            board.clickedSquare.clicked = False
            board.clickedSquare.highlightme = False

            self.release_highlight(board)

            board.pot_moves = self.show_moves(board.dict)
            board.clickedSquare = self
            board.clickedSquare.clicked = True
            board.clickedSquare.highlightme = True

    # update the clicked square and move piece
    def update_board(self, board):
        self.piece = board.clickedSquare.piece 
        self.isFull = True         # set that the square is now full
        self.clicked = False       # clicked is false
        
        board.clickedSquare.piece = None
        board.clickedSquare.clicked = False
        board.clickedSquare.isFull = False
        board.clickedSquare.highlightme = False
        
        board.clickedSquare = self

    def release_highlight(self, board):
        for move in board.pot_moves:
            if move in board.dict:
                board.dict[move].highlightme = False

    def squareClicked(self):
        if self.square.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
                self.highlightme = True

class Board:

    def __init__(self, win):
        self.A1 = Square((0,560), Rook(WHITE), win, True)
        self.B1 = Square((80,560), Knight(WHITE), win, True)
        self.C1 = Square((160,560), Bishop(WHITE), win, True)
        self.D1 = Square((240,560), Queen(WHITE), win, True) 
        self.E1 = Square((320,560), King(WHITE), win, True)
        self.F1 = Square((400,560), Bishop(WHITE), win, True)
        self.G1 = Square((480,560), Knight(WHITE), win, True)
        self.H1 = Square((560,560), Rook(WHITE), win, True)
        self.A2 = Square((0,480), Pawn(WHITE), win, True)
        self.B2 = Square((80,480), Pawn(WHITE), win, True)
        self.C2 = Square((160,480), Pawn(WHITE), win, True)
        self.D2 = Square((240,480), Pawn(WHITE), win, True)
        self.E2 = Square((320,480), Pawn(WHITE), win, True)
        self.F2 = Square((400,480), Pawn(WHITE), win, True)
        self.G2 = Square((480,480), Pawn(WHITE), win, True)
        self.H2 = Square((560,480), Pawn(WHITE), win, True)

        self.A8 = Square((0,0), Rook(BLACK), win, True)
        self.B8 = Square((80,0), Knight(BLACK), win, True)
        self.C8 = Square((160,0), Bishop(BLACK), win, True)
        self.D8 = Square((240,0), Queen(BLACK), win, True)
        self.E8 = Square((320,0), King(BLACK), win, True)
        self.F8 = Square((400,0), Bishop(BLACK), win, True)
        self.G8 = Square((480,0), Knight(BLACK), win, True)
        self.H8 = Square((560,0), Rook(BLACK), win, True)
        self.A7 = Square((0,80), Pawn(BLACK), win, True)
        self.B7 = Square((80,80), Pawn(BLACK), win, True)
        self.C7 = Square((160,80), Pawn(BLACK), win, True)
        self.D7 = Square((240,80), Pawn(BLACK), win, True)
        self.E7 = Square((320,80), Pawn(BLACK), win, True)
        self.F7 = Square((400,80), Pawn(BLACK), win, True)
        self.G7 = Square((480,80), Pawn(BLACK), win, True)
        self.H7 = Square((560,80), Pawn(BLACK), win, True)

        self.A3 = Square((0,400), None, win, False)
        self.B3 = Square((80, 400), None, win, False)
        self.C3 = Square((160, 400), None, win, False)
        self.D3 = Square((240, 400), None, win, False)
        self.E3 = Square((320, 400), None, win, False)
        self.F3 = Square((400, 400), None, win, False)
        self.G3 = Square((480, 400), None, win, False)
        self.H3 = Square((560, 400), None, win, False)

        self.A4 = Square((0,320), None, win, False)
        self.B4 = Square((80, 320), None, win, False)
        self.C4 = Square((160, 320), None, win, False)
        self.D4 = Square((240, 320), None, win, False)
        self.E4 = Square((320, 320), None, win, False)
        self.F4 = Square((400, 320), None, win, False)
        self.G4 = Square((480, 320), None, win, False)
        self.H4 = Square((560, 320), None, win, False)

        self.A5 = Square((0,240), None, win, False)
        self.B5 = Square((80, 240), None, win, False)
        self.C5 = Square((160, 240), None, win, False)
        self.D5 = Square((240, 240), None, win, False)
        self.E5 = Square((320, 240), None, win, False)
        self.F5 = Square((400, 240), None, win, False)
        self.G5 = Square((480, 240), None, win, False)
        self.H5 = Square((560, 240), None, win, False)

        self.A6 = Square((0,160), None, win, False)
        self.B6 = Square((80, 160), None, win, False)
        self.C6 = Square((160, 160), None, win, False)
        self.D6 = Square((240, 160), None, win, False)
        self.E6 = Square((320, 160), None, win, False)
        self.F6 = Square((400, 160), None, win, False)
        self.G6 = Square((480, 160), None, win, False)
        self.H6 = Square((560, 160), None, win, False)

        self.clickedSquare = self.A1
        self.pot_moves = []

        self.dict = {(0,560):self.A1, (0,480):self.A2, (0,400):self.A3, (0,320):self.A4, (0,240):self.A5, (0,160):self.A6, (0,80):self.A7, (0,0):self.A8,
                (80,560):self.B1, (80,480):self.B2, (80,400):self.B3, (80,320):self.B4, (80,240):self.B5, (80,160):self.B6, (80,80):self.B7, (80,0):self.B8,
                (160,560):self.C1, (160,480):self.C2, (160,400):self.C3, (160,320):self.C4, (160,240):self.C5, (160,160):self.C6, (160,80):self.C7, (160,0):self.C8,
                (240,560):self.D1, (240,480):self.D2, (240,400):self.D3, (240,320):self.D4, (240,240):self.D5, (240,160):self.D6, (240,80):self.D7, (240,0):self.D8,
                (320,560):self.E1, (320,480):self.E2, (320,400):self.E3, (320,320):self.E4, (320,240):self.E5, (320,160):self.E6, (320,80):self.E7, (320,0):self.E8,
                (400,560):self.F1, (400,480):self.F2, (400,400):self.F3, (400,320):self.F4, (400,240):self.F5, (400,160):self.F6, (400,80):self.F7, (400,0):self.F8,
                (480,560):self.G1, (480,480):self.G2, (480,400):self.G3, (480,320):self.G4, (480,240):self.G5, (480,160):self.G6, (480,80):self.G7, (480,0):self.G8,
                (560,560):self.H1, (560,480):self.H2, (560,400):self.H3, (560,320):self.H4, (560,240):self.H5, (560,160):self.H6, (560,80):self.H7, (560,0):self.H8}
    
        # we are probably gonna not need this
        self.list = [self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7, self.A8,
                self.B1, self.B2, self.B3, self.B4, self.B5, self.B6, self.B7, self.B8,
                self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7, self.C8,
                self.D1, self.D2, self.D3, self.D4, self.D5, self.D6, self.D7, self.D8,
                self.E1, self.E2, self.E3, self.E4, self.E5, self.E6, self.E7, self.E8,
                self.F1, self.F2, self.F3, self.F4, self.F5, self.F6, self.F7, self.F8,
                self.G1, self.G2, self.G3, self.G4, self.G5, self.G6, self.G7, self.G8,
                self.H1, self.H2, self.H3, self.H4, self.H5, self.H6, self.H7, self.H8]

    def getList(self):
        return self.list
    
    def getDict(self):
        return self.dict

        #print(dicti[(0, 560)].pos)