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
            self.col = col
            self.img = Rook_White
        else:
            self.col = col
            self.img = Rook_Black
    
    def moves(self, pos, win):
        if self.col == 0:
            pass
        else:
            pass

class Knight:
    def __init__(self, col):
        if col == 0:
            self.col = col
            self.img = Knight_White
        else:
            self.col = col
            self.img = Knight_Black
    
    def moves(self, pos, win):
        if self.col == 0:
            pass
        else:
            pass

class Bishop:
    def __init__(self, col):
        if col == 0:
            self.col = col
            self.img = Bishop_White
        else:
            self.col = col
            self.img = Bishop_Black
    
    def moves(self, pos, win):
        if self.col == 0:
            pass
        else:
            pass
            
class Queen:
    def __init__(self, col):
        if col == 0:
            self.col = col
            self.img = Queen_White
        else:
            self.col = col
            self.img = Queen_Black
    
    def moves(self, pos, win):
        if self.col == 0:
            pass
        else:
            pass

class King:
    def __init__(self, col):
        if col == 0:
            self.col = col
            self.img = King_White
        else:
            self.col = col
            self.img = King_Black
    
    def moves(self, pos, win):
        if self.col == 0:
            pass
        else:
            pass

class Pawn:
    def __init__(self, col):
        if col == 0:
            self.col = col
            self.img = Pawn_White
        else:
            self.col = col
            self.img = Pawn_Black

        self.surface = pygame.Surface((70,70))
        self.surface.set_alpha(128)
        self.surface.fill ((255,0,0))
    
    def moves(self, pos, win):
        pot_moves = []
        if self.col == 0:
            pos = (pos[0], pos[1]-80)
            pot_moves.append(pos)
            #pygame.draw.circle(win, (255,0,0), (pos[0]+40, pos[1]+40), 15)
            win.blit(self.surface, (pos[0]+5,pos[1]+5))
        else:
            pos = (pos[0], pos[1]+80)
            pot_moves.append(pos)
            #pygame.draw.circle(win, (255,0,0), (pos[0]+40, pos[1]+40), 15)
            win.blit(self.surface, (pos[0]+5,pos[1]+5))

        return pot_moves