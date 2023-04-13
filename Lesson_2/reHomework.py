
def komun():
    previous_readings = float(input('Введіть попередні показники: '))
    current_readings = float(input('Введіть поточні показники: '))
    tariff = float(input('Введіть тариф: '))

    difference = current_readings - previous_readings
    payable = tariff * difference
    print(f'До сплати {round(payable,2)}грн')

def fuel_consumption():
    pass

if __name__ == '__main__':
    komun()