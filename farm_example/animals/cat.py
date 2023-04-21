from .animal import Animal


class Cat(Animal):
    def __init__(self, name: str, preferred_food: set, age: int):
        super().__init__(name, preferred_food, age)
        self.say_word = "Мяв!"
        self.animal_type = "Кошка"

    def treat(self, hours: int = 1)-> str:
        print(f"Вы ухаживаете за {self.name} {hours} часов.")
        return "Мурчит"
