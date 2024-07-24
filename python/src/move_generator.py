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

