import numpy as np 

def generate_rook_moves(position):
    directions = [8, -8, 1, -1]  # Up, Down, Right, Left
    moves = []

    for direction in directions:
        for i in range(1, 8):
            new_position = position + direction * i

            # Check if new_position is out of bounds
            if new_position < 0 or new_position >= 64:
                break

            # Check if the movement is invalid for horizontal directions
            if direction == 1 and new_position % 8 == 0:  # Moving right
                break
            if direction == -1 and new_position % 8 == 7:  # Moving left
                break

            # Add the new position to valid moves
            moves.append(new_position)

    return moves

def generate_bishop_moves(position):
    directions = [7, 9, -7, -9]  # UpLeft, UpRight, DownLeft, DownRight
    moves = []

    for direction in directions:
        for i in range(1, 8):
            new_position = position + direction * i

            # Check if new_position is out of bounds
            if new_position < 0 or new_position >= 64:
                break

            # Boundary checks to prevent wrapping around the edges
            new_row = new_position // 8
            new_col = new_position % 8

            # Moving up-left or down-right
            if direction in [7, -9]:
                if new_col > position % 8 or abs(new_row - position // 8) != abs(new_col - position % 8):
                    break

            # Moving up-right or down-left
            if direction in [9, -7]:
                if new_col < position % 8 or abs(new_row - position // 8) != abs(new_col - position % 8):
                    break

            moves.append(new_position)

    return moves

#Queen moves is the combination of rook and bishop moves. So here we go 
def generate_queen_moves(position): 
    rook_moves = generate_rook_moves(position)
    bishop_moves = generate_bishop_moves(position)
    moves = np.union1d(rook_moves, bishop_moves)
    return moves 

def generate_king_moves(position):
    directions = [8, 7, 9, 1, -1, -8, -7, -9]  # Up, UpLeft, UpRight, Right, Left, Down, DownRight, DownLeft
    moves = []
    for direction in directions:

        new_position = position + direction

        # Check if new_position is out of bounds
        if new_position < 0 or new_position >= 64:
            break

        # Boundary checks to prevent wrapping around the edges
        new_row = new_position // 8
        new_col = new_position % 8

        # Check if the movement is invalid for horizontal directions
        if direction == 1 and new_position % 8 == 0:  # Moving right
            break
        if direction == -1 and new_position % 8 == 7:  # Moving left
            break


        # Moving up-left or down-right
        if direction in [7, -9]:
            if new_col > position % 8 or abs(new_row - position // 8) != abs(new_col - position % 8):
                break

        # Moving up-right or down-left
        if direction in [9, -7]:
            if new_col < position % 8 or abs(new_row - position // 8) != abs(new_col - position % 8):
                break


        moves.append(new_position)
    return moves

#TODO ADD THE CONDITIONS FOR CASTLING 
#   Not moved yet
#   Not in chess AND Not ending in chess
#   None of the squares moving through is in chess

def generate_knight_moves(position):
    moves = []
    directions = [6, 15, 17, 10, -6, -15, -17, -10]  # NoWeWe, NoNoWe, NoNoEa, NoEaEa, SoEeEa, SoSoEa, SoSoWe, SoweWe
    
    for direction in directions:
        new_position = position + direction

        # Check if new_position is out of bounds
        if new_position < 0 or new_position >= 64:
            continue  # Continue instead of break to check other directions

        # Boundary checks to prevent wrapping around the edges
        current_row, current_col = divmod(position, 8)
        new_row, new_col = divmod(new_position, 8)

        if abs(current_row - new_row) == 2 and abs(current_col - new_col) == 1:
            moves.append(new_position)
        elif abs(current_row - new_row) == 1 and abs(current_col - new_col) == 2:
            moves.append(new_position)

    return moves


#TODO ADD THE CONDITIONS FOR PAWN PUSH + EN PASSANT + PROMOTE
def generate_pawn_moves(position):
    directions = [7, 8, 9, 16]
    moves = []

    for direction in directions : 
        new_position = position + direction 

        moves.append(new_position)
    return moves