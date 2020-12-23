import pygame

# these are all pygame surfaces. SMH
Rook_White = "Rook_White"
Knight_White = "Knight_White"
Bishop_White = "Bishop_White"
Queen_White = "Queen_White"
King_White = "King_White"
Pawn_White = "Pawn_White"

Rook_Black ="Rook_Black"
Knight_Black = "Knight_Black"
Bishop_Black = "Bishop_Black"
Queen_Black = "Queen_Black"
King_Black = "King_Black"
Pawn_Black = "Pawn_Black"

class Rook:
    def __init__(self, col):
        if col == 0:
            self.col = col
            self.img = Rook_White
        else:
            self.col = col
            self.img = Rook_Black

        self.has_moved = False
    
    def moves(self, pos, boardDict):
       
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
        self.block_col = []
        self.block_row = []

        # get all moves and put it in our list
        for i in range(1,8):
            if (pos[0], pos[1]+i*80) in boardDict:
                if boardDict[(pos[0], pos[1]+i*80)].piece != None:
                    if boardDict[(pos[0], pos[1]+i*80)].piece.col != self.col:
                        self.all_moves.append((pos[0], pos[1]+i*80))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0], pos[1]+i*80))

        for i in range(1,8):
            if (pos[0], pos[1]-i*80) in boardDict:
                if boardDict[(pos[0], pos[1]-i*80)].piece != None:
                    if boardDict[(pos[0], pos[1]-i*80)].piece.col != self.col:
                        self.all_moves.append((pos[0], pos[1]-i*80))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0], pos[1]-i*80))
        
        for i in range(1,8):
            if (pos[0]+i*80, pos[1]) in boardDict:
                if boardDict[(pos[0]+i*80, pos[1])].piece != None:
                    if boardDict[(pos[0]+i*80, pos[1])].piece.col != self.col:
                        self.all_moves.append((pos[0]+i*80, pos[1]))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0]+i*80, pos[1]))

        for i in range(1,8):
            if (pos[0]-i*80, pos[1]) in boardDict:
                if boardDict[(pos[0]-i*80, pos[1])].piece != None:
                    if boardDict[(pos[0]-i*80, pos[1])].piece.col != self.col:
                        self.all_moves.append((pos[0]-i*80, pos[1]))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0]-i*80, pos[1]))

class Knight:
    def __init__(self, col):
        if col == 0:
            self.col = col
            self.img = Knight_White
        else:
            self.col = col
            self.img = Knight_Black
    
    def moves(self, pos, boardDict):
        
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
    
    def moves(self, pos, boardDict):
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
        for i in range(1,8):
            if (pos[0]+i*80, pos[1]+i*80) in boardDict:
                if boardDict[(pos[0]+i*80, pos[1]+i*80)].piece != None:
                    if boardDict[(pos[0]+i*80, pos[1]+i*80)].piece.col != self.col:
                        self.all_moves.append((pos[0]+i*80, pos[1]+i*80))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0]+i*80, pos[1]+i*80))

        for i in range(1,8):
            if (pos[0]+i*80, pos[1]-i*80) in boardDict:
                if boardDict[(pos[0]+i*80, pos[1]-i*80)].piece != None:
                    if boardDict[(pos[0]+i*80, pos[1]-i*80)].piece.col != self.col:
                        self.all_moves.append((pos[0]+i*80, pos[1]-i*80))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0]+i*80, pos[1]-i*80))
        
        for i in range(1,8):
            if (pos[0]-i*80, pos[1]+i*80) in boardDict:
                if boardDict[(pos[0]-i*80, pos[1]+i*80)].piece != None:
                    if boardDict[(pos[0]-i*80, pos[1]+i*80)].piece.col != self.col:
                        self.all_moves.append((pos[0]-i*80, pos[1]+i*80))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0]-i*80, pos[1]+i*80))

        for i in range(1,8):
            if (pos[0]-i*80, pos[1]-i*80) in boardDict:
                if boardDict[(pos[0]-i*80, pos[1]-i*80)].piece != None:
                    if boardDict[(pos[0]-i*80, pos[1]-i*80)].piece.col != self.col:
                        self.all_moves.append((pos[0]-i*80, pos[1]-i*80))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0]-i*80, pos[1]-i*80))
            
