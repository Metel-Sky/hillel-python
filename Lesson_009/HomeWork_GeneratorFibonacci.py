

#  генератор послідовності чисел Фібоначч

def fibonacci(end_index):
    a, b = 0, 1
    for i in range(end_index):
        yield a
        a, b = b, a + b


for number in fibonacci(30):
    print(number)