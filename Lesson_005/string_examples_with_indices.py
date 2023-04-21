


# отрезаем расширение файла

filename = 'string_examples_with_indices.py'

i = filename.rfind('.')

print(filename[:i])
print(filename[i:])

# join & split

text = """
The diesel engine, named after Rudolf Diesel, is an internal combustion
 engine in which ignition of the fuel is caused by the elevated temperature 
 of the air in the cylinder due to mechanical compression; thus, the diesel 
 engine is called a compression-ignition engine (CI engine). This contrasts 
 with engines using spark plug-ignition of the air-fuel mixture, such as a 
 petrol engine (gasoline engine) or a gas engine (using a gaseous fuel like 
 natural gas or liquefied petroleum gas)."""

text_words = text.split()

# сколько раз в тексте применяется слово ignition?
len_text_words = len(text_words)
for i in range(len_text_words):
    print(i, end=' ')
    print(text_words[i])

i = 0
while text_words >= len_text_words:
    print()

print()

for word in text_words:
    print(word, end=' ')
