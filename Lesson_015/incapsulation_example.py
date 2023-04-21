# Уровни доступа (Инкапсуляция)
# public - доступен всем
# _protected - доступен только классу и его наследникам
# __private = доступен только самому классу
class TestClass:
    def __init__(self):
        self.normal_attr = 5
        self._protected_attr = 5
        self.__private_attr = 5

    def __str__(self):
        return f"{self.normal_attr=} {self._protected_attr=} {self.__private_attr=}"

    # getter - получатель, чтение свойства
    @property
    def private_attr(self):
        return self.__private_attr

    # setter - установитель, запись свойства
    @private_attr.setter
    def private_attr(self, x):
        if isinstance(x, int) or isinstance(x, float):
            if x > 0:
                self.__private_attr = x

    # getter - получатель, чтение свойства
    @property
    def protected_attr(self):
        return self._protected_attr

    # setter - установитель, запись свойства
    @protected_attr.setter
    def protected_attr(self, x):
        if isinstance(x, int) or isinstance(x, float):
            if x > 0:
                self._protected_attr = x


if __name__ == '__main__':
    a = TestClass()
    a.protected_attr = -10
    print(a)
    print(a.private_attr)
    a.private_attr = -10
    print(a)
    a.private_attr = 10
    print(a)