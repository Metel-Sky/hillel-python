class Animal:
    # initialization
    # Конструктор класса
    # вызывается автоматически при создании объекта класса
    # Animal.__init__() то же самое, что Animal()
    def __init__(self, name: str, preferred_food: set, age: int):
        """
        :param name: имя животного
        :param preferred_food: перечень употребляемой еды
        :param age: возраст животного
        """
        # задаём новое свойство (property) этому класса
        # свойство = атрибут = поле
        # self.variable_name = some_value
        self.name = name
        self.preferred_food = preferred_food
        self.age = age

        self.say_word = "???"
        self.animal_type = "Животное"
        # Уровни доступа (Инкапсуляция)
        # public - доступен всем
        # _protected - доступен только классу и его наследникам
        # __private = доступен только самому классу
        self.__hungry = True

        # все поля класса должны задаваться в его конструкторе
        # представьте что какое-то свойство задаётся в одном методе, а используется в другом
        # где гарантии что методы будут вызваны в правильном порядке?
        # ведь если сначала прочитать еще несуществующее значение, будет ошибка
        # Чтобы её не было никогда, нужно объявлять атрибуты только в конструкторе класса
        # return self представьте что оно здесь так

    # getter - получатель, чтение свойства
    @property
    def hungry(self):
        return self.__hungry

    @hungry.setter
    def hungry(self, x):
        """
        Hungry может быть только булевым значением
        По логике работы программы можно только проголодаться
        Чтобы утолить голод, недостаточно присвоить False в hungry
        Нужно вызвать метод eat
        :param x:
        :return:
        """
        if isinstance(x, bool):
            if x:
                self.__hungry = True

    def __str__(self):
        return f"{self.animal_type} по имени {self.name}, {self.age} лет."

    def eat(self, food: str):
        """

        :param food:
        :return:
        """
        if food in self.preferred_food:
            print(f"{self.name} кушает {food}")
            self.__hungry = False
        else:
            print(f"{self.name} такое не ест: {food}")

    def say(self):
        """

        :return:
        """
        print(f"{self.name} говорит: {self.say_word}. Голод животного: {self.__hungry}")

    def treat(self, hours: int = 1):
        """
        Ухаживать ха животным, переопределяется наследниками
        :param hours:
        :return:
        """
        print(f"Вы ухаживаете за {self.name} {hours} час(ов)")
        if self.__hungry:
            print(f"{self.name} голодное!")


if __name__ == '__main__':
    a = Animal(None, {None}, None)
    # int(a)
    # a.eat(None) от порядка вызова зависит будет ли ошибка.
    # a.say()
    # hasattr - has attribute, проверка есть ли такое свойство/атрибут/поле у конкретного объекта класса
    print(hasattr(a, 'name'))
    print(hasattr(a, 'nameee'))
    print()