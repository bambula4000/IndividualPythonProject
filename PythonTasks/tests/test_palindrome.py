from unittest import TestCase
from palindrome import PalindromeInInputString


class TestPalindromeInInputString(TestCase):
    def test_calculate_palindromes_same_count_of_palindromes(self):
        output = ['bb', 'zz', 'dd']
        count_palindromes = PalindromeInInputString('bbaxzzsdd').calculate_palindromes()
        assert output == count_palindromes

    def test_calculate_palindromes_different_count_of_palindromes(self):
        output = ['bb', 'zz', 'dd']
        count_palindromes = PalindromeInInputString('asddsa').calculate_palindromes()
        assert output != count_palindromes

    def test_calculate_palindromes_if_no_palindromes(self):
        output = 3
        count_palindromes = PalindromeInInputString('asdfgh').calculate_palindromes()
        assert output != count_palindromes

    def test_quantity_of_palindromes_length_of_list(self):
        output = 3
        quantity = PalindromeInInputString('bbaxzzsdd').quantity_of_palindromes()
        assert output == len(quantity)

    def test_quantity_of_palindromes_if_no_palindromes(self):
        output = [0, ]
        quantity = PalindromeInInputString('asdfgh').quantity_of_palindromes()
        assert output == quantity
