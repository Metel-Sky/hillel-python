from typing import List, Dict

# Наследование
# Полиморфизм (Взаимозаменяемость)
# Инкапсуляция

# Агрегация или Композиция - один класс использует объект другого класса

# SOLID - принципы проектирования (для ООП и не только)
class Car:
    def __init__(self, model: str, total_km: int, fuel_tank_volume: int, fuel_consumption: float,
                 fuel: float, fuel_type: str):
        self.model = model
        self.__total_km = total_km
        self.__fuel_consumption = fuel_consumption
        self._fuel_tank_volume = fuel_tank_volume
        self.__fuel = fuel
        self._fuel_type = fuel_type

    @property
    def fuel_volume(self):
        return self.__fuel

    def fuel(self, fuel_volume: float = 9999999999) -> float:
        """
        Прибавляет в текущему объему топлива новый, однако не превышает размер бака
        :param fuel_volume: сколько топлива добавить. Значение по умолчанию расчитано на заправку до предела
                (гарантировано больше размера бака)
        :return: сколько топлива было фактически заправлено
        """
        fuel = self.__fuel + fuel_volume
        # не даём заправить больше объема бака
        if fuel > self._fuel_tank_volume:
            fuel = self._fuel_tank_volume
        # считаем сколько было заправлено
        fuel_difference = fuel - self.__fuel
        # фиксируем текущий объем топлива
        self.__fuel = fuel
        return fuel_difference

    def __str__(self):
        return f"Машина {self.model} с пробегом {self.__total_km}, расходом топлива {self.__fuel_consumption}л/100км," \
               f" сейчас в баке: {self.__fuel}/{self._fuel_tank_volume}л. Тип топлива: {self._fuel_type}"

    def drive(self, km: int):
        # 100km = fuel_consumption
        # km = ?
        fuel_needed_for_journey = km * self.__fuel_consumption / 100
        if self.__fuel > fuel_needed_for_journey:
            self.__fuel -= fuel_needed_for_journey
            self.__total_km += km
            print(f'Машина успешно проехалась')
            print(self)
        else:
            print(f'Необходимо {fuel_needed_for_journey}л топлива для поездки, в машине только {self.__fuel}л')


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


if __name__ == '__main__':
    c = Car('Lanos', total_km=150000, fuel_tank_volume=50, fuel_consumption=7, fuel=30, fuel_type="Газ")
    c.drive(100)
    c.drive(300)
    c.drive(50)

    okko = GasStation({'газ': 22, 'бензин 95': 49, 'дизель': 52})
    wog = GasStation({'газ': 21, 'бензин 95': 50, 'дизель': 52})

    wog.fuel_to_full(c)
    c.drive(50)