class Queen:
    def __init__(self, col):
        if col == 0:
            self.col = col
            self.img = Queen_White
        else:
            self.col = col
            self.img = Queen_Black
    
    def moves(self, pos, boardDict):
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
        for i in range(1,8):
            if (pos[0]+i*80, pos[1]+i*80) in boardDict:
                if boardDict[(pos[0]+i*80, pos[1]+i*80)].piece != None:
                    if boardDict[(pos[0]+i*80, pos[1]+i*80)].piece.col != self.col:
                        self.all_moves.append((pos[0]+i*80, pos[1]+i*80))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0]+i*80, pos[1]+i*80))

        for i in range(1,8):
            if (pos[0]+i*80, pos[1]-i*80) in boardDict:
                if boardDict[(pos[0]+i*80, pos[1]-i*80)].piece != None:
                    if boardDict[(pos[0]+i*80, pos[1]-i*80)].piece.col != self.col:
                        self.all_moves.append((pos[0]+i*80, pos[1]-i*80))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0]+i*80, pos[1]-i*80))
        
        for i in range(1,8):
            if (pos[0]-i*80, pos[1]+i*80) in boardDict:
                if boardDict[(pos[0]-i*80, pos[1]+i*80)].piece != None:
                    if boardDict[(pos[0]-i*80, pos[1]+i*80)].piece.col != self.col:
                        self.all_moves.append((pos[0]-i*80, pos[1]+i*80))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0]-i*80, pos[1]+i*80))

        for i in range(1,8):
            if (pos[0]-i*80, pos[1]-i*80) in boardDict:
                if boardDict[(pos[0]-i*80, pos[1]-i*80)].piece != None:
                    if boardDict[(pos[0]-i*80, pos[1]-i*80)].piece.col != self.col:
                        self.all_moves.append((pos[0]-i*80, pos[1]-i*80))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0]-i*80, pos[1]-i*80))
        
        for i in range(1,8):
            if (pos[0], pos[1]+i*80) in boardDict:
                if boardDict[(pos[0], pos[1]+i*80)].piece != None:
                    if boardDict[(pos[0], pos[1]+i*80)].piece.col != self.col:
                        self.all_moves.append((pos[0], pos[1]+i*80))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0], pos[1]+i*80))

        for i in range(1,8):
            if (pos[0], pos[1]-i*80) in boardDict:
                if boardDict[(pos[0], pos[1]-i*80)].piece != None:
                    if boardDict[(pos[0], pos[1]-i*80)].piece.col != self.col:
                        self.all_moves.append((pos[0], pos[1]-i*80))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0], pos[1]-i*80))
        
        for i in range(1,8):
            if (pos[0]+i*80, pos[1]) in boardDict:
                if boardDict[(pos[0]+i*80, pos[1])].piece != None:
                    if boardDict[(pos[0]+i*80, pos[1])].piece.col != self.col:
                        self.all_moves.append((pos[0]+i*80, pos[1]))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0]+i*80, pos[1]))

        for i in range(1,8):
            if (pos[0]-i*80, pos[1]) in boardDict:
                if boardDict[(pos[0]-i*80, pos[1])].piece != None:
                    if boardDict[(pos[0]-i*80, pos[1])].piece.col != self.col:
                        self.all_moves.append((pos[0]-i*80, pos[1]))
                        break
                    else:
                        break
                else:
                    self.all_moves.append((pos[0]-i*80, pos[1]))

