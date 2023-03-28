x = list()
for element in range(1, 11):
    x.append(element)

print(x, type(x))

# то же, что и выше

# список
# [<конечный элемент (можно с преобразованием!)>
# for <название новой переменной>
# in <iterable откуда переменная берет значения>
# if <условие>]
x = [element for element in range(1, 11)]
print(x, type(x))

inventory = ['Laptops', 'Server', 'Powerbank', 'Monitor']
# словарь
d = {element: 0 for element in inventory}
print(d, type(d))

inventory = ['Laptops', 'Server', 'Powerbank', 'Monitor', 'Powerbank']
# сет
s = {element for element in inventory}
print(s, type(s))

x = list()
for element in range(1, 11):
    # проверка чётности
    if element % 2 == 0:
        x.append(element)
print(x, type(x))

x = [element for element in range(1, 11) if element % 2 == 0]
print(x, type(x))


inventory = ['Laptops', 'Server', 'Powerbank', 'Monitor', 'Powerbank']
# сет
s = {element for element in inventory if len(element) > 6}
print(s, type(s))

x = (element for element in range(50))
print(x, type(x))