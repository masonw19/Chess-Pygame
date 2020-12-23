import pygame
from pygame.locals import Rect
from pieces import Rook, Knight, Bishop, Queen, King, Pawn

WHITE = 0
BLACK = 1
pygame.init()

class Square:

    def __init__(self, pos, piece, isIt):
        self.pos = pos
        self.piece = piece
        self.isFull = isIt
        self.clicked = False
        self.highlightme = False

        self.square = Rect(self.pos[0], self.pos[1], 80, 80)

    def show(self):
        if self.piece:
            return [True, self.piece.img, self.pos]
        return [False, None, self.pos]

    # turn on the highlightme of all potential spots and return a list of the potiential spots
    def show_moves(self, boardDict):
        if self.isFull:
            return self.piece.moves(self.pos, boardDict)
        return []

    # highlight the square   
    def get_highlight(self):
        return [self.highlightme, self.clicked, self.pos]

    # when we click a square we need to highlight the clicked square and then get info on potential moves
    def update_squares(self, board, n):
        #win.blit(surface, (self.pos[0]+5,self.pos[1]+5))

        # if the square we clicked is the same as the previous, just keep the square highglighted
        if self.pos == board.clickedSquares[board.turn].pos:
            board.pot_moves = self.show_moves(board.dict)

        # if the square we clicked is a potential move square, we need to update our clicked square and move our piece
        elif self.pos in board.pot_moves:                
            self.update_board(board, n)    # update the board
            print(self.pos)

            self.release_highlight(board)   # release all old highlights

        # else do ....
        else:
            board.clickedSquares[board.turn].clicked = False
            board.clickedSquares[board.turn].highlightme = False

            self.release_highlight(board)

            board.pot_moves = self.show_moves(board.dict)
            board.clickedSquares[board.turn] = self
            board.clickedSquares[board.turn].clicked = True
            board.clickedSquares[board.turn].highlightme = True
    
    def check_castling(self, board):
        if isinstance(board.clickedSquares[board.turn].piece, King):
            if board.clickedSquares[board.turn].piece.col == 0:
                if not board.clickedSquares[board.turn].piece.has_moved and (self.pos in board.clickedSquares[board.turn].piece.castle_moves_white):
                    moveRook = board.dict[board.clickedSquares[board.turn].piece.castle_moves_white[self.pos][0]]
                    moveRook.piece = board.dict[board.clickedSquares[board.turn].piece.castle_moves_white[self.pos][1]].piece
                    moveRook.isFull = True

                    board.dict[board.clickedSquares[board.turn].piece.castle_moves_white[self.pos][1]].piece = None
                    board.dict[board.clickedSquares[board.turn].piece.castle_moves_white[self.pos][1]].isFull = False
            else:
                if not board.clickedSquares[board.turn].piece.has_moved and (self.pos in board.clickedSquares[board.turn].piece.castle_moves_black):
                    moveRook = board.dict[board.clickedSquares[board.turn].piece.castle_moves_black[self.pos][0]]
                    moveRook.piece = board.dict[board.clickedSquares[board.turn].piece.castle_moves_black[self.pos][1]].piece
                    moveRook.isFull = True

                    board.dict[board.clickedSquares[board.turn].piece.castle_moves_black[self.pos][1]].piece = None
                    board.dict[board.clickedSquares[board.turn].piece.castle_moves_black[self.pos][1]].isFull = False

    # update the clicked square and move piece
    def update_board(self, board, n):
        # here we will check if the king or the rooks have moved. this is needed for castling functionality
        self.check_castling(board)
        
        if isinstance(board.clickedSquares[board.turn].piece, Rook) or isinstance(board.clickedSquares[board.turn].piece, King):
            board.clickedSquares[board.turn].piece.has_moved = True


        self.piece = board.clickedSquares[board.turn].piece 
        self.isFull = True         # set that the square is now full
        self.clicked = False       # clicked is false
        
        board.clickedSquares[board.turn].piece = None
        board.clickedSquares[board.turn].clicked = False
        board.clickedSquares[board.turn].isFull = False
        board.clickedSquares[board.turn].highlightme = False
        
        board.clickedSquares[board.turn] = self
        board.clickedSquares[board.turn].highlightme = False
        board.clickedSquares[board.turn].clicked = False

        if board.turn == WHITE:
            board.turn = BLACK
        else:
            board.turn = WHITE
        
        self.release_highlight(board)   # release the highlighted squares
        board.pot_moves = []            # clear our potential moves
        n.send(board)
        board.my_turn = False
        print("here")

    def release_highlight(self, board):
        for move in board.pot_moves:
            if move in board.dict:
                board.dict[move].highlightme = False

    def squareClicked(self, coords, board):
        if self.square.collidepoint(coords) and ((self.piece == None) or (self.piece.col == board.turn) or (self.pos in board.pot_moves)):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
                self.highlightme = True