class King:
    def __init__(self, col):

        if col == 0:
            self.col = col
            self.img = King_White
        else:
            self.col = col
            self.img = King_Black

        self.has_moved = False
        self.castle_moves_white = {(160, 560):[(240, 560), (0, 560)], (480, 560):[(400, 560), (560, 560)]}
        self.castle_moves_black = {(160, 0):[(240, 0), (0, 0)], (480, 0):[(400, 0), (560, 0)]}
    
    def moves(self, pos, boardDict):

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
        self.all_moves = [(pos[0],pos[1]-80), (pos[0]+80,pos[1]-80), (pos[0]+80,pos[1]), 
                         (pos[0]+80,pos[1]+80), (pos[0],pos[1]+80), (pos[0]-80,pos[1]+80), 
                         (pos[0]-80,pos[1]), (pos[0]-80,pos[1]-80)]

        # if king hasn't moved. see if we should add the castling moves
        if not self.has_moved:
            if self.col == 0:
                castle_moves = [(0, 560), (560, 560)]
                for i in castle_moves:
                    if boardDict[i].piece != None:
                        if isinstance(boardDict[i].piece, Rook):
                            if not boardDict[i].piece.has_moved:
                                if (i == (0,560)) and (boardDict[(80,560)].piece == None) and (boardDict[(160, 560)].piece == None) and (boardDict[(240, 560)].piece == None):
                                    self.all_moves.append((160, 560))
                                elif (i == (560,560)) and (boardDict[(400,560)].piece == None) and (boardDict[(480, 560)].piece == None):
                                    self.all_moves.append((480, 560))
            else:
                castle_moves = [(0, 0), (560, 0)]
                for i in castle_moves:
                    if boardDict[i].piece != None:
                        if isinstance(boardDict[i].piece, Rook):
                            if not boardDict[i].piece.has_moved:
                                if (i == (0,0)) and (boardDict[(80,0)].piece == None) and (boardDict[(160, 0)].piece == None) and (boardDict[(240, 0)].piece == None):
                                    self.all_moves.append((160, 0))
                                elif (i == (560,0)) and (boardDict[(400,0)].piece == None) and (boardDict[(480, 0)].piece == None):
                                    self.all_moves.append((480, 0))        

class Pawn:
    def __init__(self, col, pos):
        if col == 0:
            self.col = col
            self.img = Pawn_White
        else:
            self.col = col
            self.img = Pawn_Black

        self.init_pos = pos     # need this because first move can move forward 2 spaces
    
    def moves(self, pos, boardDict):
        
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

        print(pot_moves)
        return pot_moves
    
    def update_all_moves(self, pos, boardDict):
        
        self.all_moves = []         # list of all our moves

        if self.col == 0:
            if pos == self.init_pos:
                mypos = [(pos[0], pos[1]-80), (pos[0], pos[1]-160)]  
            else:
                mypos = [(pos[0], pos[1]-80)]
            pot_moves = [(pos[0]+80, pos[1]-80), (pos[0]-80, pos[1]-80)]    # these are the diagonal moves

        else:
            if pos == self.init_pos:
                mypos = [(pos[0], pos[1]+80), (pos[0], pos[1]+160)]                                     # this is the forward move
            else:
                mypos = [(pos[0], pos[1]+80)]            
            pot_moves = [(pos[0]+80, pos[1]+80), (pos[0]-80, pos[1]+80)]    # these are the diagonal moves

        for pos in mypos:
            if pos in boardDict:  # if the forward position exists in our boardDictionary, execute
                if boardDict[pos].piece != None:  # if there is no piece on our forward move then append the position to our moves
                    break
                else:
                    self.all_moves.append(pos) 

        for pos in pot_moves:   # loop through our diagonal positions
            if pos in boardDict:    # if the position exists in our boardDictionary, execute
                if boardDict[pos].piece != None:    # if there is no piece there, we cannot move there. dont append position
                    if boardDict[pos].piece.col != self.col:    # if the piece there is the opposite colour, append move
                        self.all_moves.append(pos)