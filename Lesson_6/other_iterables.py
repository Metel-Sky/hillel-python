list_x = [1, 3, 2.0, -1, 5, 120, 19, 3]
tuple_x = (7, 5, 2, 3, 4, 5, 6)
set_x = {6, 5, 3, 4, 4, 4, 2}

print(type(list_x), list_x)
print(type(tuple_x), tuple_x)
print(type(set_x), set_x)

# SET (множество)  для уникальных значений, сразу сортирует, не умеет индексироваться, но очень быстрый поиск
# print(set_x[0]) с сетом так нельзя
for element in set_x:
    print(element, end=' ')
print()

print(f'Max of {set_x}: {max(set_x)}')
print(f'Min of {set_x}: {min(set_x)}')
if 100 in set_x:
    print(f'100 in {set_x}')
set_x.add(100)  # добавлять в сет
if 100 in set_x:
    print(f'100 in {set_x}')
set_x.remove(100)  # удалять из сета
if 100 in set_x:
    print(f'100 in {set_x}')

# можно преобразовать список в сет
new_set_x = set(list_x)
print(type(new_set_x), new_set_x)


# TUPLE (кортёж) - умеет всё, кроме редактирования. Константный список
print('=' * 10, 'TUPLES', '=' * 10)
tuple([2, 3, 4])  # конвертация в кортёж
print(tuple_x[2])
for element in tuple_x:
    print(element, end=' ')
print()
sorted_tuple = sorted(tuple_x)
print(f'Sorted {tuple_x}: {type(sorted_tuple)} {sorted_tuple}')