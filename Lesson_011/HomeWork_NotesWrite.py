
# add - додати нотатку
# shortest -  Від найкоротшої до найдовшої
# longest - Від найдовшої до найкоротшоЇ
# latest - Від найпізнішої до найранішої
# earliest - Від найранішої до найпізнішої
# exit -

# def text_file_writeline(file_handler, text_to_write: list):
#     # Записує в файл список строк
#     # Плюси: можна записувати багато тексту одразу
#     # Мінуси: не ставить перенос на нову строку
#     for line in text_to_write:
#         file_handler.write(line + '\n')

def text_file_writeline(file_handler, text_to_write: list):
    # записывает в файл список строк
    # плюсы: сразу много текста
    # минусы: не ставит перенос на новую строку
    for line in text_to_write:
        file_handler.write(line.rstrip() + '\n')


def text_file_write(file_handler, text_to_write: str):
    # Записує в файл просто строку
    file_handler.write(text_to_write)


def notes():
    # Зчитуємо нотатки з файлу, якщо він існує
    try:
        with open('notes.txt', encoding='utf-8') as read_f:
            notes_list = read_f.readlines()
    except FileNotFoundError:
        notes_list = []

    while True:
        command = input("Доступні команди: add, shortest, longest, latest, earliest, save&exit > ").lower()

        if command == "add":
            note = input("Введіть нотатку: ")
            notes_list.append(note)

        elif command == "earliest":
            sorted_notes = sorted(notes_list)
            print("Від найдавнішої до найновішої:")
            for note in sorted_notes:
                print(note)

        elif command == "latest":
            sorted_notes = sorted(notes_list, reverse=True)
            print("Від найновішої до найдавнішої:")
            for note in sorted_notes:
                print(note)

        elif command == "longest":
            sorted_notes = sorted(notes_list, key=len, reverse=True)
            print("Від найдовшої до найкоротшої:")
            for note in sorted_notes:
                print(note)

        elif command == "shortest":
            sorted_notes = sorted(notes_list, key=len)
            print("Від найкоротшої до найдовшої:")
            for note in sorted_notes:
                print(note)


        elif command == "save&exit":
            # Записуємо нотатки в файл і виходимо з програми
            with open('notes.txt', 'a', encoding='utf-8') as f:
                text_file_write(f, '\n')
                text_file_writeline(f, notes_list)
                print("Збережено в файлі.")
            break

        else:
            print("Невідома команда.")


if __name__ == '__main__':
    notes()
