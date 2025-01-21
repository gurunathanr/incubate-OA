from negative_integer_Exception import NegativeIntegerException
import re

class StringToListParser:

    COMMA_DELIMITER = ","
    NEW_LINE_DELIMITER = "\n"

    def parse(self, number_string: str):
        if number_string == "":
            return []
        else:
            list_of_positive_integers = []
            delimiter, number_string = self.extract_demiliter_and_string(number_string)
            list_of_int_char = re.split(delimiter, number_string)
            for numeric_string in list_of_int_char:
                integer = int(numeric_string)
                if integer < 0:
                    raise NegativeIntegerException()
                else:
                    list_of_positive_integers.append(integer)
            return list_of_positive_integers
        
    def extract_demiliter_and_string(self, string: str):
        if string.startswith("//"):
            delimiter_str, numbers_string = string.split('\n', 2)
            delimiter_str = delimiter_str.replace('//', '')
            return delimiter_str, numbers_string
        else:
            return f"{StringToListParser.COMMA_DELIMITER}|{StringToListParser.NEW_LINE_DELIMITER}", string
