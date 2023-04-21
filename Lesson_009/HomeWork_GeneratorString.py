
# Генератор

def word_gen(s):
    words = s.split()
    for word in words:
        yield word


s = input('Введіть текст: ') # Вместо *i am generating words from text*
for word in word_gen(s):
    print(word)