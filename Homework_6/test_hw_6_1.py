# Данный тестовый модуль  решает две задачи
# 1. Проверяет корректность расчета среднего значения заданных списков.
# 2. Проверяет корректность вывода данных о сравнении списков.

import pytest

from hw_6_1 import Numbers


@pytest.fixture
def list1():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def list2():
    return [2, 3, 4, 5, 6]

def test_get_lists_averages(list1, list2):
    nums_list = Numbers(list1, list2)
    assert nums_list.get_lists_averages() == (3, 4)


def test_first_average_more(list1, list2, capfd):
    nums_list = Numbers(list2, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Первый список имеет большее среднее значение'

def test_second_average_more(list1, list2, capfd):
    nums_list = Numbers(list1, list2)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Второй список имеет большее среднее значение'

def test_equal_averages(list1, capfd):
    """Проверка сообщения когда средние значения списков равны"""
    nums_list = Numbers(list1, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Средние значения равны'
