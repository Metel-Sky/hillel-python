from car import Car
from car_technician import CarTechnician
from gas_station import GasStation


if __name__ == '__main__':
    c = Car('Lanos', total_km=150000, fuel_tank_volume=50, fuel_consumption=7, fuel=30, fuel_type="Газ")
    c.drive(50)
    c.drive(300)
    c.drive(50)

    okko = GasStation({'газ': 22, 'бензин 95': 49, 'дизель': 52})
    wog = GasStation({'газ': 21, 'бензин 95': 50, 'дизель': 52})

    wog.fuel_to_full(c)
    c.drive(50)

    general = CarTechnician('Андрей', '+(380) 321 4321', 'Київ, вул. Героїв Дніпра 50', 'загальне')
    c.add_technician(CarTechnician('Сергей', '+(380)-123-1234', 'Київ, вул. Голосіївська 50', 'електрик'))
    c.add_technician(general)
    print(c.car_technicians)
    print(c.car_technicians[0])

    c.car_technicians[1].maintenance(c)
    c.car_technicians[0].diagnose(c)

    b = Car('Toyota Camry', total_km=10000, fuel_type='petrol', fuel_consumption=7, fuel_tank_volume=50, fuel=20)
    b.add_technician(general)

    b.add_technician(CarTechnician('Андрей', '+(380) 321 4321', 'Київ, вул. Героїв Дніпра 50', 'загальне'))
    b.car_technicians[0].repair(b)

    print(repr(b.car_technicians[1]))
    print(repr(c.car_technicians[1]))




    # CarTechnician('Александр', '+(380)-321=5678', 'Київ, вул. Героїв Дніпра 50', 'рихтовка')