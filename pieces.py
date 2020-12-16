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

        self.surface = pygame.Surface((70,70))
        self.surface.set_alpha(128)
        self.surface.fill ((255,0,0))
    
    def moves(self, pos, win, boardDict):
       
        self.update_all_moves(pos, boardDict)

        pot_moves = []

        # loop for all potential moves
        for pos in self.all_moves:   
            if pos in boardDict:    # if the position is in our board dictionary, continue
                if boardDict[pos].piece != None:    # if the position has a piece do the if statement
                    if boardDict[pos].piece.col != self.col:    # if the piece is the opposite colour of us, make the highlight
                        boardDict[pos].highlightme = True
                        pot_moves.append(pos)
                else:
                    boardDict[pos].highlightme = True
                    pot_moves.append(pos)

        return pot_moves

    def update_all_moves(self, pos, boardDict):

        self.all_moves = []

        # get all moves and put it in our list
        for i in range(8):
            self.all_moves.append((pos[0], pos[1]+i*80))
            self.all_moves.append((pos[0], pos[1]-i*80))
            self.all_moves.append((pos[0]+i*80, pos[1]))
            self.all_moves.append((pos[0]-i*80, pos[1]))

class Knight:
    def __init__(self, col):
        if col == 0:
            self.col = col
            self.img = Knight_White
        else:
            self.col = col
            self.img = Knight_Black
    
    def moves(self, pos, win, boardDict):
        
        self.update_all_moves(pos)
        
        pot_moves = []

        # loop for all potential moves
        for pos in self.all_moves:   
            if pos in boardDict:    # if the position is in our board dictionary, continue
                if boardDict[pos].piece != None:    # if the position has a piece do the if statement
                    if boardDict[pos].piece.col != self.col:    # if the piece is the opposite colour of us, make the highlight
                        boardDict[pos].highlightme = True
                        pot_moves.append(pos)
                else:
                    boardDict[pos].highlightme = True
                    pot_moves.append(pos)

        return pot_moves
    
    def update_all_moves(self, pos):
        self.all_moves = [(pos[0]-80, pos[1]-160), (pos[0]+80, pos[1]-160), (pos[0]+160, pos[1]-80), (pos[0]+160, pos[1]+80),
                          (pos[0]-80, pos[1]+160), (pos[0]+80, pos[1]+160), (pos[0]-160, pos[1]-80), (pos[0]-160, pos[1]+80)]

class Bishop:
    def __init__(self, col):
        if col == 0:
            self.col = col
            self.img = Bishop_White
        else:
            self.col = col
            self.img = Bishop_Black

        self.surface = pygame.Surface((70,70))
        self.surface.set_alpha(128)
        self.surface.fill ((255,0,0))
    
    def moves(self, pos, win, boardDict):
        self.update_all_moves(pos)
        
        pot_moves = []

        # loop for all potential moves
        for pos in self.all_moves:   
            if pos in boardDict:    # if the position is in our board dictionary, continue
                if boardDict[pos].piece != None:    # if the position has a piece do the if statement
                    if boardDict[pos].piece.col != self.col:    # if the piece is the opposite colour of us, make the highlight
                        boardDict[pos].highlightme = True
                        pot_moves.append(pos)
                else:
                    boardDict[pos].highlightme = True
                    pot_moves.append(pos)

        return pot_moves


    def update_all_moves(self, pos):

        self.all_moves = []

        # get all moves and put it in our list
        for i in range(8):
            self.all_moves.append((pos[0]+i*80, pos[1]+i*80))
            self.all_moves.append((pos[0]+i*80, pos[1]-i*80))
            self.all_moves.append((pos[0]-i*80, pos[1]+i*80))
            self.all_moves.append((pos[0]-i*80, pos[1]-i*80))
            
