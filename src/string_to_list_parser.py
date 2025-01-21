from negative_integer_Exception import NegativeIntegerException


class StringToListParser:

    DELIMITER = ","

    def parse(self, number_string: str):
        if number_string == "":
            return []
        else:
            list_of_positive_integers = []
            list_of_int_char = number_string.split(StringToListParser.DELIMITER)
            for numeric_string in list_of_int_char:
                integer = int(numeric_string)
                if integer < 0:
                    raise NegativeIntegerException()
                else:
                    list_of_positive_integers.append(integer)
            return list_of_positive_integers