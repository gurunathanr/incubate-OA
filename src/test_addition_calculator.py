import unittest

from addition_calculator import Additioncalculator

class TestAdditioncalculator(unittest.TestCase):

    def test_should_return_0_when_array_is_empty(self):
        array_of_integers = []
        expected = 0

        actual = Additioncalculator().add(array_of_integers)

        self.assertEqual(expected, actual)

    def test_should_return_1_when_array_has_single_element_1(self):
        array_of_integers = [1]
        expected = 1

        actual = Additioncalculator().add(array_of_integers)

        self.assertEqual(expected, actual)

    def test_should_return_2_when_array_has_single_element_2(self):
        array_of_integers = [2]
        expected = 2

        actual = Additioncalculator().add(array_of_integers)

        self.assertEqual(expected, actual)

    def test_should_return_3_when_array_has_two_elements_1_2(self):
        array_of_integers = [1, 2]
        expected = 3

        actual = Additioncalculator().add(array_of_integers)

        self.assertEqual(expected, actual)

    def test_should_return_15_when_array_has_1_2_3_4_5(self):
        array_of_integers = [1, 2, 3, 4, 5]
        expected = 15

        actual = Additioncalculator().add(array_of_integers)

        self.assertEqual(expected, actual)

    def test_should_return_15_when_array_has_1_2_3_4_5_1001(self):
        array_of_integers = [1, 2, 3, 4, 5, 1001]
        expected = 15

        actual = Additioncalculator().add(array_of_integers)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
     unittest.main()