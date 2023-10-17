"""Module for comparison"""
import numbers

class AverageCompare:
    """Class for comparison of two numbers"""

    @staticmethod
    def find_bigger_average(number1, number2):
        """Print message to terminal, which of two numbers are bigger."""
        if not number1 or not number2:
            raise ValueError("One  or both of the Average number/numbers is missing")
        if not isinstance(number1, numbers.Number) or not isinstance(number2, numbers.Number):
            raise TypeError("One or both values are not numbers")
        if number1 > number2:
            print("Первый список имеет большее среднее значение")
        elif number2 > number1:
            print("Второй список имеет большее среднее значение")
        else:
            print("Средние значения равны")
