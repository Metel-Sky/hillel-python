import random


def my_min(my_data: list):
    """
    Сравнить числа из my_data и найти наименьшее
    :param my_data: данные из которых выбрать минимум
    :return: самое маленькое число из my_data
    """
    current_min = data[0]
    # для каждого number из data[1:] выполни следующие действия:
    for number in data[1:]:
        if current_min > number:
            current_min = number
    return current_min


def my_max(my_data: list):
    """
    Сравнить числа из my_data и найти наибольшее
    :param my_data: данные из которых выбрать максимум
    :return: самое большое число из my_data
    """
    current_max = data[0]
    # для каждого number из data[1:] выполни следующие действия:
    for number in data[1:]:
        if current_max < number:
            current_max = number
        if number == -1:
            break
            print('I am after break!')
    print('Или цикл закончился или цикл нашел -1')
    return current_max


if __name__ == '__main__':
    data_len = random.randint(2, 15)
    data = [random.randint(1, 100) for i in range(data_len)]
    # data = set(data)
    # data = tuple(data)

    _max = max(data)

    print(f'Data: {data}')
    print(f'Function max: {_max}')

    # 1. Взять первых 2 яблока
    # 2. Сравнить какое из них больше
    # ПОВТОР
    # 3. Меньшее убрать, большее оставить
    # 4. Взять следующее яблоко
    # 5. Сравнить какое больше

    print(f'Custom max: {my_max(data)}')

    print(f'Function min: {min(data)}')
    print(f'Custom min: {my_min(data)}')