class Board:

    def __init__(self, my_turn):

        self.my_turn = my_turn

        self.A1 = Square((0,560), Rook(WHITE), True)
        self.B1 = Square((80,560), Knight(WHITE), True)
        self.C1 = Square((160,560), Bishop(WHITE), True)
        self.D1 = Square((240,560), Queen(WHITE), True) 
        self.E1 = Square((320,560), King(WHITE), True)
        self.F1 = Square((400,560), Bishop(WHITE), True)
        self.G1 = Square((480,560), Knight(WHITE), True)
        self.H1 = Square((560,560), Rook(WHITE), True)
        self.A2 = Square((0,480), Pawn(WHITE,(0,480)), True)
        self.B2 = Square((80,480), Pawn(WHITE,(80,480)), True)
        self.C2 = Square((160,480), Pawn(WHITE,(160,480)), True)
        self.D2 = Square((240,480), Pawn(WHITE,(240,480)), True)
        self.E2 = Square((320,480), Pawn(WHITE,(320,480)), True)
        self.F2 = Square((400,480), Pawn(WHITE,(400,480)), True)
        self.G2 = Square((480,480), Pawn(WHITE,(480,480)), True)
        self.H2 = Square((560,480), Pawn(WHITE,(560,480)), True)

        self.A8 = Square((0,0), Rook(BLACK), True)
        self.B8 = Square((80,0), Knight(BLACK), True)
        self.C8 = Square((160,0), Bishop(BLACK), True)
        self.D8 = Square((240,0), Queen(BLACK), True)
        self.E8 = Square((320,0), King(BLACK), True)
        self.F8 = Square((400,0), Bishop(BLACK), True)
        self.G8 = Square((480,0), Knight(BLACK), True)
        self.H8 = Square((560,0), Rook(BLACK), True)
        self.A7 = Square((0,80), Pawn(BLACK,(0,80)), True)
        self.B7 = Square((80,80), Pawn(BLACK,(80,80)), True)
        self.C7 = Square((160,80), Pawn(BLACK,(160,80)), True)
        self.D7 = Square((240,80), Pawn(BLACK,(240,80)), True)
        self.E7 = Square((320,80), Pawn(BLACK,(320,80)), True)
        self.F7 = Square((400,80), Pawn(BLACK,(400,80)), True)
        self.G7 = Square((480,80), Pawn(BLACK,(480,80)), True)
        self.H7 = Square((560,80), Pawn(BLACK,(560,80)), True)

        self.A3 = Square((0,400), None, False)
        self.B3 = Square((80, 400), None, False)
        self.C3 = Square((160, 400), None, False)
        self.D3 = Square((240, 400), None, False)
        self.E3 = Square((320, 400), None, False)
        self.F3 = Square((400, 400), None, False)
        self.G3 = Square((480, 400), None, False)
        self.H3 = Square((560, 400), None, False)

        self.A4 = Square((0,320), None, False)
        self.B4 = Square((80, 320), None, False)
        self.C4 = Square((160, 320), None, False)
        self.D4 = Square((240, 320), None, False)
        self.E4 = Square((320, 320), None, False)
        self.F4 = Square((400, 320), None, False)
        self.G4 = Square((480, 320), None, False)
        self.H4 = Square((560, 320), None, False)

        self.A5 = Square((0,240), None, False)
        self.B5 = Square((80, 240), None, False)
        self.C5 = Square((160, 240), None, False)
        self.D5 = Square((240, 240), None, False)
        self.E5 = Square((320, 240), None, False)
        self.F5 = Square((400, 240), None, False)
        self.G5 = Square((480, 240), None, False)
        self.H5 = Square((560, 240), None, False)

        self.A6 = Square((0,160), None, False)
        self.B6 = Square((80, 160), None, False)
        self.C6 = Square((160, 160), None, False)
        self.D6 = Square((240, 160), None, False)
        self.E6 = Square((320, 160), None, False)
        self.F6 = Square((400, 160), None, False)
        self.G6 = Square((480, 160), None, False)
        self.H6 = Square((560, 160), None, False)

        self.dict = {(0,560):self.A1, (0,480):self.A2, (0,400):self.A3, (0,320):self.A4, (0,240):self.A5, (0,160):self.A6, (0,80):self.A7, (0,0):self.A8,
                (80,560):self.B1, (80,480):self.B2, (80,400):self.B3, (80,320):self.B4, (80,240):self.B5, (80,160):self.B6, (80,80):self.B7, (80,0):self.B8,
                (160,560):self.C1, (160,480):self.C2, (160,400):self.C3, (160,320):self.C4, (160,240):self.C5, (160,160):self.C6, (160,80):self.C7, (160,0):self.C8,
                (240,560):self.D1, (240,480):self.D2, (240,400):self.D3, (240,320):self.D4, (240,240):self.D5, (240,160):self.D6, (240,80):self.D7, (240,0):self.D8,
                (320,560):self.E1, (320,480):self.E2, (320,400):self.E3, (320,320):self.E4, (320,240):self.E5, (320,160):self.E6, (320,80):self.E7, (320,0):self.E8,
                (400,560):self.F1, (400,480):self.F2, (400,400):self.F3, (400,320):self.F4, (400,240):self.F5, (400,160):self.F6, (400,80):self.F7, (400,0):self.F8,
                (480,560):self.G1, (480,480):self.G2, (480,400):self.G3, (480,320):self.G4, (480,240):self.G5, (480,160):self.G6, (480,80):self.G7, (480,0):self.G8,
                (560,560):self.H1, (560,480):self.H2, (560,400):self.H3, (560,320):self.H4, (560,240):self.H5, (560,160):self.H6, (560,80):self.H7, (560,0):self.H8}
    
        self.list = [self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7, self.A8,
                self.B1, self.B2, self.B3, self.B4, self.B5, self.B6, self.B7, self.B8,
                self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7, self.C8,
                self.D1, self.D2, self.D3, self.D4, self.D5, self.D6, self.D7, self.D8,
                self.E1, self.E2, self.E3, self.E4, self.E5, self.E6, self.E7, self.E8,
                self.F1, self.F2, self.F3, self.F4, self.F5, self.F6, self.F7, self.F8,
                self.G1, self.G2, self.G3, self.G4, self.G5, self.G6, self.G7, self.G8,
                self.H1, self.H2, self.H3, self.H4, self.H5, self.H6, self.H7, self.H8]
        
        self.clickedSquares = [self.A1, self.A8]
        self.pot_moves = []
        self.turn = WHITE

        self.disc = False   # TESTING

    def getList(self):
        return self.list
    
    def getDict(self):
        return self.dict