class Queen:
    def __init__(self, col):
        if col == 0:
            self.col = col
            self.img = Queen_White
        else:
            self.col = col
            self.img = Queen_Black

        self.surface = pygame.Surface((70,70))
        self.surface.set_alpha(128)
        self.surface.fill ((255,0,0))
    
    def moves(self, pos, win, boardDict):
        self.update_all_moves(pos)
        
        pot_moves = []

        # loop for all potential moves
        for pos in self.all_moves:   
            if pos in boardDict:    # if the position is in our board dictionary, continue
                if boardDict[pos].piece != None:    # if the position has a piece do the if statement
                    if boardDict[pos].piece.col != self.col:    # if the piece is the opposite colour of us, make the highlight
                        boardDict[pos].highlightme = True
                        pot_moves.append(pos)
                else:
                    boardDict[pos].highlightme = True
                    pot_moves.append(pos)

        return pot_moves

    def update_all_moves(self, pos):

        self.all_moves = []

        # get all moves and put it in our list
        for i in range(8):
            self.all_moves.append((pos[0]+i*80, pos[1]+i*80))
            self.all_moves.append((pos[0]+i*80, pos[1]-i*80))
            self.all_moves.append((pos[0]-i*80, pos[1]+i*80))
            self.all_moves.append((pos[0]-i*80, pos[1]-i*80))
            self.all_moves.append((pos[0], pos[1]+i*80))
            self.all_moves.append((pos[0], pos[1]-i*80))
            self.all_moves.append((pos[0]+i*80, pos[1]))
            self.all_moves.append((pos[0]-i*80, pos[1]))

class King:
    def __init__(self, col):

        if col == 0:
            self.col = col
            self.img = King_White
        else:
            self.col = col
            self.img = King_Black
    
    def moves(self, pos, win, boardDict):

        self.update_all_moves(pos)

        pot_moves = []
        
        # loop for all potential moves
        for pos in self.all_moves:   
            if pos in boardDict:    # if the position is in our board dictionary, continue
                if boardDict[pos].piece != None:    # if the position has a piece do the if statement
                    if boardDict[pos].piece.col != self.col:    # if the piece is the opposite colour of us, make the highlight
                        boardDict[pos].highlightme = True
                        pot_moves.append(pos)
                else:
                    boardDict[pos].highlightme = True
                    pot_moves.append(pos)

        return pot_moves

    def update_all_moves(self, pos):
        self.all_moves = [(pos[0],pos[1]-80), (pos[0]+80,pos[1]-80), (pos[0]+80,pos[1]), 
                         (pos[0]+80,pos[1]+80), (pos[0],pos[1]+80), (pos[0]-80,pos[1]+80), 
                         (pos[0]-80,pos[1]), (pos[0]-80,pos[1]-80)]

class Pawn:
    def __init__(self, col):
        if col == 0:
            self.col = col
            self.img = Pawn_White
        else:
            self.col = col
            self.img = Pawn_Black

        self.first_move = True
    
    def moves(self, pos, win, boardDict):
        
        self.update_all_moves(pos, boardDict)

        pot_moves = []

        # loop for all potential moves
        for pos in self.all_moves:   
            if pos in boardDict:    # if the position is in our board dictionary, continue
                if boardDict[pos].piece != None:    # if the position has a piece do the if statement
                    if boardDict[pos].piece.col != self.col:    # if the piece is the opposite colour of us, make the highlight
                        boardDict[pos].highlightme = True
                        pot_moves.append(pos)
                else:
                    boardDict[pos].highlightme = True
                    pot_moves.append(pos)

        return pot_moves
    
    def update_all_moves(self, pos, boardDict):
        
        self.all_moves = []         # list of all our moves

        if self.col == 0:
            mypos = (pos[0], pos[1]-80)                                     # this is the forward move
            pot_moves = [(pos[0]+80, pos[1]-80), (pos[0]-80, pos[1]-80)]    # these are the diagonal moves

        else:
            mypos = (pos[0], pos[1]+80)                                     # this is the forward move
            pot_moves = [(pos[0]+80, pos[1]+80), (pos[0]-80, pos[1]+80)]    # these are the diagonal moves

        if mypos in boardDict:  # if the forward position exists in our boardDictionary, execute
            if boardDict[mypos].piece == None:  # if there is no piece on our forward move then append the position to our moves
                self.all_moves.append(mypos) 

        for pos in pot_moves:   # loop through our diagonal positions
            if pos in boardDict:    # if the position exists in our boardDictionary, execute
                if boardDict[pos].piece != None:    # if there is no piece there, we cannot move there. dont append position
                    if boardDict[pos].piece.col != self.col:    # if the piece there is the opposite colour, append move
                        self.all_moves.append(pos)
            