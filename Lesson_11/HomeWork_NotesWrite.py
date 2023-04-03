
# add - додати нотатку
# shortest -  Від найкоротшої до найдовшої
# longest - Від найдовшої до найкоротшоЇ
# latest - Від найпізнішої до найранішої
# earliest - Від найранішої до найпізнішої
# exit -


def text_file_write(file_handler, text_to_write: str):
    # записывает в файл просто строку
    file_handler.write(text_to_write)


def notes():
    with open('my_file', encoding='utf-8') as read_f:
        notes_list = read_f.readlines()[:]

    while True:
        command = input("доступні команди: add, "
                        "shortest,  longest, latest, earliest, exit > ").lower()

        if command == "add":
            note = input("Введіть нотатку: ")
            notes_list.append(note)

        elif command == "earliest":
            sorted_notes = sorted(notes_list)
            print("Від найранішої до найпізнішої:")
            for note in sorted_notes:
                print(note)

        elif command == "latest":
            sorted_notes = sorted(notes_list, reverse=True)
            print("Від найпізнішої до найранішої:")
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

        elif command == "exit":
            with open('my_file', 'a', encoding='utf-8') as f:
                text_file_write(f, '\n')
                for note in notes_list:
                    text_file_write(f, note + '\n')
            break

        else:
            print("Невідома команда")

if __name__ == '__main__':
    notes()