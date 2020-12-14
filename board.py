import pygame
from pieces import Rook, Knight, Bishop, Queen, King, Pawn

WHITE = 0
BLACK = 1

class Square:

    def __init__(self, pos, piece, win, isIt):
        self.pos = pos
        self.piece = piece
        self.isFull = isIt
    
    def show(self, win):
        if self.piece:
            win.blit(self.piece.img, self.pos)

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
        self.D3 = Square((340, 400), None, win, False)
        self.E3 = Square((320, 400), None, win, False)
        self.F3 = Square((400, 400), None, win, False)
        self.G3 = Square((480, 400), None, win, False)
        self.H3 = Square((560, 400), None, win, False)

        self.A4 = Square((0,320), None, win, False)
        self.B4 = Square((80, 320), None, win, False)
        self.C4 = Square((160, 320), None, win, False)
        self.D4 = Square((340, 320), None, win, False)
        self.E4 = Square((320, 320), None, win, False)
        self.F4 = Square((400, 320), None, win, False)
        self.G4 = Square((480, 320), None, win, False)
        self.H4 = Square((560, 320), None, win, False)

        self.A5 = Square((0,240), None, win, False)
        self.B5 = Square((80, 240), None, win, False)
        self.C5 = Square((160, 240), None, win, False)
        self.D5 = Square((340, 240), None, win, False)
        self.E5 = Square((320, 240), None, win, False)
        self.F5 = Square((400, 240), None, win, False)
        self.G5 = Square((480, 240), None, win, False)
        self.H5 = Square((560, 240), None, win, False)

        self.A6 = Square((0,160), None, win, False)
        self.B6 = Square((80, 160), None, win, False)
        self.C6 = Square((160, 160), None, win, False)
        self.D6 = Square((340, 160), None, win, False)
        self.E6 = Square((320, 160), None, win, False)
        self.F6 = Square((400, 160), None, win, False)
        self.G6 = Square((480, 160), None, win, False)
        self.H6 = Square((560, 160), None, win, False)
    
    def getList(self):
        return [self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7, self.A8,
                self.B1, self.B2, self.B3, self.B4, self.B5, self.B6, self.B7, self.B8,
                self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7, self.C8,
                self.D1, self.D2, self.D3, self.D4, self.D5, self.D6, self.D7, self.D8,
                self.E1, self.E2, self.E3, self.E4, self.E5, self.E6, self.E7, self.E8,
                self.F1, self.F2, self.F3, self.F4, self.F5, self.F6, self.F7, self.F8,
                self.G1, self.G2, self.G3, self.G4, self.G5, self.G6, self.G7, self.G8,
                self.H1, self.H2, self.H3, self.H4, self.H5, self.H6, self.H7, self.H8]
        