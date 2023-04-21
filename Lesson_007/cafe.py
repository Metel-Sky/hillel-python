

MENU = [
    ('Tea', 10),
    ('Coffee', 12),
    ('Donut', 15)
]


def display_menu():
    print('Menu:')
    for menu_entry in MENU:
        name, price = menu_entry
        # https://pyformat.info
        # '{:10}'.format('test') ==  f'{"test":10}' одно и то же
        print(f'  {name:10} {price:.2f} UAH')


if __name__ == '__main__':
    menu_set = set()
    for menu_entry in MENU:
        menu_set.add(menu_entry[0])
    print(menu_set)

    display_menu()

    order = input('What is your order? ')
    if order in menu_set:
        print(f'У нас есть {order}!')
    else:
        print(f'У нас нет {order}!')