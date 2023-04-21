

# зчитуємо вміст файлу та розділяємо на лінії
lines = [line.strip("\n") for line in open("input.txt", "r")]

# застосовуємо перетворення до кожної лінії використовуючи list comprehension
result = [line[line.find("a"):] if "a" in line else "" for line in lines]
result = [line.capitalize() for line in result]

# результат
print(result)
