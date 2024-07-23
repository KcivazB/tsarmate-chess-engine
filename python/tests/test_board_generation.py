import pytest
import numpy as np

from ..src.chess_engine_python import Board

def test_initial_white_pieces():
    board = Board()
    assert np.array_equal(board.bitboards['white_pawns'][8:16], np.ones(8), "White Pawns have to be one the second rank")