class StringToListParser:

    def parse(self, number_string: str):
        if number_string == "":
            return []
        else:
            return [int(number_string)]
