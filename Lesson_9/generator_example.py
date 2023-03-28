# Генераторы - это функции где есть ключевое слово yield
# смешивать в одной функции return и yield - не рекомендуется

def my_generator(x: int):
    for i in range(x):
        yield i

g = my_generator(10)
print(g, type(g))
# print(len(g)) len на генераторе не вызывается
# print(g[0]) индексация на генератор так же не работает
for element in g:
    print(element)


# first_number
# multiplier
def geom_progression(first_number: float, multiplier: float, element_count: int):
    """
    Генератор членом геометрической прогрессии
    :param first_number: первый элемент прогрессии
    :param multiplier: множитель
    :param element_count: количество элементов, которые нужно сгенерировать
    :return: генерирует за раз 1 элемент прогрессии в возрастающем порядке
    """
    x = first_number
    for i in range(element_count):
        yield x
        # x = x * multiplier
        x *= multiplier


# Fibonacci numbers
# 0 1 1 2 3 5 8 13 21 34 55
j = 0
for number in geom_progression(3, 2, 30):
    print(f'{j + 1}. {number}')
    j += 1
