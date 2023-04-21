if __name__ == '__main__':
    with open('my_file', encoding='utf-8') as read_f:
        lines_to_save = read_f.readlines()[:3]
        # print(lines, type(lines))
    lines_to_save.append(input("Нам нужны новые строки, вводите: ") + '\n')
    lines_to_save.append(input("Еще парочку: ") + '\n')
    lines_to_save.append(input("И последнюю: ") + '\n')
    with open('my_file', 'w', encoding='utf-8') as write_f:
        text = ''.join(lines_to_save)
        # грубо, жестко, но действенно, работает лучше на чужой непонятной программе
        # .replace('\n\n', '\n').replace('\n\n\n', '\n')
        # лучше задействовать правильную модель данных. Т.е. выбрать ОДНО из двух:
        # 1. \n Хранятся в конце каждой строки
        # 2. \n добавляются между строчками при склеивании и записи
        # Выбирать оба одновременно - не стоит
        write_f.write(text)
        # None - это не пустая строка
        # write_f.writelines(lines_to_save)