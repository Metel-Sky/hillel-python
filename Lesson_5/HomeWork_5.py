
total = 0
while True:
    user_input = input("Введите число или sum: ")
    if user_input.lower() == "sum":
        break

    try:
        num = float(user_input)
        total += num
    except ValueError:
        print('Не корректный ввод')

print("Сумма введеных чисел:", total)

#__________________________________________________________________________________________________________________



total = []
while True:
    user_input = input("Введите число или sum: ")
    if user_input.lower() == "sum":
        break
    if user_input.isdigit():
        num = float(user_input)
        total.append(num)
    else:
        print('Не корректный ввод')
print("Сума введених чисел:", sum(total))


#____________________________________________________________________________________________________________________

total = []
while True:
    user_input = input("Введите число или sum: ")
    if user_input.lower() == "sum":
        break
    try:
        num = float(user_input)
        total.append(num)
    except ValueError:
        print('Не корректный ввод')

print("Сумма введеных чисел:", sum(total))






























































