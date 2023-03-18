



def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def calculate_perimeter(a, b, c):
    return a + b + c

def calculate_area(a, b, c):
    half_p = calculate_perimeter(a, b, c) / 2
    return sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))

if __name__ == '__main__':
    print("Введіть сторони трикутника:")
    a = read_side()
    b = read_side()
    c = read_side()

    if check_triangle(a, b, c):
        perimeter = calculate_perimeter(a, b, c)
        area = calculate_area(a, b, c)

        print(f"Трикутник існує зі сторонами {a}, {b}, {c}")
        print(f"Периметр трикутника: {perimeter}")
        print(f"Площа трикутника: {area}")
    else:
        print(f"Трикутник зі сторонами {a}, {b}, {c} не існує")































