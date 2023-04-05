import json

def read_json_examples():
    """
    Эта функция показывает примеры чтения json формата из файла или строки
     в переменную типа dict или list
    """
    # load
    with open('children.json', 'r') as fp:
        d = json.load(fp)
        print('\nLoad children.json')
        print(type(d))
        print(d)

    d = json.load(open('children.txt', 'r'))
    print('\nLoad children.txt')
    print(type(d))
    print(d)

    # loads
    with open('children.txt') as fp:
        json_text = fp.read()

    d = json.loads(json_text)
    print('\nLoad STRING text from children.txt')
    print(type(d))
    print(d)

    print('\nСмотрим содержимое Json')
    for children_json_data in d["children"]:
        print(children_json_data)

    d = json.loads('{"key1": "value1", "key2": 2}')
    print('\nLoad STRING text from our text dictionary')
    print(type(d))
    print(d)

    d = json.loads('[0.5, "value1", "value2", 2]')
    print('\nLoad STRING text from our text list')
    print(type(d))
    print(d)


def write_json_examples():
    """
    Эта функция показывает примеры записи в json формате в файла или строку
     из переменной типа dict или list
    :return:
    """
    d = {
        "Laptops": ['Lenovo ASDJH', 'MacBook Pro', 'Dell Latitude X123', 'Lenovo ASDJH', 'MacBook Pro',
                    'Dell Latitude X123'],
        "Keyboards": ['ASUS TUF', "Logitech 123xs", 'Razer ASDH&!@#'],
        "Server": ['Microsoft Server', 'Toshiba', 'Samsung'],
        "Monitors": ['Toshiba X123', 'Benq ASG@', 'Toshiba X123', 'Benq ASG@']
    }
    json.dump(d, open('tech_inventory.json', 'w'), indent=2, sort_keys=True)
    s = json.dumps(d, indent=4)
    print(type(d), d)
    print(type(s), s)

    d = [1, 2, 'value3', True]
    json.dump(d, open('tech_inventory.json', 'w'), indent=2, sort_keys=True)
    s = json.dumps(d, indent=4)
    print(type(d), d)
    print(type(s), s)


if __name__ == '__main__':
    # dump - сохраняет в файл
    # dumps - сохраняет в строку
    # load - загружает из файла
    # loads - загружает из строки
    # fp = File Pointer, fh = File Handler, tw - Text Wrapper, в принципе все синонимы
    write_json_examples()