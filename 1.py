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

        print(x1, x2)

        print("Проверка по теореме Виета:")

        print((x1 + x2), (-b / a))
        print((x1 * x2), (c / a))

        if (abs((x1 + x2) - (-b / a)) < 1e-10 and
            abs((x1 * x2) - (c / a)) < 1e-10):
            print("Все норм!")
        else:
            print("Все плохо :(")

if __name__ == "__main__":
    a = 1
    b = 6
    c = 2
    solve_quadratic_equation(a, b, c)
