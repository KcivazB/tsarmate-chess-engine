import pytest
import numpy as np

from src.board import Board
from src.move_generator import generate_rook_moves

def test_initial_white_pieces():
    board = Board()
    assert np.array_equal(board.bitboards['white_pawn'][8:16], np.ones(8), "White Pawns have to be one the second rank")
    assert board.bitboards['white_rook'][0] == 1 and board.bitboards['white_rook'][7] == 1, "White rooks should be on the corners of the first rank"
    assert board.bitboards['white_knight'][1] == 1 and board.bitboards['white_knight'][6] == 1, "White knights should be next to the rooks on the first rank"
    assert board.bitboards['white_bishop'][2] == 1 and board.bitboards['white_bishop'][5] == 1, "White bishops should be next to the knights on the first rank"
    assert board.bitboards['white_queen'][3] == 1, "White queen should be on the fourth square of the first rank"
    assert board.bitboards['white_king'][4] == 1, "White king should be on the fifth square of the first rank"

def test_initial_black_pieces():
    board = Board()
    assert np.array_equal(board.bitboards['black_pawn'][48:56], np.ones(8)), "Black pawns should be on the seventh rank"
    assert board.bitboards['black_rook'][56] == 1 and board.bitboards['black_rook'][63] == 1, "Black rooks should be on the corners of the eighth rank"
    assert board.bitboards['black_knight'][57] == 1 and board.bitboards['black_knight'][62] == 1, "Black knights should be next to the rooks on the eighth rank"
    assert board.bitboards['black_bishop'][58] == 1 and board.bitboards['black_bishop'][61] == 1, "Black bishops should be next to the knights on the eighth rank"
    assert board.bitboards['black_queen'][59] == 1, "Black queen should be on the fourth square of the eighth rank"
    assert board.bitboards['black_king'][60] == 1, "Black king should be on the fifth square of the eighth rank"

def test_bitboard_state():
    board = Board()
    state = board.occupied_squares_bb
    expected_pieces = np.zeros(64, dtype=int)
    expected_pieces[0] = 1
    expected_pieces[7] = 1
    expected_pieces[1] = 1
    expected_pieces[6] = 1
    expected_pieces[2] = 1
    expected_pieces[5] = 1
    expected_pieces[3] = 1
    expected_pieces[4] = 1
    expected_pieces[8:16] = 1

    expected_pieces[63] = 1
    expected_pieces[56] = 1
    expected_pieces[62] = 1
    expected_pieces[57] = 1
    expected_pieces[61] = 1
    expected_pieces[58] = 1
    expected_pieces[59] = 1
    expected_pieces[60] = 1
    expected_pieces[48:56] = 1

    assert np.array_equal(state, expected_pieces), "The board state should match the expected initial position"
