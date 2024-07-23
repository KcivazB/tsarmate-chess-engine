import numpy as np

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
    
    def get_bitboard_state(self):
        result = np.zeros(64, dtype = int)
        for bitboard in self.bitboards.values():
            result = np.bitwise_or(bitboard, result, dtype = int)
        return result
            
    def pretty_print(self):
        combined_board = self.get_bitboard_state()
        val = ''
        for i, square in enumerate(combined_board):
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