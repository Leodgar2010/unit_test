import unittest


class Vehicle():
    def __init__(self, company: str, model: str, year_release: int, num_wheels: int, speed: int):
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = num_wheels
        self.speed = speed

    def test_drive(self):
        pass

    def park(self):
        pass

    def __repr__(self):
        return f"Vehicle: {self.company}, {self.model}, {self.year_release}, {self.speed},{self.num_wheels}"


class Car(Vehicle):
    def __init__(self, company, model, year_release, num_wheels=4, speed=0):
        super().__init__(company, model, year_release, num_wheels, speed)

    def test_drive(self):
        self.speed = 60

    def park(self):
        self.speed = 0


class Motorcycle(Vehicle):
    def __init__(self, company, model, year_release, num_wheels=2, speed=0):
        super().__init__(company, model, year_release, num_wheels, speed)

    def test_drive(self):
        self.speed = 75

    def park(self):
        self.speed = 0


# 1.  Проверить, что экземпляр объекта Car также является экземпляром
# транспортного средства (используя оператор instanceof).
class Test_Vehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("Lada", '2105', 1979)
        self.motorcycle = Motorcycle("Ява", '638', 1984)

    # 1.  Проверить, что экземпляр объекта Car также является экземпляром
    # транспортного средства (используя оператор instanceof).
    def test_is_Vehicle(self):
        self.assertIsInstance(self.car, Vehicle)
    # 2. Проверить, что объект Car создается с 4-мя колесами.
    def test_car_is_4_wheels(self):
        self.assertEqual(self.car.num_wheels, 4)

    # 3. Проверить, что объект Motorcycle создается с 2-мя колесами.
    def test_motorcycle_is_2_wheels(self):
        self.assertEqual(self.motorcycle.num_wheels, 2)

    # 4. Проверить, что объект Car развивает скорость 60 в
    # режиме тестового вождения (используя метод testDrive()).
    def test_car_test_drive(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

    # 5. Проверить, что в режиме парковки (сначала testDrive, потом
    # park, т.е. эмуляция движения транспорта) машина останавливается (speed = 0).
    def test_car_test_drive_and_park(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)
        self.car.park()
        self.assertEqual(self.car.speed, 0)

    # 6. Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция
    # движения транспорта) мотоцикл останавливается (speed = 0).
    def test_motorcycle_test_drive_and_park(self):
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75)
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == '__main__':
    test = Test_Vehicle()
