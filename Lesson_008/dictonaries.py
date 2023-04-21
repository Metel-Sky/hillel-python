# словарь - это перечень пар ключ:значение. К словарю нельзя обращаться по индексу или слайсу.
# Можно обращаться только по ключам. По ключу значение получить можно, по значению - нельзя

eng_to_ru = {
    # ключ: значение
    "hello": "привет",
    # два ключа быть не может, сохраняется только последнее
    "hello": "здравствуйте",
    "bye": "пока",
    "code": "код",
    "program": "программа",
    "sun": "солнце"
}

print(eng_to_ru)
print(type(eng_to_ru))


print(eng_to_ru["hello"])

# print(eng_to_ru["привет"])

eng_to_ru["moon"] = "луна"
print(eng_to_ru)

eng_to_ru["opinion"] = "опинион"
print(eng_to_ru)
eng_to_ru["opinion"] = "мнение"
print(eng_to_ru)

del eng_to_ru["opinion"]
print(eng_to_ru)

value = eng_to_ru.pop("program")
print(eng_to_ru, value)

""" командой del можно убирать любую переменную
x = 5
del x
print(x)
"""

for key in ("moon", "program", "opinion", 'code'):
    if key in eng_to_ru:
        print(f'There is {key}:', eng_to_ru[key])
    else:
        print(f'There is no {key}')

my_dict = {
    0: 'zero',
    1: 'one',
    2: 'two',
    5.5: 'five and a half',
    'two': 2,
    'one': 1,
    'zero': 0,
    # ['asdasd', 'asdsad', 3]: 5,
    # {1, 2, 5, 5, 5}: 'a set',
    # {1: 2, 3: 4, '3': 5}: 'a dict',
    (1, 2, 3, 5, 'asd'): 'a tuple',
    'a list': [1, 2, 3, 4, 'as', 5],
    'a dict': {1: 2, 3: 4, '3': 5},
    'a tuple': (1, 2, 3, 5, 'asd'),
    'a set': {1, 2, 5, 5, 5}
}

print(my_dict)