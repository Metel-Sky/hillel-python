from math import sqrt  # Імпорт бібліотеки
def read_side():  #  Приймаємо сторони трикутника
    while True:  # Запуск безкінечного циклу
        side = input("Введіть додатнє число для сторони трикутника: ")  # Пропонуємо ввести число (Сторону трикутника)
        try:                                                            # Провіряємо на додатнє число
            side = float(side)                                          # Встановлюємо тип числа
            if side > 0:                                                # Якщо число не додатнє просимо ввести ще раз
                return side                                             # Повертаємо додатнє число
        except ValueError:                                              # Якщо число не додатнє починаємо все спочатку
            pass  # Нічого не робимо
        print("Це не додатнє число! "
              "Будь ласка, введіть додатнє число.")                     # Вказуєм на помилку
                                                                        # знов просимо дурня ввести додатнечисло

def check_triangle(a, b, c):   # Порівнюєм сторони трикутника
    if a + b > c and a + c > b and b + c > a: # Якщо тут все ок ідем далі
        return True
    else:  # Якщо не ок то пишем ВСЕ ПРОПАЛО!!!
        return False

def calculate_perimeter(a, b, c):  # Дізнаємся периметр
    return a + b + c

def calculate_area(a, b, c):  # Дізнаємся площу
    half_p = calculate_perimeter(a, b, c) / 2
    return sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))

if __name__ == '__main__':
    print("Введіть сторони трикутника:")
    a = read_side()
    b = read_side()
    c = read_side()

    if check_triangle(a, b, c):
        perimeter = calculate_perimeter(a, b, c)
        area = calculate_area(a, b, c)

        print(f"Трикутник існує зі сторонами {a}, {b}, {c}")
        print(f"Периметр трикутника: {perimeter}")
        print(f"Площа трикутника: {area}")
    else:
        print(f"ВСЕ ПРОПАЛО!!! Трикутника зі сторонами {a}, {b}, {c} не існує")
