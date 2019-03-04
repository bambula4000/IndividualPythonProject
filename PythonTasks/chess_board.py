from models.input import AskInput, AskIntInput
from models.valid import CheckInputData, IsBiggerThanZero


class ChessBoard:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def make_chess_board(self) -> list:
        complete_board = []
        for digit in range(self._height):
            board_row = []
            if digit % 2 == 0:
                for num in range(self._width):
                    if num % 2 == 0:
                        board_row.append('☻')
                    else:
                        board_row.append('☺')

            if digit % 2 != 0:
                for num in range(self._width):
                    if num % 2 == 0:
                        board_row.append('☺')
                    else:
                        board_row.append('☻')
            complete_board.append(board_row)
        return complete_board


if __name__ == "__main__":
    while True:
        chess_board_width = AskIntInput(AskInput('Please enter chess board width(greater than 0): ')).value()
        chess_board_height = AskIntInput(AskInput('Please enter chess board height(greater than 0): ')).value()

        if CheckInputData(
                IsBiggerThanZero()
        ).passed(chess_board_width) and CheckInputData(
                                            IsBiggerThanZero()
                                        ).passed(chess_board_height):
            completed_chess_board = ChessBoard(chess_board_width, chess_board_height).make_chess_board()

            for board_rows in completed_chess_board:
                print(*board_rows, sep='')
            break
