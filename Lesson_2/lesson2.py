import math
import time


a = int()  # инт - это целые числа
b = float()  # float - десятичные числа, "плавающая запятая"

print(a, b)

a = 2
b = 2.5
print(a,  b)
print(type(a), type(b))

a = 2 + 5
print(a)
a = 3 - 1
print(a)
a = 38 * 2
print(a)
a = 38 / 2
print(a, type(a))  # деление всегда производит флоат
a = int(38 / 2)
print(a, type(a))  # инт() преобразовывает в инт тип
a = 10 / 3
print(round(a, 2))
a = 10 / 3
print(int(a))
print(int(1.75))  # int обрезает десятичную часть
print(round(1.75))  # round - округляет
print(round(1.75, 2))  # можно округлять не до конца
print(math.ceil(8.3))  # ceil всегда округляет вверх (потолок)

print(float(int(1.75)))  # float() тоже преобразовывает, но не возвращает ранее отрезанные данные


b = 5 ** 2
print(b)
b = pow(3, 4)
print(b)
b = pow(25, 1 / 2)
print(b)
print(math.sqrt(36))  # квадратный корень

b = 25 ** (1 / 2)  # есть приоритет операций
print(b)

x = 25 * 3 - 2 / 4 - 2
print(x)

unlucky_ticket = 938984
print(f'Calculating if ticket {unlucky_ticket} is lucky!')
left_side = unlucky_ticket // 1000  # деление нацело
right_side = unlucky_ticket % 1000  # остаток от деления
# 938 = 9 + 3 + 8
x = left_side % 10
y = left_side // 10 % 10
z = left_side // 100
print(f'Ticket left side {left_side} sum equals to {x + y + z}')


x = right_side % 10
y = right_side // 10 % 10
z = right_side // 100
print(f'Ticket right side {right_side} sum equals to {x + y + z}')

print('Ticket is unlucky!')

lucky_ticket = 123501
print(f'Calculating if ticket {lucky_ticket} is lucky!')
print(divmod(lucky_ticket, 1000))  # деление нацело И остаток от деления
left_side, right_side = divmod(lucky_ticket, 1000)
x = left_side % 10
y = left_side // 10 % 10
z = left_side // 100
print('Ticket left side ' + str(left_side) + f' sum equals to {x + y + z}')

x = right_side % 10
y = right_side // 10 % 10
z = right_side // 100
print(f'Ticket right side {right_side} sum equals to {x + y + z}')

print('Ticket is lucky!')

print(divmod(10, 3))

print(type(z))
print(f'Is Z integer? {isinstance(z, int)}')
print(f'Is Z float?', isinstance(z, float))

print('Этого нет')

x = 100 / 6
print(f'{x:.3f}')  # 2 символа после запятой, вместо round()


# на потом
x = input('Number >')
print(type(x))
x = float(x)
print(type(x))

