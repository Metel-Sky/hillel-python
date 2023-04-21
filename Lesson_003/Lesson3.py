s = 'This is a string'
print(s)
s = "This is a string"
print(s)

# склеивание (или конкатенация) строк
s = 'String start' + ' ' + 'string end'
print(s)

b = 'String start'
a = 'String end'
c = 'String middle part'

ba = b + ' ' + a
print(ba)

bca = ' '.join([b, c, a])
print(bca)

# \n \t или пробел - символы разделения по умолчанию
print(bca.split())

bca_split_by_comma = bca.split(',')
print(bca_split_by_comma)

text_with_commas = 'Hello, my name is Kyrylo, I am programming in Python.'
print(text_with_commas.split(','))

s = '  this is line with spaces at start and in the end   '
print('.', s.strip(), '.', sep='=')
print('.', s.rstrip(), '.', sep='=')
print('.', s.lstrip(), '.', sep='=')

s = '.,.,.this is, line with dots. Many, dots. Too many...,..,,,.,.....'
print(s.strip('.,'))
print(s.rstrip('.,'))
print(s.lstrip('.,'))

s = 'We are coding in Python, Python is a great language, all hail Python!'
# так думают фронтендеры
print(s.replace('Python', 'Javascript'))

c + a
pattern_letter = """
Hello, dear {recipient_name}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada eleifend risus eu finibus. Pellentesque vestibulum purus eget felis pulvinar.

Date: {date}
Sincerely yours, {sender_name} 
"""

pattern_letter = pattern_letter.replace('{recipient_name}', 'Anton')
pattern_letter = pattern_letter.replace('{date}', '28 Feb 2023')
pattern_letter = pattern_letter.replace('{sender_name}', 'Kyrylo')

x = print(pattern_letter)

# None - пустота
print(x)

test_str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
test_str2 = 'AjJnsahjYUjnmxS'
# всё маленькими буквами
print(test_str.lower())
print(test_str2.lower())

# всё большими буквами
print(test_str.upper())
print(test_str2.upper())

# с большой буквы начало строки
print(test_str.capitalize())
print(test_str2.capitalize())

# с большой буквы каждое слово
print(test_str.title())
print(test_str2.title())

# поиск слева, возвращает индекс первого найденного
print('Ipsum found from left:', test_str.find('ipsum'))
print(test_str.find('e'))
# если не находит - возвращает -1
print(test_str.find('python'))

# поиск справа
print(test_str.rfind('e'))
print('Ipsum found from right:', test_str.rfind('ipsum'))

filename = 'script.py'
print(f'Всё что правее индекса {filename.rfind(".")} - это расширение файла')
print(f'Заканчивается ли {filename} .py: ', filename.endswith('.py'))
print(f'Заканчивается ли {filename} .exe: ', filename.endswith('.exe'))

# whitespaces - перенос на новую строку = \n, пробел и знак табуляции (\t)
multiline_text = """client name
client last name
client card
operation type
operation value
bank
recipient name
recipient last name
recipient card"""

print('a', multiline_text)
# то же самое, что и multiline text, только хуже читается. Вернее, вообще не читается
# так делать не надо, но зато под капотом именно так и устроено
print('b', 'client name\nclient last name\nclient card\noperation type\noperation value\nbank\nrecipient name\nrecipient last name\nrecipient card')

print(multiline_text.split())
print(multiline_text.split('\n'))

multiline_text_b = '''line 1
line 2
line 3
line 4
line 5
'''

tab_string = 'operation a\t\tlkasjd\taSDASDASD\t\tASDASDASD'
print(tab_string)
tab_string = 'operation value\tbank\trecipient name\trecipient last name'
print(tab_string)

# попробуй выполнить "подозрительную" часть кода
try:
    x = float(input('Введите число: '))
# исключение в случае ошибки
except Exception:
    print('Вы ввели не число!')