from unittest import TestCase
from number_to_text import NumberToText


class TestNumberToText(TestCase):
    def test_one_to_99_same_output_and_converted_number(self):
        output = " девяносто девять"
        converted_number = NumberToText(99).one_to_99(99)
        assert output == converted_number

    def test_one_to_99_different_output_and_converted_number(self):
        output = " девяносто пять"
        converted_number = NumberToText(99).one_to_99(99)
        assert output != converted_number

    def test_one_to_99_same_digits_but_converted_number_is_negative(self):
        output = " девяносто девять"
        converted_number = NumberToText(-99).one_to_99(-99)
        assert output != converted_number

    def test_one_to_99_empty_string_output(self):
        output = " "
        converted_number = NumberToText(99).one_to_99(99)
        assert output != converted_number

    def test_one_to_99_integer_output_instead_string(self):
        output = 99
        converted_number = NumberToText(99).one_to_99(99)
        assert output != converted_number

    def test_hundred_to_999_same_output_and_converted_number(self):
        output = " восемьсот восемьдесят восемь"
        converted_number = NumberToText(888).hundred_to_999(888)
        assert output == converted_number

    def test_hundred_to_999_different_output_and_converted_number(self):
        output = " восемьсот восемьдесят восемь"
        converted_number = NumberToText(899).hundred_to_999(899)
        assert output != converted_number

    def test_hundred_to_999_same_digits_but_converted_number_is_negative(self):
        output = " восемьсот восемьдесят восемь"
        converted_number = NumberToText(-888).hundred_to_999(-888)
        assert output != converted_number

    def test_hundred_to_999_empty_string_output(self):
        output = " "
        converted_number = NumberToText(888).hundred_to_999(888)
        assert output != converted_number

    def test_hundred_to_999_integer_output_instead_string(self):
        output = 888
        converted_number = NumberToText(888).hundred_to_999(888)
        assert output != converted_number

    def test_thousand_to_999_same_output_and_converted_number(self):
        output = " семьсот семьдесят семь тысяч семьсот семьдесят семь"
        converted_number = NumberToText(777777).thousand_to_999(777777)
        assert output == converted_number

    def test_thousand_to_999_different_output_and_converted_number(self):
        output = " семьсот семьдесят семь тысяч семьсот семьдесят семь"
        converted_number = NumberToText(123456).thousand_to_999(123456)
        assert output != converted_number

    def test_thousand_to_999_same_digits_but_converted_number_is_negative(self):
        output = " семьсот семьдесят семь тысяч семьсот семьдесят семь"
        converted_number = NumberToText(-777777).hundred_to_999(-777777)
        assert output != converted_number

    def test_thousand_to_999_empty_string_output(self):
        output = " "
        converted_number = NumberToText(777777).thousand_to_999(777777)
        assert output != converted_number

    def test_thousand_to_999_integer_output_instead_string(self):
        output = 777777
        converted_number = NumberToText(888).thousand_to_999(777777)
        assert output != converted_number

    def test_number_range_same_positive_digits(self):
        output = " девяносто девять"
        converted_number = NumberToText(99).number_range()
        assert output == converted_number

    def test_number_range_same_digits_but_converted_number_is_negative(self):
        output = " девяносто девять"
        converted_number = NumberToText(-99).number_range()
        assert output != converted_number

    def test_number_range_different_output_and_converted_number(self):
        output = " девяносто девять"
        converted_number = NumberToText(999).number_range()
        assert output != converted_number

    def test_number_range_integer_output_instead_string(self):
        output = 99
        converted_number = NumberToText(99).number_range()
        assert output != converted_number

    def test_number_range_empty_string_output(self):
        output = " "
        converted_number = NumberToText(99).number_range()
        assert output != converted_number
