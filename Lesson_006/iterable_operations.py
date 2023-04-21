x = [1, 3, 2.0, True, 'this is a string']

x.insert(3, 22)

print('Insert 22 at 3rd position:', x)

x.append(3)
x.append(3)
# remove медленная операция, лучше не пользоваться
while 3 in x:
    x.remove(3)
    print('Remove 3 from list:', x)

# гораздо быстрее remove, но требует индекс элемента
print(f'{x} before popping')
# pop полностью убирает элемент из списка по заданному индексу
# но есть возможность сохранить удалённый элемент в отдельную переменную
# никак не связанную со списком
y = x.pop(3)
print(f'Popped {y} at 3rd position from {x}')

# i = x.index(3) возвращает индекс найденного элемента. Выполнение index и pop один за другим - то же самое что remove
# index & remove - медленные, поп - моментальный

x.append(22)
x.append(22)
z = x.count(22)
print(f'In {x} there are {z} 22s')
for i in range(z):
    x.remove(22)
    print(f'Removed 22 from {x}')

# x.remove(22)  # удалять то чего нет нельзя - будет ошибка


text = """
The diesel engine, named after Rudolf Diesel, is an internal combustion
 engine in which ignition of the fuel is caused by the elevated temperature 
 of the air in the cylinder due to mechanical compression; thus, the diesel 
 engine is called a compression-ignition engine (CI engine). This contrasts 
 with engines using spark plug-ignition of the air-fuel mixture, such as a 
 petrol engine (gasoline engine) or a gas engine (using a gaseous fuel like 
 natural gas or liquefied petroleum gas)."""

text_words = text.split()

"""
# Вариант 1-а, видоизменение текущего списка через индексы
len_text_words = len(text_words)
for j in range(len_text_words):
    word = text_words.pop(j)
    word = word.strip('().,;:')
    text_words.insert(j, word)
    j += 1


# Вариант 1-б, видоизменение текущего списка через значения
i = 0
for w in text_words:
    text_words.pop(i)
    w = w.strip('().,;:')
    text_words.insert(i, w)
    i += 1
"""

# Вариант 2 создание нового "параллельного" списка
# вместо того чтобы редактировать старый список, мы создаём его видоизменённую копию
stripped_words = list()
for w in text_words:
    stripped_words.append(w.strip('(),.;:'))

lowered_words = list()
for w in text_words:
    lowered_words.append(w.strip('(),.;:').lower())

print(text_words)
print(stripped_words)


x = [1, 3, 2.0, -1, 5, 120, 19]
# x = [1, 3, 2.0, -1, 5, 120, 19, 's'] ашипка
# x = [1, 3, 2.0, -1, 5, 120, 19, True] не ашипка, но так можно вляпаться

print('=' * 10, 'Numbers (int & float)', '=' * 10)
print(f'Sum of elements of {x}: {sum(x)}')
print(f'Min of elements {x}: {min(x)}')
print(f'Max of elements {x}: {max(x)}')
print('=' * 5, 'Sorting', '=' * 5)
print(f'Sorted {x}: {sorted(x)}')
sorted_x = sorted(x)
print(f'Reverse sort {x}: {list(reversed(sorted_x))}')
print(f'Reverse sort {x}: {sorted(x, reverse=True)}')
print(f'Reverse of {x}: {list(reversed(x))}')

print('=' * 10, 'Strings', '=' * 10)
# sum(text_words) суммируем мы всё же числа, если нужно склеить строки - есть join
s = " ".join(text_words)
print(f'Join of elements of {text_words}:\n{s}')
print(f'Min of source text: {min(text_words)}')
print(f'Max of source text: {max(text_words)}')
print(f'Min of stripped text: {min(stripped_words)}')
print(f'Max of stripped text: {max(stripped_words)}')
print(f'Min of lowered text: {min(lowered_words)}')
print(f'Max of lowered text: {max(lowered_words)}')

# при поиска минимума/максимума в строках, идёт сортировка по алфавиту
# вначале символы препинания, затем - большие буквы (по алфавиту), затем - маленькие буквы (по алфавиту)

print('=' * 5, 'Sorting', '=' * 5)
print(f'Sorted source text: {sorted(text_words)}')
print(f'Sorted stripped text: {sorted(stripped_words)}')
print(f'Sorted lowered text: {sorted(lowered_words)}')
print(f'Reverse sort source text: {sorted(text_words, reverse=True)}')
print(f'Reverse sort stripped text: {sorted(stripped_words, reverse=True)}')
print(f'Reverse sort lowered text: {sorted(lowered_words, reverse=True)}')
print(f'Reverse of source text: {list(reversed(text_words))}')