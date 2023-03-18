
from input_number import get_user_float, get_user_int, MY_VAR
# from helper_functions import get_user_float, get_user_int

print(MY_VAR)

"""
while True:
    try:
        x = input('Введите число: ')
        x = float(x)
        break
    except Exception:
        print('Число!!!')
"""

# y = power_of(6, 2) функцию можно вызывать ПОСЛЕ её объявления, как с переменными
# def <имя функции>(<параметры функции через запятую>):
#   с отступа тело функции
def power_of(x: float, power: float):
    # return - вернуть, после него указать ЧТО функция возвращает. Функция завершает выполнение
    print('перед return')
    return x ** power, 'Hi Mark'
    # это не выполнится
    print('после return')

# def - define - определить

# имя + параметры/аргументы = сигнатура функции
def get_number_from_user(
        comment: str,
        arg2=2,
        arg3=3,
        arg4=4,
        arg5=5
):
    # внутри функции - локальная область видимости
    while True:
        try:
            z = input(comment)
            return float(z)
        except Exception:
            print('Число!!!')

# всё что снаружи функции - глобальная область видимости

# в функциях должны использоваться только три типа переменных
# 1. Параметры/аргументы функции
# 2. Переменные, которые объявляются внутри функции
# 3. Константы (КОНСТАНТЫ)
# Переменные извне функции которые не передаются как параметры использовать крайне не рекомендуется в теле функции


if __name__ == '__main__':
    y = power_of(6, 2)
    print(type(y))
    print(y[0])
    print(power_of(6, 2)[0])
    print(power_of(5, 2)[0])
    print(power_of(1, 0)[0])
    print(power_of(4, 3)[0])
    y = 5

    x = get_number_from_user('Введите число: ')
    print(f'Вы ввели: {x}')
    print(y)

    x = get_number_from_user('Введите другое число: ')
    print(f'Другое: {x}')

    print(get_user_float('Float: '))
    print(get_user_int('Int: '))