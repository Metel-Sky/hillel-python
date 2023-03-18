def task1():
    previous = float(input("Введіть попередні данні : "))
    current = float(input("Введіть поточні данні : "))
    tariff = float(input("Введіть тариф : "))

    p = current - previous  # Отнимаем предварительные от текущих показателей
    y = tariff * p  # умножаем на тариф
    x = round(y, 2)  # сокращаем количество цифр после запятой
    print(f'Сумма до сплати:  {x}')