





# имя + параметры/аргументы = сигнатура функции
def get_user_float(comment: str):
    # внутри функции - локальная область видимости
    while True:
        try:
            z = input(comment)
            return float(z)
        except Exception:
            print('Число!!!')


def get_user_int(comment: str):
    # внутри функции - локальная область видимости
    while True:
        try:
            z = input(comment)
            return int(z)
        except Exception:
            print('Число!!!')


MY_VAR = 'Python variable'

print('not main code', __name__)

# Весь код в Пайтон файлах должен иметь одну из 4 форм:
# 1. Внутри функции
# 2. Внутри main-конструкции: "if __name__ == '__main__':"
# 3. Импорт код
# 4. Объявление констант
# Весь остальной код на деле некорректен и его нужно куда-то направить.

# Пример обычного пайтон файла:
# импорты
# объявление констант
# объявление функций
# main-конструкция и основная логика в ней


def my_function(x):
    pass


if __name__ == '__main__':
    print('Main code')
