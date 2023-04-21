from car import Car
from typing import Dict


class GasStation:
    def __init__(self, fuel_prices: Dict[str, float]):
        # GasStation агрегирует в себя тип данных dict
        self.fuel_prices = fuel_prices

    # метод класса GasStation принимает объект другого класса (Car)
    # может быть объект своего класса

    # сигнатура метода/функции (даже если не в классе):
    # имя функции/метода; перечень входных параметров (и их типов); тип возвращаемого значения
    def fuel_to_full(self, car: Car):
        """
        Заправляем до тех пор, пока в топливном баке автомобиля есть место
        :param car:
        :return:
        """
        fuel_type = car._fuel_type.lower()
        if fuel_type in self.fuel_prices:
            # узнаём сколько быо заправлено
            fuel_volume = car.fuel()
            price = self.fuel_prices[fuel_type] * fuel_volume
            print(f'Заправлено {fuel_type}: {fuel_volume}л, цена: {price:.2f} UAH')
            print(car)