import pytest
from testobject import sum, mul, div, sub

# Тесты на проверку корректного выполнения функций с правильными аргументами и пограничными значениями.
@pytest.mark.parametrize("a, b, result", [
    (2, 3, 5),   # Обычное сложение положительных чисел
    (-1, 1, 0),  # Обычное сложение положительного и отрицательного числа
    (-2, -3, -5),  # Обычное сложение отрицательных чисел
    (2.5, 3.5, 6.0),  # Обычное сложение чисел с плавающей точкой
    (0, 0, 0),   # Сложение нулей
    (0.1, 0.2, 0.3),   # Обычное сложение положительных чисел: Expected :0.3 Actual :0.30000000000000004
    (1000000000, 1000000000, 2000000000),  # Обычное сложение больших чисел (граничное значение)
])
def test_sum(a, b, result):
    assert sum(a, b) == result

@pytest.mark.parametrize("a, b, result", [
    (2, 3, 6),   # Обычное умножение положительных чисел
    (-1, 5, -5),  # Обычное умножение положительного и отрицательного числа
    (0, 100, 0),  # Умножение на ноль
    (2.5, 4, 10.0),  # Обычное умножение чисел с плавающей точкой
    (15, 40, 600),  # Обычное умножение больших чисел
    (1, 1, 1),   # Обычное умножение чисел (граничное значение)
    (-1, -1, 1), # Обычное умножение отрицательных чисел (граничное значение)
])
def test_mul(a, b, result):
    assert mul(a, b) == result

@pytest.mark.parametrize("a, b, result", [
    (6, 2, 3),   # Обычное деление положительных чисел
    (-10, 2, -5),  # Обычное деление отрицательного числа на положительное
    (2, 5, 0.4),  # Обычное деление положительного числа на положительное с плавающей точкой
    (0, 3, 0),  # Деление нуля на положительное число
    (15, 40, 0.375),  # Обычное деление больших чисел
    (1, 1, 1),   # Деление единицы на себя (граничное значение)
])
def test_div(a, b, result):
    assert div(a, b) == result

@pytest.mark.parametrize("a, b, result", [
    (5, 3, 2),   # Обычное вычитание положительных чисел
    (-1, -1, 0),  # Обычное вычитание отрицательных чисел
    (0, 0, 0),  # Вычитание нулей
    (5.5, 2.5, 3.0),  # Обычное вычитание чисел с плавающей точкой
    (12, 25, -13),  # Обычное вычитание больших чисел
    (1, 1, 0),   # Обычное вычитание чисел (граничное значение)
    (-999999, 999999, -1999998), # Обычное вычитание отрицательных (граничное значение)
])
def test_sub(a, b, result):
    assert sub(a, b) == result


# Тесты на обработку ошибок (деление на ноль)
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


# Параметризованные тесты для проверки комбинаций аргументов/ожидаемых ошибок TypeError
@pytest.mark.parametrize("func, a, b", [
    (sum, 100, '2'),
    (mul, 1, '400'),  #  Failed: DID NOT RAISE <class 'TypeError'> Actual: '400'
    (div, 45, '21'),
    (sub, 0.2, '101')
])
def test_Error(func, a, b):
    with pytest.raises(TypeError):
        func(a, b)