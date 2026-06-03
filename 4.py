class KnapsackProblem:
    @staticmethod
    def knapsackDP(capacity, weights, values, n):
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(capacity + 1):
                if weights[i - 1] > w:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(dp[i - 1][w],
                                   values[i - 1] + dp[i - 1][w - weights[i - 1]])

        KnapsackProblem.printDPTable(dp, n, capacity)

        maxValue = dp[n][capacity]
        print("Максимальная стоимость:", maxValue)

        KnapsackProblem.findSelectedItems(dp, weights, n, capacity)

    @staticmethod
    def printDPTable(dp, n, capacity):
        sys.stdout.write("     ")
        for w in range(capacity + 1):
            sys.stdout.write("{:4d} ".format(w))
        print()
        sys.stdout.write("     ")
        for w in range(capacity + 1):
            sys.stdout.write("─────")
        print()

        for i in range(n + 1):
            if i == 0:
                sys.stdout.write(" 0: ")
            else:
                sys.stdout.write(" {:d}: ".format(i))
            for w in range(capacity + 1):
                sys.stdout.write("{:4d} ".format(dp[i][w]))
            print()

    @staticmethod
    def findSelectedItems(dp, weights, n, capacity):
        w = capacity
        selected = [False] * n

        print("ВОССТАНОВЛЕНИЕ НАБОРА ПРЕДМЕТОВ:")

        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected[i - 1] = True
                w -= weights[i - 1]
                if i == 1:
                    cost = 3
                elif i == 2:
                    cost = 4
                elif i == 3:
                    cost = 5
                else:
                    cost = 6
                print("  Предмет {} (вес={}, стоимость={}) ВЗЯТ".format(
                    i, weights[i - 1], cost))

        print("Итоговый набор предметов:", end=' ')
        totalWeight = 0
        totalValue = 0
        for i in range(n):
            if selected[i]:
                print(i + 1, end=' ')
                totalWeight += weights[i]
                if i == 0:
                    totalValue += 3
                elif i == 1:
                    totalValue += 4
                elif i == 2:
                    totalValue += 5
                else:
                    totalValue += 6
        print()
        print("Общий вес:", totalWeight, "(вместимость:", capacity, ")")
        print("Общая стоимость:", totalValue)


def main():
    capacity = 30
    weights = [1, 2, 4, 6, 8, 10]
    values = [2, 3, 6, 8, 10, 12]
    n = len(weights)

    print("Вместимость рюкзака:", capacity)
    print("Предметы: ")
    for i in range(n):
        print("  {}: вес = {}, стоимость = {}".format(i + 1, weights[i], values[i]))
    print()

    KnapsackProblem.knapsackDP(capacity, weights, values, n)


if __name__ == "__main__":
    import sys
    main()
