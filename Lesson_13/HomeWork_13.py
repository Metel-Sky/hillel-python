import random

class Cat:
    def __init__(self, name, breed, age, weight):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight
        self.is_hungry = True
        self.is_sleeping = False
        self.is_playing = False
        self.hunger_level = 5
        self.boredom_level = 5

    def eat(self):
        self.is_hungry = False
        self.hunger_level = 10
        print(self.name + " Їсть.")

    def play(self):
        self.is_playing = True
        self.boredom_level = 10
        print(self.name + " грається.")

    def sleep(self):
        self.is_sleeping = True
        print(self.name + " спить.")

    def meow(self):
        print(self.name + " мявчить!")

    def go_for_a_walk(self):
        self.is_playing = True
        self.boredom_level = 10
        print(self.name + " збирається на прогулянку.")

    def __str__(self):
        return "{} їв/їла ({}), {} років, важить {} кг {}голодний , {}сумує і {} спить.".format(
            self.name, self.breed, self.age, self.weight, "" if not self.is_hungry else "не дуже ",
            "" if not self.is_playing else "дуже ", "" if not self.is_sleeping else "")


cat_names = ["Мурка", "Зорька", "Шкряба", "Мурзік", "Льолік", "Болік"]
cat_breeds = ["Віскас", "Пуріна", "4 лапи", "Мишей", "Кашу", "Нагетси"]
cat_ages = [2, 3, 4, 5, 6, 7]
cat_weights = [3, 4, 5, 6, 7, 8]

cats = []
for i in range(6):
    cat = Cat(cat_names[i], cat_breeds[i], cat_ages[i], cat_weights[i])
    cats.append(cat)


for cat in cats:
    print(cat)
    cat.is_hungry = True
    cat.is_playing = False
    cat.is_sleeping = False
    cat.hunger_level = random.randint(1, 10)
    cat.boredom_level = random.randint(1, 10)
    if cat.hunger_level > 5:
        cat.eat()
    if cat.boredom_level > 5:
        cat.play()
    if random.random() < 0.5:
        cat.meow()
    if random.random() < 0.5:
        cat.go_for_a_walk()
    if cat.is_hungry:
        print(cat.name + " дуже голодний(на)!")
    if not cat.is_playing:
        print(cat.name + " сумує.")
