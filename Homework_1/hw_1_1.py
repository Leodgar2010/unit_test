# В классе Calculator создайте метод calculateDiscount,
# который принимает сумму покупки и процент скидки и возвращает сумму
# с учетом скидки. Ваша задача - проверить этот метод с использованием
# библиотеки AssertJ. Если метод calculateDiscount получает недопустимые аргументы,
# он должен выбрасывать исключение ArithmeticException. Не забудьте написать тесты
# для проверки этого поведения.

class Calculator:
    def __init__(self, first_number: float, second_number: float) -> float:
        self.first_number = first_number
        self.second_number = second_number



    def calculate_discount (self,percent:int) -> float:
        a= self.first_number+self.second_number
        b= ((self.first_number+self.second_number) * percent)/100
        return a-b


def test_calculate_discount_negative_argument ():
    calc = Calculator(1, 2)
    percent = (5)
    assert calc.calculate_discount(percent) < 3, "Тест на положительный процент скидки провален"


def test_calculate_discount_negative_number_assert():
    calc = Calculator(1, 2)
    percent = (-5)
    assert (calc.first_number+calc.second_number)==(abs(calc.first_number)+abs(calc.second_number)), \
            "Тест на положительные аргументы провален"
    assert calc.calculate_discount(percent) < (abs(calc.first_number)+abs(calc.second_number)),\
            "Тест на положительный процент скидки провален"


if __name__ == "__main__":
    test_calculate_discount_negative_number_assert()