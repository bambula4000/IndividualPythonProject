from typing import Any
from models.input import AskInput
from models.valid import CheckInputData, IsLongerThanOneSymbol


class PalindromeInInputString:
    def __init__(self, row: Any):
        self.row = row

    def calculate_palindromes(self) -> list:
        palindromes = []
        for finish_char in range(len(self.row)):
            for start_char in range(finish_char):
                palindrome = self.row[start_char:finish_char + 1]
                if palindrome == palindrome[::-1]:
                    palindromes.append(palindrome)
        return palindromes

    def quantity_of_palindromes(self) -> list:
        palindromes = self.calculate_palindromes()
        if len(palindromes) > 0:
            return palindromes
        palindromes.append(0)
        return palindromes


if __name__ == '__main__':
    while True:
        string_for_checking = AskInput("Please enter a string to check a palindromes: ").value()
        if CheckInputData(IsLongerThanOneSymbol()).passed(string_for_checking):
            sequence_of_palindromes = PalindromeInInputString(string_for_checking).quantity_of_palindromes()
            print(set(sequence_of_palindromes))
            break
