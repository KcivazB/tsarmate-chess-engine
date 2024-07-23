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

