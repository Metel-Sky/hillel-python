


def text_file_read(file_handler) -> str:
    text = file_handler.read()
    return text


def text_file_readline(file_handler) -> list:
    # в этом списке мы храним все строки файла
    lines = list()
    # здесь мы храним текущую строчку которую мы читаем
    next_line = file_handler.readline()
    # пока текущая строчка не пустая - в файле еще есть что читать
    while next_line:
        # добавляем текущую строчку в список строчек
        lines.append(next_line.strip())
        # читаем следующую строчку
        next_line = file_handler.readline()
    # возвращаем список прочитанных строк файла
    return lines


def text_file_readlines(file_handler) -> list:
    lines = list()
    for line in file_handler.readlines():
        lines.append(line.strip())
    return lines


# В программировании не как в жизни
# Файл одновременно можно ИЛИ читать ИЛИ писать
# Пока идёт чтение или запись в файл, другие программы не имеют доступ к этому файлу
# Чтобы не блокировать другие программы, лучше файл быстро прочитать/записать и закрыть
# mode r - чтение (read) - загрузка (load)
# mode w - запись (write) - сохранение (save)
# encoding='utf-8' - если не открывает кириллицу по умолчанию. Если и с этим не открывает -
# гуглить/чатгпт какая кодировка подойдёт
if __name__ == '__main__':
    # вот так лучше не делать
    f = open('my_text_file.txt', 'r', encoding='utf-8')
    # потому что файл надо где-то закрыть и не всегда очевидно где это происходит
    f.close()

    # with open(<обычные параметры>) as <имя переменной обработчика файла (file handler)>:
    # вместе с открытием такого-то файла в таком-то режиме, под названием/известный как f:
    with open('my_text_file.txt', 'r', encoding='utf-8') as f:
        # FileHandle == TextWrapper == Обработчик файла
        # IO = input/output
        print(f)
        print(type(f))
        print('Readable: ', f.readable())
        print('Writable: ', f.writable())

        # от 50 MB - увесистый файл
        # 1 гб и выше - очень тяжелый файл и на него нужна особая обработка
        print(text_file_read(f).split('\n'))

        # При чтении файла, объект TextWrapper (который мы получаем через open()) запоминает текущий прогресс чтения
        # Функцией f.seek() можно изменить прогресс
        # Например, выполнив f.seek(0), можно перейти обратно в начало файла
        f.seek(0)
        print('Мы перешли в начало файла')
        print('Print with readline')
        print(text_file_readline(f))

        f.seek(0)
        print('Мы перешли в начало файла')
        print('Print with readlineS')
        print(text_file_readlines(f))
