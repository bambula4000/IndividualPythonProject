from unittest import TestCase
from chess_board import ChessBoard


class TestChessBoard(TestCase):

    def test_make_chess_board_same_size(self):
        output = [
            ['☻', '☺', '☻', '☺', '☻'],
            ['☺', '☻', '☺', '☻', '☺'],
            ['☻', '☺', '☻', '☺', '☻'],
            ['☺', '☻', '☺', '☻', '☺'],
            ['☻', '☺', '☻', '☺', '☻'],
        ]
        chess_board = ChessBoard(5, 5).make_chess_board()
        assert output == chess_board

    def test_make_chess_board_different_height(self):
        output = [
            ['☻', '☺', '☻', '☺', '☻'],
            ['☺', '☻', '☺', '☻', '☺'],
            ['☻', '☺', '☻', '☺', '☻'],
        ]
        chess_board = ChessBoard(5, 5).make_chess_board()
        assert output != chess_board

    def test_make_chess_board_all_char_the_same(self):
        output = [
            ['☻', '☻', '☻', '☻', '☻'],
            ['☻', '☻', '☻', '☻', '☻'],
            ['☻', '☻', '☻', '☻', '☻'],
        ]
        chess_board = ChessBoard(5, 3).make_chess_board()
        assert output != chess_board

    def test_make_chess_board_negative_different_width(self):
        output = [
            ['☻', '☺', '☻', '☺', '☻'],
            ['☺', '☻', '☺', '☻', '☺'],
            ['☻', '☺', '☻', '☺', '☻'],
        ]
        chess_board = ChessBoard(4, 3).make_chess_board()
        assert output != chess_board

    def test_make_chess_board_integer_instead_string(self):
        output = [
            [1, 2, 1, 2, 1],
            ['☺', '☻', '☺', '☻', '☺'],
            ['☻', '☺', '☻', '☺', '☻'],
        ]
        chess_board = ChessBoard(4, 3).make_chess_board()
        assert output != chess_board
