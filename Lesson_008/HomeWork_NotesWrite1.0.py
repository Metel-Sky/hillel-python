def add_note(notes):

    note = input("Введіть нотатку: ")
    notes.append(note) #  Додаємо нотатку
    print("Нотатка додана!")

def sort_by_earliest(notes):
    sorted_n = sorted(notes) #  Сортуємо
    print("Від найранішої до найпізнішої:")
    for note in sorted_n:
        print(note)

def sort_by_latest(notes):

    sorted_n = sorted(notes, reverse=True) #  Сортуємо
    print("Від найпізнішої до найранішої:")
    for note in sorted_n:
        print(note)

def sort_by_longest(notes):

    sorted_n = sorted(notes, key=len, reverse=True) #  Сортуємо
    print("Від найдовшої до найкоротшої:")
    for note in sorted_n:
        print(note)

def sort_by_shortest(notes):

    sorted_n = sorted(notes, key=len) #  Сортуємо
    print("Від найкоротшої до найдовшої:")
    for note in sorted_n:
        print(note)

def notes():

    notes = []

    while True:
        # Виводимо доступні команди і зразу переводимо в нижній регістр
        command = input("Доступні команди: add, shortest,"
                        " longest, latest, earliest > ").lower()

        if command == "add":
            add_note(notes)

        elif command == "earliest":
            sort_by_earliest(notes)

        elif command == "latest":
            sort_by_latest(notes)

        elif command == "longest":
            sort_by_longest(notes)

        elif command == "shortest":
            sort_by_shortest(notes)

        else:
            print("Невідома команда")

if __name__ == '__main__':
    notes()
