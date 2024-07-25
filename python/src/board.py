import numpy as np
from .move_generator import generate_rook_moves, generate_bishop_moves, generate_queen_moves, generate_king_moves, generate_knight_moves  # generate_pawn_moves
from .utils import index_to_chess_notation, chess_notation_to_index
class Board:
    # PAWNS
    # ROOKS
    # KNIGHTS
    # BISHOPS
    # QUEEN
    # KING

    def __init__(self):
        self.bitboards = {
            'white_pawn': np.zeros(64, dtype=int),
            'white_rook': np.zeros(64, dtype=int),
            'white_knight': np.zeros(64, dtype=int),
            'white_bishop': np.zeros(64, dtype=int),
            'white_queen': np.zeros(64, dtype=int),
            'white_king': np.zeros(64, dtype=int),
            'black_pawn': np.zeros(64, dtype=int),
            'black_rook': np.zeros(64, dtype=int),
            'black_knight': np.zeros(64, dtype=int),
            'black_bishop': np.zeros(64, dtype=int),
            'black_queen': np.zeros(64, dtype=int),
            'black_king': np.zeros(64, dtype=int),
        }

        self.chars = {
            'white_pawn': "P",
            'white_rook': "R",
            'white_knight': "N",
            'white_bishop': "B",
            'white_queen': "Q",
            'white_king': "K",
            'black_pawn': "p",
            'black_rook': "r",
            'black_knight': "n",
            'black_bishop': "b",
            'black_queen': "q",
            'black_king': "k",
        }
        
        self.symbols = {
            'white_pawn': "P",
            'white_rook': "R",
            'white_knight': "N",
            'white_bishop': "B",
            'white_queen': "Q",
            'white_king': "K",
            'black_pawn': "p",
            'black_rook': "r",
            'black_knight': "n",
            'black_bishop': "b",
            'black_queen': "q",
            'black_king': "k",
        }
        
        self.init_pieces()

    @property
    def white_pieces_bb(self):
        return self.bitboards['white_pawn'] | self.bitboards['white_rook'] | self.bitboards['white_knight'] | self.bitboards['white_bishop'] | self.bitboards['white_queen'] | self.bitboards['white_king']

    @property
    def black_pieces_bb(self):
        return self.bitboards['black_pawn'] | self.bitboards['black_rook'] | self.bitboards['black_knight'] | self.bitboards['black_bishop'] | self.bitboards['black_queen'] | self.bitboards['black_king']

    @property
    def empty_squares_bb(self):
        return ~self.occupied_squares_bb

    @property
    def occupied_squares_bb(self):
        return self.white_pieces_bb | self.black_pieces_bb
    

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

    def get_rook_moves(self, notation):
        position = chess_notation_to_index(notation)
        occupied_squares = self.occupied_squares_bb
        potential_moves = generate_rook_moves(position)
        
        #Check for move validity here and loop over valid moves
        return [index_to_chess_notation(move) for move in potential_moves]

    def get_bishop_moves(self, notation):
        position = chess_notation_to_index(notation)
        occupied_squares = self.occupied_squares_bb
        potential_moves = generate_bishop_moves(position)

        #Check for move validity here and loop over valid moves
        return [index_to_chess_notation(move) for move in potential_moves]

    def get_queen_moves(self, notation):
        position = chess_notation_to_index(notation)
        occupied_squares = self.occupied_squares_bb
        potential_moves = generate_queen_moves(position)

        #Check for move validity here and loop over valid moves
        return [index_to_chess_notation(move) for move in potential_moves]

    def get_king_moves(self, notation):
        position = chess_notation_to_index(notation)
        occupied_squares = self.occupied_squares_bb
        potential_moves = generate_king_moves(position)

        #Check for move validity here and loop over valid moves
        return [index_to_chess_notation(move) for move in potential_moves]

    def get_knight_moves(self, notation):
        position = chess_notation_to_index(notation)
        occupied_squares = self.occupied_squares_bb
        potential_moves = generate_knight_moves(position)

        #Check for move validity here and loop over valid moves
        return [index_to_chess_notation(move) for move in potential_moves]

   
    def pretty_print_bitboard(self, bitboard):
        files = 'abcdefgh'
        ranks = '12345678'
        val = '  ' + ' '.join(files) + '\n'
        
        for rank in range(8):
            row = ranks[7 - rank] + ' '
            for file in range(8):
                index = (7 - rank) * 8 + file
                if bitboard[index]:
                    for piece, piece_bitboard in self.bitboards.items():
                        if piece_bitboard[index]:
                            row += self.symbols[piece] + ' '
                            break 
                else:
                    row += '- '
            val += row + ' ' + ranks[7 - rank] + '\n'
        
        val += '  ' + ' '.join(files)
        print(val)