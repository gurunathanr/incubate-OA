import unittest

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
 
if __name__ == "__main__":
    unittest.main()
