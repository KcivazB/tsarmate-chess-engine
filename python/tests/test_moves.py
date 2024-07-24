import pytest
import numpy as np

from src.chess_engine import Board
from src.move_generator import generate_rook_moves

def test_rook_moves():
    board = Board()
    rook_position = 'a1'
    valid_moves = board.get_rook_moves(rook_position)
    expected_moves = ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
    assert set(valid_moves) == set(expected_moves)
