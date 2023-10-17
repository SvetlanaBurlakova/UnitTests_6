# Отчет о покрытиях тестами

Unit тестами покрываются различные варианты входных данных для каждого из модулей по
отдельности. Так же по отдельности проверяется выброс исключений, если данные не допустимые.
Комбинированные тесты проверяют. что оба модуля корректно работают вместе.

1. Unit тесты для list_average:
- *test_calculate_list_average* - параметризованный тест, проверяет расчет среднего значения для заданного списка, 
включает различные варианты входных листов
- *test_calculate_list_average_typeerror* - тест проверяет выброс ошибки, если на вход подается на список
- *test_calculate_list_average_typeerror_not_all_numbers_in_list* - тест для расчета среднего значения, проверяет, 
если в листе не все значения - числа
- *test_calculate_list_average_valueerror* - тест для расчета среднего значения, проверяет выброс ошибки 
если лист пустой

2. Unit тесты для list_compare:
- *test_find_which_number_bigger* - параметризованный тест, проверяет корректную работу сравнения двух чисел
- *test_find_which_number_bigger_typeerror* - тест, проверяет выброс ошибки при сравнение двух чисел, если, одно или все 
входные данные - не числа
- *test_find_which_number_bigger_valueerror* -  тест, проверяет выброс ошибки при сравнение двух чисел, если, одно или все 
входные данные - пустые

3. Комбинированные тесты:
- *test_integration_success* - првоеряет совместный запуск двух модулей, по расчеты среднего значения и по 
- сравнению среднего
- *test_integration_raise_value_error* - проверяет выброс ошибки Value error, если входные данные пустые
- *test_integration_raise_type_error* - проверяет выброс ошибки, если не все входные данные числа

### Отчет об успешном выполнении всех тестов
![All tests are passed](/Pictures/All_tests.png)

### Отчет о покрытии тестами
![Code coverage](/Pictures/Coverage.png)

### Отчет об анализе кода модуля list_average при помощи pyLint 
![Code coverage](/Pictures/list_average.png)

### Отчет об анализе кода модуля list_compare при помощи pyLint 
![Code coverage](/Pictures/list_compare.png)

### Отчет об анализе кода модуля с тестами при помощи pyLint 
![Code coverage](/Pictures/test_list_average.png)