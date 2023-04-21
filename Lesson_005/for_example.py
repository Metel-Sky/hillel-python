


text = """
The diesel engine, named after Rudolf Diesel, is an internal combustion
 engine in which ignition of the fuel is caused by the elevated temperature 
 of the air in the cylinder due to mechanical compression; thus, the diesel 
 engine is called a compression-ignition engine (CI engine). This contrasts 
 with engines using spark plug-ignition of the air-fuel mixture, such as a 
 petrol engine (gasoline engine) or a gas engine (using a gaseous fuel like 
 natural gas or liquefied petroleum gas)."""

text_words = text.split()



# итерируемые типы данных - те которые можно разложить на независимые равные элементы

for i in range(10):
    print('Я поднимаюсь по лестнице')
    print(f'Я на {i} этаже')
print('Я поднялся!')


len_text_words = len(text_words)
for i in range(len_text_words):
    print(i, end=' ')
    print(text_words[i])

# for <объявляем переменную> in <источник данных>:
# в объявленную переменную будет записан каждый элемент данных из источника
for i in 'Я поднимаюсь по лестнице':
    print(i)

print()
# можно так же проходиться по спискам
for i in [1, 2, 3, 4]:
    print(i)