import pygame

Rook_White = pygame.image.load("imgs/Rook_White.png")
Knight_White = pygame.image.load("imgs/Knight_White.png")
Bishop_White = pygame.image.load("imgs/Bishop_White.png")
Queen_White = pygame.image.load("imgs/Queen_White.png")
King_White = pygame.image.load("imgs/King_White.png")
Pawn_White = pygame.image.load("imgs/Pawn_White.png")

Rook_Black = pygame.image.load("imgs/Rook_Black.png")
Knight_Black = pygame.image.load("imgs/Knight_Black.png")
Bishop_Black = pygame.image.load("imgs/Bishop_Black.png")
Queen_Black = pygame.image.load("imgs/Queen_Black.png")
King_Black = pygame.image.load("imgs/King_Black.png")
Pawn_Black = pygame.image.load("imgs/Pawn_Black.png")

class Rook:
    def __init__(self, col):
        if col == 0:
            self.img = Rook_White
        else:
            self.img = Rook_Black

class Knight:
    def __init__(self, col):
        if col == 0:
            self.img = Knight_White
        else:
            self.img = Knight_Black

class Bishop:
    def __init__(self, col):
        if col == 0:
            self.img = Bishop_White
        else:
            self.img = Bishop_Black
            
class Queen:
    def __init__(self, col):
        if col == 0:
            self.img = Queen_White
        else:
            self.img = Queen_Black

class King:
    def __init__(self, col):
        if col == 0:
            self.img = King_White
        else:
            self.img = King_Black

class Pawn:
    def __init__(self, col):
        if col == 0:
            self.img = Pawn_White
        else:
            self.img = Pawn_Black