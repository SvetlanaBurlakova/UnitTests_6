"""Module average calculation"""

import numbers

class Average:
    """Class for average list calculation"""

    @staticmethod
    def calculate_list_average(lst):
        """Return average for the list."""
        if not isinstance(lst, list):
            raise TypeError("Input should be a list")
        if not all([isinstance(value, numbers.Number) for value in lst]):
            raise TypeError("All values in list have to be numbers")
        if not lst:
            raise ValueError("List should be not empty")
        return sum(lst) / len(lst)
