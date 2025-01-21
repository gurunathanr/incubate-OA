class Additioncalculator:

    def add(self, array_of_integers: list):
        sum = 0
        for integer in array_of_integers:
            if integer < 1000:
                sum +=integer
        return sum

