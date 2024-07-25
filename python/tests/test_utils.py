import pytest
import numpy as np

from src.utils import index_to_chess_notation, chess_notation_to_index

def test_conversion_index_to_chess_notation():
    index = 0 
    result = index_to_chess_notation(index)
    expected_chess_notation = 'a1'
    assert result == expected_chess_notation

def test_conversion_chess_notation_to_index():
    chess_notation = 'h8'
    result = chess_notation_to_index(chess_notation)
    expected_index = 63
    assert result == expected_index
