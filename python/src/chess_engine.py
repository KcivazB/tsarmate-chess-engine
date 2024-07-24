import numpy as np
from .move_generator import generate_rook_moves, generate_bishop_moves, generate_queen_moves, generate_king_moves, generate_knight_moves # generate_pawn_moves

class Board():
    
    #PAWNS
    #ROOKS
    #KNIGHTS
    #BISHOPS
    #QUEEN
    #KING
    
    def __init__(self):
        self.bitboards = {
            'white_pawn' : np.zeros(64, dtype = int),
            'white_rook' : np.zeros(64, dtype = int),
            'white_knight' : np.zeros(64, dtype = int),
            'white_bishop' : np.zeros(64, dtype = int),
            'white_queen' : np.zeros(64, dtype = int),
            'white_king' : np.zeros(64, dtype = int),
            'black_pawn' : np.zeros(64, dtype = int),
            'black_rook' : np.zeros(64, dtype = int),
            'black_knight' : np.zeros(64, dtype = int),
            'black_bishop' : np.zeros(64, dtype = int),
            'black_queen' : np.zeros(64, dtype = int),
            'black_king' : np.zeros(64, dtype = int),
        }

        self.init_pieces()
    
    def get_occupied_squares_bitboard(self):
        result = np.zeros(64, dtype = int)
        for bitboard in self.bitboards.values():
            result = np.bitwise_or(bitboard, result, dtype = int)
        return result
            
    def get_empty_squares_bitboard(self):
        return 1- self.get_occupied_squares_bitboard()

    def pretty_print_bitboard(self, bitboard):
        val = ''
        for i, square in enumerate(bitboard):
            if not i % 8:
                val += '\n'
            if square:
                val += 'X'
            else:
                val += '-'
        print(val)
        
    def init_pieces(self):
        self.bitboards['white_rook'][0] = 1
        self.bitboards['white_rook'][7] = 1
        self.bitboards['white_knight'][1] = 1
        self.bitboards['white_knight'][6] = 1
        self.bitboards['white_bishop'][2] = 1
        self.bitboards['white_bishop'][5] = 1
        self.bitboards['white_queen'][3] = 1
        self.bitboards['white_king'][4] = 1

        self.bitboards['white_pawn'][8:16] = 1

        self.bitboards['black_rook'][63] = 1
        self.bitboards['black_rook'][56] = 1
        self.bitboards['black_knight'][62] = 1
        self.bitboards['black_knight'][57] = 1
        self.bitboards['black_bishop'][61] = 1
        self.bitboards['black_bishop'][58] = 1
        self.bitboards['black_queen'][59] = 1
        self.bitboards['black_king'][60] = 1
        
        self.bitboards['black_pawn'][48:56] = 1
        
    def get_rook_moves(self, position):
        all_moves = generate_rook_moves(position)
        #Check valid moves
        return all_moves
    
    def get_bishop_moves(self, position):
        all_moves = generate_bishop_moves(position)
        #Check valid moves
        return all_moves
    
    def get_queen_moves(self, position):
        all_moves = generate_queen_moves(position)
        #Check valid moves
        return all_moves
    
    def get_king_moves(self, position):
        all_moves = generate_king_moves(position)
        #Check valid moves
        return all_moves
    
    def get_knight_moves(self, position):
        all_moves= generate_knight_moves(position)
        #Check valid moves
        return all_moves