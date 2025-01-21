import unittest
from unittest import mock

from string_to_list_parser import StringToListParser
from addition_calculator import Additioncalculator

from main import add

class TestMain(unittest.TestCase):

    @mock.patch.object(StringToListParser, "parse", return_value=[1,2])
    @mock.patch.object(Additioncalculator, "add", return_value=3)
    def test_should_return_3_when_string_is_1_2_3(self, mock_add, mock_parse):
        number_str = "1,2,3"
        expected = 3

        actual = add(number_str)

        mock_parse.assert_called_once_with(number_str)
        mock_add.assert_called_once_with([1,2])

        self.assertEqual(expected, actual)
    
if __name__ == "__main__":
    unittest.main()
