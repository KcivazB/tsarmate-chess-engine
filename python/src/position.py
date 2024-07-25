from python.src.constants import Color

class Position : 
    def __init__(self): 
        self.board = None # Combiend pieces bitboards   
        self.color_to_move = Color.WHITE # First player is white
        self.castling_auth = { Color.WHITE : True, Color.BLACK : True } # Keeps track of castling authorizations
        self.en_passant_target = None # Store the target square of an en passant
        self.halfmove_clock = 0 # Takes care of enforcing the fifty-move rule. This counter is reset after captures or pawn moves, and incremented otherwise.

    def make_move(self, move):
        self.color_to_move = not self.color_to_move

        if not self.is_legal_move(move):
            print('Illegal Move !')
        
        self.update_bitboards(move)

    def update_bitboards(self, move):
        pass