import unittest

from negative_integer_Exception import NegativeIntegerException
from string_to_list_parser import StringToListParser

class TestStringToListParser(unittest.TestCase):

    def test_should_return_empty_array_when_number_string_is_empty(self):
        number_str = ""
        expected = []

        actual = StringToListParser().parse(number_str)

        self.assertEqual(expected, actual)
    
    def test_should_return_array_with_1_when_number_string_is_1(self):
        number_str = "1"
        expected = [1]

        actual = StringToListParser().parse(number_str)

        self.assertEqual(expected, actual)

    def test_should_return_array_with_2_when_number_string_is_2(self):
        number_str = "2"
        expected = [2]

        actual = StringToListParser().parse(number_str)

        self.assertEqual(expected, actual)

    def test_should_return_array_with_1_2_when_number_string_is_1_2_on_comma_separated(self):
        number_str = "1,2"
        expected = [1,2]

        actual = StringToListParser().parse(number_str)

        self.assertEqual(expected, actual)

    def test_should_raise_negative_number_exception_when_number_string_has_negative_integer(self):
        number_str = "-1"

        with self.assertRaises(NegativeIntegerException):
             StringToListParser().parse(number_str)
 
    def test_should_return_array_with_1_2_3_when_number_string_is_1_2_3_with_comma_new_line_separators(self):
        number_str = "1\n2,3"
        expected = [1,2,3]

        actual = StringToListParser().parse(number_str)

        self.assertEqual(expected, actual)

    def test_should_return_comma_and_new_line_and_number_string_when_number_string_no_separator_in_format(self):
        number_str = "1,2,3"
        expected_delimiter = ",|\n"  
        expected_number_string = "1,2,3"  

        actual_delimiter, actual_number_string = StringToListParser().extract_demiliter_and_string(number_str)

        self.assertEqual(expected_delimiter, actual_delimiter)
        self.assertEqual(expected_number_string, actual_number_string)

    def test_should_return_semicolon_when_number_string_has_semicolon_as_separator_in_format(self):
        number_str = "//;\n1;2;3"
        expected_delimiter = ";"  
        expected_number_string = "1;2;3"    

        actual_delimiter, actual_number_string = StringToListParser().extract_demiliter_and_string(number_str)

        self.assertEqual(expected_delimiter, actual_delimiter)
        self.assertEqual(expected_number_string, actual_number_string)

    def test_should_return_array_with_1_2_3_when_number_string_is_1_2_3_with_its_own_separator_in_format(self):
        number_str = "//;\n1;2;3"
        expected = [1,2,3]

        actual = StringToListParser().parse(number_str)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
