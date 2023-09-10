# Задача 0
from datetime import datetime
from math import sqrt


def square_root(num: float) -> float:
    if num < 0:
        raise RuntimeError(f"Число {num} должно быть неотрицательным")
    # assert num>0, "Число должно быть больше 0"
    return sqrt(num)


def test_square_root_positive():
    assert square_root(25) == 5, "Тест с положительными числами провален"


def test_square_root_zero():
    assert square_root(0) == 0, "Тест с нулевыми значениями провален"


def test_square_root_negative():
    try:
        square_root(-5)
    except RuntimeError:
        print('Все тесты прошли')


# Задача 4
def happy_Ny():
    current_date= datetime.now()
    assert current_date > datetime (year=2024, month=1, day=1, hour=0, minute=0, second=0), '2024 ещё не наступил'
if __name__ == "__main__":
    happy_Ny()