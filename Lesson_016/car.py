from car_technician import CarTechnician


class Car:
    def __init__(self, model: str, total_km: int, fuel_tank_volume: int, fuel_consumption: float,
                 fuel: float, fuel_type: str):
        self.model = model
        self.__total_km = total_km
        self.__fuel_consumption = fuel_consumption
        self._fuel_tank_volume = fuel_tank_volume
        self.__fuel = fuel
        self._fuel_type = fuel_type

        self.car_technicians = list()

    def add_technician(self, car_technician: CarTechnician):
        self.car_technicians.append(car_technician)

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