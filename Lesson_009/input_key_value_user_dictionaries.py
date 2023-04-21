def populate_dict_key_value(my_dict: dict) -> dict:
    """

    :param my_dict:
    :return:
    """
    key = input('Введите ключ словаря: ')
    value = input(f'Введите значение для ключа {key}: ')
    my_dict[key] = value
    return my_dict


def populate_dict_pair(my_dict: dict) -> dict:
    """

    :param my_dict:
    :return:
    """
    while True:
        try:
            pair = input('Введите ключ и значение, разделив их двоеточием: ')
            key, value = pair.split(':')
            my_dict[key] = value
            break
        except Exception:
            print('Пожалуйста, только одно двоеточие!')
    return my_dict


if __name__ == '__main__':
    d = {
        "Laptops": 5,
        "Keyboards": 2,
        "Server": 3
    }
    d = populate_dict_pair(d)
    d = populate_dict_key_value(d)
    print(d)