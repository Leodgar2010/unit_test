from typing import Any


class Numbers:
    def __init__(self, lst1: [float], lst2: [float]):
        self.lst1 = lst1
        self.lst2 = lst2

    def get_lists_averages(self) -> tuple[float | int | Any, float | int | Any]:
        avg1_lst1 = 0
        if self.lst1:
            avg1_lst1 = sum(self.lst1) / len(self.lst1)

        avg2_lst2 = 0
        if self.lst2:
            avg2_lst2 = sum(self.lst2) / len(self.lst2)

        return avg1_lst1, avg2_lst2

    def compare_averages(self) -> None:
        avg1_lst1, avg2_lst2 = self.get_lists_averages()
        if avg1_lst1 > avg2_lst2:
            print('Первый список имеет большее среднее значение')
        elif avg1_lst1 < avg2_lst2:
            print('Второй список имеет большее среднее значение')
        else:
            print('Средние значения равны')
