from .animal import Animal


class Cow(Animal):
    def __init__(self, name: str, preferred_food: set, age: int):
        super().__init__(name, preferred_food, age)
        self.say_word = "Му-у-у!"
        self.animal_type = "Корова"

    def treat(self, hours: int = 1) -> str:
        print(f"Вы ухаживаете за {self.name} {hours} часов.")
        return "Молоко"