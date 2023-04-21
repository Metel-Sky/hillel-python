d = {
    "Laptops": 5,
    "Keyboards": 2,
    "Server": 3,
    5: 3
}


# get позволяет взять значение по ключу из словаря не вызывая ошибки в случае отсутствия ключа
# когда желаемого ключа нет, возвращается второй аргумент - значение по умолчанию. Если его не указывать, будет None
print(d.get('Powerbank'))
value = d.get('Powerbank', 0)
# if value == None:
# if isinstance(value, type(None)):
print(value)

print(d.get('Laptops', 0))

print('\nИнвентаризация!')
for element in ['Laptops', 'Server', 'Powerbank', 'Monitor']:
    print(element, d.get(element, 0))

print('\nПроходимся for-ом по словарю:')
for element in d:
    print(element)

print('\nПроходимся for-ом по словарю.keys():')
for element in d.keys():
    print(element)

print('\nПроходимся for-ом по словарю.values():')
for element in d.values():
    print(element)

print('\nПроходимся for-ом по словарю.items():')
for element in d.items():
    key1 = element[0]
    value1 = element[1]
    key2, value2 = element
    print(element, type(element), ';', key1, value1, ';', key2, value2)

for key, value in d.items():
    print(key, value)


x = [1, 5, 6] + [2, 4, 12]
print(x)

z = {
    4: 2,
    8: 10,
    3: 0,
    5: 2
}
c = z.copy()
c.update(d)
# z.update(d)
print('z.copy().update(d):', c)
print('z:', z)
print('d:', d)

a = d.copy()
a.update(z)
print('d.copy().update(z):', a)