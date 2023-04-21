

from Lesson_007.input_number import get_user_int

MENU = [
    ('Чай', 10),
    ('Эспрессо', 12),
    ('Раф', 15),
    ('Малиновый пончик', 15),
    ('Шоколадный пончик', 15),
    ('Круассан', 15)
]


def display_menu():
    """
    Пользуется константой MENU чтобы красиво и читаемо вывести на экран меню
    """
    print('Меню:')
    for menu_entry in MENU:
        name, price = menu_entry
        # https://pyformat.info
        # '{:10}'.format('test') ==  f'{"test":10}' одно и то же
        print(f'  {name:20} {price:.2f} UAH')


if __name__ == '__main__':
    # для поиска что есть в меню, а чего нет, будем использовать set()
    menu_set = set()
    for menu_entry in MENU:
        menu_set.add(menu_entry[0].lower())
    # print(menu_set)
    menu_dict = dict()
    for menu_entry in MENU:
        menu_dict[menu_entry[0].lower()] = menu_entry[1]
    print(menu_dict)

    user_pouch = get_user_int('Сколько у вас денег (UAH)? ', 0)

    while True:
        to_exit = input(f'Нажмите enter чтобы сделать заказ или введите exit чтобы уйти... ').lower()
        if to_exit == 'exit':
            exit(0)
        display_menu()
        order = input(f'У вас есть {user_pouch:.2f} UAH. Что будете заказывать? ').lower()
        if order in menu_dict:
            if user_pouch >= menu_dict[order]:
                user_pouch -= menu_dict[order]
                print(f'{order.capitalize()} подано, с вас {menu_dict[order]:.2f} UAH')
            else:
                print(f'{order.capitalize()} стоит {menu_dict[order]:.2f} UAH. У вас не хватает!')
        else:
            print(f'У нас нет {order}!')


# x = x + 2 то же самое x += 2
# x = x - 5 то же самое x -= 5
# x = x * 2 то же самое x *= 2
# x = x / 5 то же самое x /= 5