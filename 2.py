class NewtonResult:
    def __init__(self, root, iterations, success):
        self.root = root
        self.iterations = iterations
        self.success = success


def f(x):
    """f(x) = x³ - 5"""
    return x**3  - 5


def df(x):
    """f'(x) = 3x² - 2"""
    return 3*x**2 

def solveNewtonMethod(initial_x, eps):
    x = initial_x
    iterations = 0

    while True:
        iterations += 1
        fx = f(x)
        dfx = df(x)

        if abs(dfx) == 0:
            print("Производная равна нулю!")
            break

        x_new = x - fx / dfx
        delta = abs(x_new - x)

        print("Итерация {}: x = {:.8f}, f(x) = {:.10f}, Δx = {:.8f}".format(iterations, x, fx, delta))

        if delta < eps:
            x = x_new
            break

        x = x_new

    print("\nКорень:",x)
    print("Итераций: ",iterations)
    print("f(x) = ",f(x))


def findRootNewton(initial_x, eps):
    x = initial_x
    iterations = 0

    while True:
        iterations += 1
        fx = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-15:
            print("Производная равна нулю!")
            return float('nan')

        x_new = x - fx / dfx
        delta = abs(x_new - x)

        if delta < eps:
            print("Количество итераций:",iterations)
            return x_new

        x = x_new


def findRootWithDetails(initial_x, eps):
    x = initial_x
    iterations = 0

    while True:
        iterations += 1
        fx = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-15:
            return NewtonResult(float('nan'), iterations, False)

        x_new = x - fx / dfx
        delta = abs(x_new - x)

        if delta < eps:
            return NewtonResult(x_new, iterations, True)

        x = x_new


if __name__ == "__main__":
    x0 = 0
    epsilon = 0.00001
    solveNewtonMethod(x0, epsilon)
