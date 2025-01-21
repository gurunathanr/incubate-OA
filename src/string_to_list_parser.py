class StringToListParser:

    DELIMITER = ","

    def parse(self, number_string: str):
        if number_string == "":
            return []
        else:
            
            return [int(numeric_string) for numeric_string in number_string.split(StringToListParser.DELIMITER)]
