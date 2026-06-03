import math

def solve_quadratic_equation(a, b, c):
    D = b * b - 4 * a * c
    if D < 0:
        print("Нет корней")
    elif D == 0:
        x = -b / (2.0 * a)
        print(x)
    else:
        x1 = (-b + math.sqrt(D)) / (2.0 * a)
        x2 = (-b - math.sqrt(D)) / (2.0 * a)

        print(x1 + x2)

        print("Проверка по теореме Виета:")

        print((x1 + x2) + (-b / a))
        print((x1 * x2) + (c / a))

        if (abs((x1 + x2) - (-b / a)) < 1e-10 and
            abs((x1 * x2) - (c / a)) < 1e-10):
            print("Все норм!")
        else:
            print("Все плохо :(")


def get_quadratic_roots(a, b, c):
    D = b * b - 4 * a * c
    if D < 0:
        return []
    elif D == 0:
        x = -b / (2.0 * a)
        return [x]
    else:
        x1 = (-b + math.sqrt(D)) / (2.0 * a)
        x2 = (-b - math.sqrt(D)) / (2.0 * a)
        return [x1, x2]


if __name__ == "__main__":
    a = 1
    b = 2
    c = 1
    solve_quadratic_equation(a, b, c)
