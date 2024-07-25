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

def test_knight_moves():
    board = Board()
    knight_position = 'b1'
    valid_moves = board.get_knight_moves(knight_position)
    expected_moves = ['a3', 'c3', 'd1']
    assert set(valid_moves) == set(expected_moves)


def test_bishop_moves():
    board = Board()
    bishop_position = 'c1'
    valid_moves = board.get_bishop_moves(bishop_position)
    expected_moves = ['b2', 'a3', 'd2', 'e3', 'f4', 'g5', 'h6']
    assert set(valid_moves) == set(expected_moves)


def test_queen_moves():
    board = Board()
    queen_position = 'd1'
    valid_moves = board.get_rook_moves(queen_position)
    expected_moves = ['d2','d3','d4','d5','d6','d7','d8','a1','b1','c1','e1','f1','g1','h1','c2','b3','a4','e2', 'f3', 'g4', 'h5']
    assert set(valid_moves) == set(expected_moves)