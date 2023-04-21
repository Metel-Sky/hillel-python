from datetime import datetime, timedelta  # , time, date

if __name__ == '__main__':
    x = datetime.now()
    print(x)
    print(type(x))
    print('microsecond', x.microsecond)

    x = datetime(year=2023, month=4, day=9, hour=8, minute=0)
    print(x)
    # m = method
    # p = property (свойство)
    # f = function
    print('hour', x.hour)
    print('weekday', x.weekday())  # день недели, понедельник - 0, воскресенье - 6
    print('timestamp', x.timestamp())

    y = datetime.fromtimestamp(x.timestamp() + 120)
    print(y)

    z = datetime.now() + timedelta(days=2, hours=3)
    print(z)
    print(z.weekday())

    # ==