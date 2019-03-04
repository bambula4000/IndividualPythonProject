from models.input import AskInput, AskIntInput
from models.valid import CheckInputData, IsBiggerThanZero, IsSmallerThanMillion


class NumberToText:
    units = {
        1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
    }
    ten_to_nineteen = {
        10: 'десять', 11: 'одинадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
        16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать',
    }
    tens = {
        2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят',
        8: 'восемьдесят', 9: 'девяносто'
    }
    hundreds = {
        1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот',
        8: 'восемьсот', 9: 'девятьсот',
    }
    thousand_word_ends = {
        1: "ча", 2: "чи", 3: "чи", 4: "чи", 5: "ч", 6: "ч", 7: "ч", 8: "ч", 9: "ч", 0: "ч"
    }

    def __init__(self, number: int):
        self._number = number
        self._converted_number = ''

    def one_to_99(self, number: int) -> str:
        if 0 < number < 10:
            self._converted_number += ' ' + (self.units[number])
        elif 9 < number < 20:
            self._converted_number += ' ' + (self.ten_to_nineteen[number])
        elif 19 < number < 100:
            self._converted_number += ' ' + (self.tens[number // 10])
            if number % 10 != 0:
                self._converted_number += ' ' + (self.units[number % 10])
        return self._converted_number

    def hundred_to_999(self, number: int) -> str:
        self._converted_number = ''
        if 99 < number < 1000:
            self._converted_number = " " + (self.hundreds[number // 100]) + (self.one_to_99(number % 100))
        return self._converted_number

    def thousand_to_999(self, number: int) -> str:
        thousand_count = number // 1000
        if 10 <= thousand_count % 100 <= 19:
            word_ending = self.one_to_99(thousand_count) + self.hundred_to_999(thousand_count) + " тысяч"
        else:
            index = int((str(thousand_count))[-1])
            word_ending = self.one_to_99(thousand_count) + self.hundred_to_999(thousand_count) + " тыся" \
                + self.thousand_word_ends[index]
        word_ending = word_ending.replace("один ", "одна ")
        word_ending = word_ending.replace("два ", "две ")
        if number % 1000 < 100:
            self._converted_number = word_ending + self.hundred_to_999(number % 1000) + self.one_to_99(number % 1000)
        else:
            self._converted_number = word_ending + self.hundred_to_999(number % 1000)
        return self._converted_number

    def number_range(self) -> str:
        if 0 < self._number < 100:
            self._converted_number += (self.one_to_99(self._number))
        elif 99 < self._number < 1000:
            self._converted_number += (self.hundred_to_999(self._number))
        elif 999 < self._number < 1000000:
            self._converted_number = (self.thousand_to_999(self._number))
        return self._converted_number


if __name__ == "__main__":
    while True:
        entered_number = AskIntInput(AskInput('Please enter a number(greater than 0): ')).value()
        if CheckInputData(
                IsBiggerThanZero(),
                IsSmallerThanMillion(),
        ).passed(entered_number):
            converted_number_to_text = NumberToText(entered_number)
            print(converted_number_to_text.number_range())
            break
