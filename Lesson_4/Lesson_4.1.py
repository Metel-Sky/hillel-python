# bool - булевая переменная, 1 или 0
x = True
print(x, type(x))
x = False
print(x, type(x))

# условное выражение (conditional expression)
x = 8 > 5
print(x, type(x))

print(11 < 9)

# условные операторы (conditional operator)
if 8 > 5:
    # если условие верное (True "трушное"), выполнится этот код. Если False, этот код никогда не выполнится
    print('8 is greater than 5!')
else:
    # выполняется если условие выше False (неверное)
    print('8 is not greater than 5!')

# if - если, после него следует условное выражение и двоеточие. Далее С ОТСТУПОМ (1 таб или 4 пробела) - тело правдивого исхода
# else - иначе, обязано быть после тела if (или elif). В нём содержится тело неправдивого исхода

# > - больше
# >= - больше или равно
# < - меньше
# <= - меньше или равно

# == - равно
# != - неравно
# not нет

# если мы в if ложим не условие, а любую другую переменную любого типа
# то происходит проверка на не ноль или не пустоту
if '':
    print('5?')
else:
    print('not 5')

# '' - пустая строка
# 0 - "пустое" число
# 0.0 - "пустое" число

# None - ПОЛНАЯ пустота))


x = 150
# > 0 < 100
# and or

# and требует True выполнение ОБОИХ соединямых условий
if x > 0 and x < 100:
    print('x is greater than 0 AND lesser than 100')

# "синтаксический сахар" упрощает жизнь, красивее выглядит, смысл такой же как и у выражения выше
if 0 < x < 100:
    print('x is greater than 0 AND lesser than 100')

y = 10000

# or требует ХОТЯ бы одно из условий верным
if x < 100 or y > 1000:
    print('x is lesser than 100 OR y is greater than 1000')

# сложная группировка
if x > 0 and (x < 100 or x > 200):
    print('x is greater than 0 AND lesser than 100')

# кроме двух условий можно ввести третье, четвертое и сколько угодно других с помощью elif
x = 5
if x < 10:
    print('x is less than 10')
elif x < 20:
    print('x is less than 20, but greater 10')
else:
    print('x is greater than 20')

print()