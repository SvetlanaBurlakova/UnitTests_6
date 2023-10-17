"""Module for all tests"""
import pytest

from list_average import Average
from list_compare import AverageCompare


class TestListAverage:
    """Class for tests"""

    @pytest.mark.parametrize("lst, expected", [
        ([10, 2, 0], 4),        # Расчет среднего значения, если числа в списке разные положительные
        ([1, 1, 1, 1, 1], 1),   # Расчет среднего значение, если числа в списке одинаковые
        ([-8, -2, -5, -5], -5), # Расчет среднего значения, если числа в списке отрицательные
        ([-1, -1, -1], -1),     # Расчет среднего значение, если числа в списке одинаковые отр-ные
        ([0.2, 1.4, 1.1], 0.9),  # Расчет среднего значения, если числа в списке с плавающей точкой
        ([-0.2, -1.4, -1.1], -0.9),  # Расчет среднего значения, если числа в списке
                                    # с плавающей точкой отрицательные
        ([0, 0, 0], 0),  # Расчет среднего значение, если числа в списке одинаковые нулевые
        ([4], 4)  # Расчет среднего значение, если список содержит одно число
    ])
    def test_calculate_list_average(self, lst, expected):
        """Parametrized unit test for calculation average for the list"""
        assert Average.calculate_list_average(lst) == expected

    def test_calculate_list_average_typeerror(self):
        """Unit Test for raising type error when in input not a list"""
        with pytest.raises(TypeError):
            Average.calculate_list_average("Not a list")

    def test_calculate_list_average_typeerror_not_all_numbers_in_list(self):
        """Unit Test for raising type error when in list not all values are number"""
        with pytest.raises(TypeError):
            Average.calculate_list_average([1,2,3,'4'])

    def test_calculate_list_average_valueerror(self):
        """Unit Test for raising value error when in input empty list"""
        with pytest.raises(ValueError):
            Average.calculate_list_average([])

    @pytest.mark.parametrize("number1, number2, expected", [
        (4, 2, "Первый список имеет большее среднее значение\n"),
                # Сравнение значений, если первое больше второго
        (2, 4, "Второй список имеет большее среднее значение\n"),
                # Сравнение значений, если второе больше
        (2, 2, "Средние значения равны\n")
                # Сравнение значений, если два значения равны
         ])
    def test_find_which_number_bigger(self, capsys, number1, number2, expected):
        """Parametrized Unit Test for checking correct output in terminal"""
        AverageCompare.find_bigger_average(number1, number2)
        captured = capsys.readouterr()
        assert captured.out == expected

    def test_find_which_number_bigger_typeerror(self):
        """Unit Test for raising TypeError in comparing average if one value is not number"""
        with pytest.raises(TypeError):
            AverageCompare.find_bigger_average('Not number', 10)
        with pytest.raises(TypeError):
            AverageCompare.find_bigger_average(10, 'Not number')
        with pytest.raises(TypeError):
            AverageCompare.find_bigger_average('Not number', 'Not number')

    def test_find_which_number_bigger_valueerror(self):
        """Unit Test for raising ValueError in comparing average if one of the value is None"""
        with pytest.raises(ValueError):
            AverageCompare.find_bigger_average(None, 10)
        with pytest.raises(ValueError):
            AverageCompare.find_bigger_average(10, None)
        with pytest.raises(ValueError):
            AverageCompare.find_bigger_average(None, None)

    def test_integration_success(self, capsys):
        """Integration Test for success calculation average for two lists and
        comparison of these averege numbers"""
        average1 = Average.calculate_list_average([1, 2, 3, 4, 5])
        average2 = Average.calculate_list_average([2, 3, 4, 5, 6])
        AverageCompare.find_bigger_average(average1, average2)
        captured = capsys.readouterr()
        assert captured.out == "Второй список имеет большее среднее значение\n"

    def test_integration_raise_value_error(self):
        """Integration Test for raising value error"""
        with pytest.raises(ValueError):
            AverageCompare.find_bigger_average(Average.calculate_list_average([]),
                                                Average.calculate_list_average([2, 3, 4, 5, 6]))

    def test_integration_raise_type_error(self):
        """Integration Test for raising TypeError"""
        with pytest.raises(TypeError):
            AverageCompare.find_bigger_average(Average.calculate_list_average('Not number'),
                                                Average.calculate_list_average([2, 3, 4, 5, 6]))
