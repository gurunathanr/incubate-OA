from string_to_list_parser import StringToListParser
from addition_calculator import Additioncalculator

def add(numbers: str) -> int:
    list_of_integers = StringToListParser().parse(numbers)

    return Additioncalculator.add(list_of_integers)

if __name__ == "__main__":
    add("1,0")