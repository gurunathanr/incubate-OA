import unittest

from string_to_list_parser import StringToListParser

class TestStringToListParser(unittest.TestCase):

    def test_should_return_empty_array_when_number_string_is_empty(self):
        number_str = ""
        expected = []

        actual = StringToListParser().parse(number_str)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
