# #Фибоначчи
#
# N = int(input("N = "))
#
# l = [0, 1]
#
# for i in range(N - 2):
#     new_el = l[0] + l[1]
#     l[0] = l[1]
#     l[1] = new_el
# print(l[1])


# def kuznechik(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     l = [1, 1, 2]
#     for i in range(n - 3):
#         new = l[0] + l[1] + l[2]
#         l = [l[1], l[2], new]  # сдвиг
#
#     return l[2]
#
# n = int(input("N: "))
# itog = kuznechik(n)
# print(f"Кол-во способов: {itog}")



def turtle_max_coins(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    # Заполняем первую клетку
    dp[0][0] = grid[0][0]

    # Заполняем первую строку
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Заполняем первый столбец
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Заполняем остальное
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[-1][-1]

CoinsOld = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 40, 70, 0, 0, 1],
    [100, 0, 0, 0, 0, 1],
]

Coins = [
    [0, 1, 11],
    [0, 1, 2],
    [0, 1, 15],
]

N = 4
M = 6

for i in range(len(Coins)):
    for j in range(len(Coins[i])):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j != 0:
            Coins[i][j] = Coins[i][j] + Coins[i][j - 1]
        elif i != 0 and j == 0:
            Coins[i][j]  = Coins[i][j] + Coins[i - 1][j]
        else:
            Coins[i][j] = max(Coins[i - 1][j], Coins[i][j - 1]) + Coins[i][j]

print(Coins[-1][-1])



