def text_file_writeline(file_handler, text_to_write: list):
    # записывает в файл список строк
    # плюсы: сразу много текста
    # минусы: не ставит перенос на новую строку
    file_handler.writelines(text_to_write)


def text_file_write(file_handler, text_to_write: str):
    # записывает в файл просто строку
    file_handler.write(text_to_write)

    # искусственное создание ошибки
    # Как сообщить об ошибке
    # как сделать так, чтобы программа думала что у нее ошибка
    # raise ValueError("Здесь произошло что-то не так")


if __name__ == '__main__':
    with open('my_file', 'w', encoding='utf-8') as f:
        text_file_write(f, 'Привіт! Ми записуємо у звичайний текстовий файл!')
        text_file_writeline(
            f,
            ['\n' + x for x in ['line', ' line', '  line', '   line']]
        )

    # a - режим добавления. Всё то же, что и с режимом w, но изначальное содержимое файла не вытирается
    with open('my_file', 'a', encoding='utf-8') as f:
        text_file_write(f, '\n')
        text_file_write(f, 'Привіт! Ми записуємо у звичайний текстовий файл!')