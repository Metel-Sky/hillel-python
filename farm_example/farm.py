from animals import Animal, Dog, Hen, Cow, Cat
from random import choices


if __name__ == '__main__':
    a = Animal('Чупакабра', {'???'}, -1)
    print(a, type(a))
    a.say()
    a.eat('печенька')
    a.treat()
    a.name = 'Не Чупакабра'
    a.age = 5
    print(a.hungry)
    a.eat('???')
    print(a.hungry)
    a.hungry = 10
    print(a)
    a.say()

    farm_animals = [
        Dog('Напас', {'мясо', 'сало', 'борщ'}, 14),
        Hen('Ряба', {"пшено", "крупа", "вода"}, 2),
        Cow('Бурёнка', {"трава", "сено"}, 5),
        Cat('Мурзилка', {"вискас", "мышка","вода"}, 7)
    ]

    # пример полиморфизма - одинаковые названия функций, но разные классы и разная логика выполнения.
    food_to_offer = ['мясо', 'сало', 'борщ', "пшено", "крупа", "вода", "трава", "сено","вискас", "мышка"]
    what_we_lost = list()
    what_we_get = list()
    for animal in farm_animals:
        print('\n', animal, type(animal))
        animal.say()
        for food in choices(food_to_offer, k=3):
            animal.eat(food)
            what_we_lost.append(food)
        what_we_get.append(animal.treat())

    farm_animals.append('Оса')
    farm_animals.append(5)
    farm_animals.append([3, 4, 'Шершень'])
    for animal in farm_animals:
        # if type(5) == int
        # if type(animal) == Dog
        # то же самое, что и выше, но рекомендуется сравнивать типы именно через isinstance
        if isinstance(animal, Animal):
            print(f'\nНайден представитель типа данных Animal: {animal}')
            if animal.hungry:
                print(f"На вашей ферме голодное животное! {animal}")
        else:
            print(f"{animal} не с нашей фермы.")
    print()
    print(f'Ухаживая за животными, мы потеряли: {what_we_lost}')
    print(f'Ухаживая за животными, мы получили: {what_we_get}')