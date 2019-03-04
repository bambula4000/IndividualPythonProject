from math import sqrt
from models.input import AskIntInput, AskInput
from models.valid import IsBiggerThanZero, IsSmallerThanMillion, CheckInputData


class CalculateSquareRoot:
    def __init__(self, length: int, square: int):
        self._length = length
        self._square = square

    def compute_square_root(self)-> int:
        return int(sqrt(self._square))

    def create_sequence(self)-> list:
        sequence = list()
        minimal_square_root = self.compute_square_root()
        for _ in range(self._length):
            minimal_square_root += 1
            sequence.append(minimal_square_root * minimal_square_root)
        return sequence


if __name__ == '__main__':
    while True:
        sequence_length = AskIntInput(AskInput('Please enter a sequence length between 1 to 999999: ')).value()
        digit_to_compute_square_root = AskIntInput(AskInput('Please enter a minimal square root: ')).value()

        if CheckInputData(
                IsBiggerThanZero(),
                IsSmallerThanMillion()
        ).passed(sequence_length) and CheckInputData(
                                        IsBiggerThanZero(),
                                      ).passed(digit_to_compute_square_root):
            sequence_of_square_roots = CalculateSquareRoot(sequence_length, digit_to_compute_square_root)
            print(sequence_of_square_roots.create_sequence())
            break
