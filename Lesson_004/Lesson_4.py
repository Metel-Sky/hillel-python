name = input('Как тебя зовут? ')
while not len(name) >= 2:
    print('Вы ввели пустое имя!')
    name = input('Как тебя зовут? ')
age = int(input('Сколько тебе полных лет? '))
sex = input('Укажите ваш пол: (М/Ж) ')

# меньше 6 (включительно) - ребёнок
# от 6 до 18 - школьник
# от 18 до 25 - юноша/девушка
# от 25 до 60 - взрослый(ая)
# от 60 до 90 - пенсионер
# 90+ - долгожитель

# str conditional
# ==
# !=

# не пользуясь elif-ами
if age < 0:
    print(f'{name} не врите!')
if age > 0 and age <= 6:
    print(f'{name} ребёнок!')
if age > 6 and age <= 18:
    print(f'{name} школьник!')
if 18 < age <= 25:
    print(f'{name} юноша/девушка!')
if 25 < age <= 60:
    print(f'{name} взрослый!')
if 60 < age <= 90:
    print(f'{name} пенсионер!')
else:
    print(f'{name} долгожитель!')

# пользуясь elif-ами
if age < 0:
    print(f'{name} не врите!')
elif age <= 6:
    print(f'{name} ребёнок!')
elif age <= 18:
    print(f'{name} школьник!')
elif age <= 25:
    print(f'{name} юноша/девушка!')
elif age <= 60:
    print(f'{name} взрослый!')
elif age <= 90:
    print(f'{name} пенсионер!')
else:
    print(f'{name} долгожитель!')