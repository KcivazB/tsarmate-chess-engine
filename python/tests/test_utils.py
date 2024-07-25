import pytest
import numpy as np

from src.chess_engine import Board
from src.move_generator import generate_rook_moves

def test_conversion_index_to_chess_notation():
    board = Board()
    index = 0 
    result = board.index_to_chess_notation(index)
    expected_chess_notation = 'a1'
    assert result == expected_chess_notation

def test_conversion_chess_notation_to_index():
    board = Board()
    chess_notation = 'h8'
    result = board.chess_notation_to_index(chess_notation)
    expected_index = 63
    assert result == expected_index
