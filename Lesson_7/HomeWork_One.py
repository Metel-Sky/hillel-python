def task1(previous, current, tariff):


    p = current - previous  # Отнимаем предварительные от текущих показателей
    y = tariff * p  # умножаем на тариф
    x = round(y, 2)  # сокращаем количество цифр после запятой

    return print(f'Сумма до сплати:  {x}')


