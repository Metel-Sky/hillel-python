x = '123456'

print(len(x))

pin = '4444'
if len(pin) == 4:
    print('Processing...')
else:
    print('PIN must be 4 digits!')

if 'Marco' == 'Marco':
    print('Marco is Marco!')
else:
    print('Marco is not Marco!')

# как это начиналось
list_of_guests = """ Andrew,
 Julia,
 Anton,
 Natasha,
 Olesya,
 Oleksiy,
 Ivan,
"""

name = ' ' + input('Hey, this is private party, what is your name? ') + ','
# in - оператор поиска. Возвращает True если нашел, False если нет
if name in list_of_guests:
    print('Добро пожаловать!')
else:
    print('Что-то не вижу вашего имени в списке приглашенных.')


# вечеринка обиженных и сердитых, куда пускают ВООБЩЕ всех кроме узурпаторов изначальной вечеринки
blacklist = """ Andrew,
 Julia,
 Anton,
 Natasha,
 Olesya,
 Oleksiy,
 Ivan,
"""

name = ' ' + input('Hey, this is hate party, what is your name? ') + ','
# in - оператор поиска. Возвращает True если нашел, False если нет
if name not in blacklist:
    print('Добро пожаловать!')
else:
    print('Что-то не вижу вашего имени в списке приглашенных.')

those_who_tried = ''

# операция инкремента (взять себя же и добавить что-то в конец)
those_who_tried = those_who_tried + name
# то же самое
those_who_tried += name

user_command = 'EXIT'
"""
# так наслиовать if не стоит, лучше воспользоваться lower()
if user_command == 'EXIT':
    # выход из программы (досрочный, в этой строчке)
    exit()
if user_command == 'exit':
    exit()
if user_command == 'eXiT':
    exit()
if user_command == 'Exit':
    exit()
"""

if user_command.lower() == 'exit':
    print('exiting...')
    exit()