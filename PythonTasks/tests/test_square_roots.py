from unittest import TestCase
from square_roots import CalculateSquareRoot


class TestCalculateSquareRoot(TestCase):
    def test_compute_square_root_correct_output(self):
        output = 3
        square_root = CalculateSquareRoot(1, 9).compute_square_root()
        assert output == square_root

    def test_compute_square_root_incorrect_output(self):
        output = 4
        square_root = CalculateSquareRoot(1, 9).compute_square_root()
        assert output != square_root

    def test_compute_square_root_negative_output(self):
        output = -3
        square_root = CalculateSquareRoot(1, 9).compute_square_root()
        assert output != square_root

    def test_create_sequence_same_length(self):
        output = [4, 9, 16, 25, 36]
        created_sequence = CalculateSquareRoot(5, 3).create_sequence()
        assert output == created_sequence

    def test_create_sequence_different_length(self):
        output = [4, 9, 16, 25]
        created_sequence = CalculateSquareRoot(5, 3).create_sequence()
        assert output != created_sequence

    def test_create_sequence_string_instead_integer(self):
        output = ['4', '9', '16', '25', '36']
        created_sequence = CalculateSquareRoot(5, 3).create_sequence()
        assert output != created_sequence

