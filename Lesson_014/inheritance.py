# inheritance - наследование
# класс родитель (супер, базовый класс)
# класс наследник (subclass, дочерний класс)

class MySuperClass:
    def __init__(self, a: float):
        self.a = a

    def pow(self, n: int):
        return pow(self.a, n)


class MySubClass(MySuperClass):
    def pow(self, n: int, to_print=False):
        if to_print:
            print('I print')
        return super().pow(n)

    def div(self, n: float):
        return self.a / n


if __name__ == '__main__':
    msc = MySuperClass(5)
    print(msc.pow(2))
    print(type(msc))

    msubclass = MySubClass(5)
    print(msubclass.pow(2, to_print=True))
    print(type(msubclass))

    print(msubclass.div(2))