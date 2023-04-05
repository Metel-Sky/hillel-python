import csv
# import pandas - продвинутое чтение и анализ csv файлов


def read_csv_examples():
    """
    Примеры чтения csv файла с заголовком и без заголовка
    """
    # csv.reader() - для чтения csv файлов без заголовков
    # newline нужно указывать пустой строкой, когда мы работаем с csv-файлами

    # delimeter разделитель колонок, по умолчанию запятая
    # quotechar экранирование записей, по умолчанию " двойные кавычки. Внутри экранирования разделитель
    # трактуется как обычный текст
    with open('children.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        print(type(reader))
        # reader[0] - это не список, это подвид генератора
        for row in reader:
            print(type(row), row)

    # csv.DictReader() - для чтения csv файлов с ЗАГОЛОВКОМ
    with open('children.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)  # , delimiter=' ', quotechar='|')
        print(type(reader))
        # reader[0] - этл не список, это подвид генератора
        for row in reader:
            print(type(row), row)


def write_csv_examples():
    """
    Примеры записи в csv файл с заголовком и без заголовка
    """
    # csv.writer() - для записи csv файлов без заголовков
    # нужно подготовить список списков или список кортежей
    # подсписки должны быть одной длины
    header = ("Цена", "Название", "Новый заголовок")
    data = [
        ('Чай', 10),
        ('Эспрессо', 12),
        ('Раф', 15),
        ('Малиновый пончик', 15),
        ('Шоколадный пончик; с глазурью', 15),
        ('Круассан', 15)
    ]
    with open('cafe_menu.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"')
        print(type(writer))
        # запишем заголовок
        writer.writerow(header)
        # записать все ряды сразу
        writer.writerows(data)
        # если у нас всех рядов пока нету, мы записываем их по очереди
        # for row in data:
        #    writer.writerow(row)

    dict_list = list()
    for menu_item in data:
        dict_list.append({
            "Название": menu_item[0],
            "Цена": menu_item[1]
        })
    print(dict_list)
    # csv.DictWriter() - для записи csv файлов с заголовками
    # нужно подготовить список словарей и заголовок
    # заголовок задаётся при создании, а записывается в файл отдельной командой
    # заголовок должен соответствовать ключам словарей в списке данных

    # если в header есть заголовки, которых нет в ключах - будут пустые колонки (или ячейки)
    # если в ключах есть то чего нет в header - ошибка
    with open('cafe_menu_header.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, header, delimiter=';', quotechar='"')
        print(type(writer))
        writer.writeheader()
        writer.writerows(dict_list)


if __name__ == '__main__':
    read_csv_examples()
    write_csv_examples()
