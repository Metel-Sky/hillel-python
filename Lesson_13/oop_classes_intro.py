from time import sleep
from random import randint, choices

# Класс - это тип данных
# Класс определяется:
# - полями (атрибуты, свойства, переменные класса)
# - методами (функции, поведение класса)


# class *имя класса*:
class Dog:
    # конструктор класса или метод инициализации
    # вызывается автоматически при создании объекта этого класса
    def __init__(
            self, name: str, gender: str, age: int,
            breed: str, play_hours: int, preferred_food: set
    ):
        """
        Рождение объекта класса/конструктор/инициализация
        :param name:
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.breed = breed
        self.play_hours = play_hours
        self.preferred_food = preferred_food
        self.hungry = False

    def __str__(self) -> str:
        return f'{self.breed.title()}, {self.age} лет по кличке {self.name}'

    def bark(self):
        print(f'{self.name} гавкает!')

    def play(self):
        if self.play_hours == 0:
            print(f'{self.name} не гуляет')
        else:
            print(f'{self.name} играет {self.play_hours} часов!')
            print('Ждём...')
            # sleep(self.play_hours)
            self.bark()
            print('Гавкает потому что довольна!')
        print(f'{self.name} проголодалась')
        self.hungry = True

    def eat(self, suggested_food: str):
        if suggested_food in self.preferred_food:
            print(f'{self.name} кушает {suggested_food}')
            self.hungry = False
        else:
            print(f'{self.name} предложили {suggested_food}, но мы такого не едим')


if __name__ == '__main__':
    bobik = Dog('Бобик', 'M', 4, 'дворняга', randint(2, 6), {'рыба', 'мясо'})
    rocky = Dog('Роки', 'M', 5, 'йоркский терьер', 0, {'корм', 'яблоки'})
    napas = Dog('Напас', 'M', 14, 'такса', 1, {'корм', 'сало', 'борщ'})
    jessy = Dog('Джесси', 'Ж', 9, 'канекорса', 4, {'мясо', 'каша'})

    potential_food = ['рыба', 'мясо', 'корм', 'яблоки', 'сало', 'борщ', 'каша']
    print(bobik, type(bobik))
    print(rocky, type(rocky))
    hungry_dogs = list()
    for dog in [bobik, rocky, napas, jessy]:
        print('=' * 20, f'\nОбычный день {dog}:')
        dog.bark()
        dog.play()
        # choices(list, k=3) k - сколько раз выбрать случайный элемент
        for food in choices(potential_food, k=2):
            dog.eat(food)
        if dog.hungry:
            hungry_dogs.append(dog)

    if hungry_dogs:
        print(f'Найдены {len(hungry_dogs)} голодная(ые) собака(и), срочно покормите их!')
        print('Вот их имена:', ', '.join([dog.name for dog in hungry_dogs]))
