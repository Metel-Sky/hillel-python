
# add - додати нотатку
# shortest -  Від найкоротшої до найдовшої
# longest - Від найдовшої до найкоротшоЇ
# latest - Від найпізнішої до найранішої
# earliest -Від найранішої до найпізнішої
def notes():
    notes = []

    while True:
        command = input("доступні команди: add, "
                        "shortest,  longest, latest, earliest > ").lower()

        if command == "add": # додаемо нотатку
            note = input("Введіть нотатку: ")
            notes.append(note)

        elif command == "earliest":#
            sorted_n = sorted(notes)
            print("Від найранішої до найпізнішої:")
            for note in sorted_n:
                print(note)

        elif command == "latest":#
            sorted_n = sorted(notes, reverse=True)
            print("Від найпізнішої до найранішої:")
            for note in sorted_n:
                print(note)

        elif command == "longest":#
            sorted_n = sorted(notes, key=len, reverse=True)
            print("Від найдовшої до найкоротшоЇ:")
            for note in sorted_n:
                print(note)

        elif command == "shortest":
            sorted_n = sorted(notes, key=len)
            print("Від найкоротшої до найдовшої:")
            for note in sorted_n:
                print(note)



        else:
            print("Невідома команда")

if __name__ == '__main__':
    notes()
