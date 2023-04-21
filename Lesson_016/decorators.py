def decorator_function(f):
    def wrapper(name: str):
        print('This is before our function')
        f(name)
        print('This is after')
    return wrapper


@decorator_function
def printer(name: str):
    print(f'Hello, {name}!')


"""
@route('/home')
def printer(name: str):
    print(f'Hello, {name}!')
"""

if __name__ == '__main__':
    printer('python')