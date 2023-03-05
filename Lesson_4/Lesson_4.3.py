x = float(input('Input number x='))
y = float(input('Input another number y='))

if not x > y:
    if x == y:
        print(f'{x} and {y} are equal!')
    else:
        print(f'{x} is lesser than {y}')
else:
    print(f'{x} is greater than {y}')

print('_________________________________________________________')

i = 0
while i < 10:
    print('Я поднимаюсь по лестнице')
    print(f'Я на {i} этаже')

    # две идентичные команды
    # i = i + 1
    i += 1

print('Я поднялся!')
