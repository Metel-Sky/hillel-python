


# квадратные скобочки и значения через запятую - это список
x = [1, 2, 3, 4]
print(x)
print(type(x))

y = 4
x = [1, 2, 3, y]
print(x)
print(type(x), type(y))

x = [1, 2.0, True, 'this is a string']
print(x)
print(type(x))

# добавить в конец списка новый элемент
x.append('this is list in Python')
print(x)

# примеры объявления пустого списка
_y = []
y = list()

y.append('first element')
y.append('second element')
y.append('last element')
# y.append(input('What do you want to add?'))
print(y)

print(x + y)
# x + y != y + x
print(y + x)

# sim_card1_contact_list.extend(sim_card2_contact_list)
# x = x + y  # идентично x.extend(y)
x.extend(y)
print(x)

x.append(y)
print(x)
y.append(5)
print(y)
print(x)