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
    [0, 1, 16],
]

N = len(Coins)
M = len(Coins[0])

# Матрица для хранения пути (откуда пришли)
path = [[(0, 0)] * M for _ in range(N)]
path[0][0] = (-1, -1)  # Начальная точка

# Ваш алгоритм с записью пути
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j != 0:
            Coins[i][j] = Coins[i][j] + Coins[i][j - 1]
            path[i][j] = (i, j - 1)  # пришли слева
        elif i != 0 and j == 0:
            Coins[i][j] = Coins[i][j] + Coins[i - 1][j]
            path[i][j] = (i - 1, j)  # пришли сверху
        else:
            if Coins[i - 1][j] > Coins[i][j - 1]:
                Coins[i][j] = Coins[i - 1][j] + Coins[i][j]
                path[i][j] = (i - 1, j)  # пришли сверху
            else:
                Coins[i][j] = Coins[i][j - 1] + Coins[i][j]
                path[i][j] = (i, j - 1)  # пришли слева

max_coins = Coins[-1][-1]
print(f"Максимальное количество монет: {max_coins}")

# Восстанавливаем путь
path_coords = []
i, j = N - 1, M - 1

while (i, j) != (-1, -1):
    path_coords.append((i, j))
    i, j = path[i][j]

# Переворачиваем путь
path_coords.reverse()

# Выводим путь с указанием направления
print("Путь черепахи:")
for idx in range(1, len(path_coords)):
    prev_i, prev_j = path_coords[idx - 1]
    curr_i, curr_j = path_coords[idx]

    # Определяем откуда пришли
    if curr_i == prev_i + 1 and curr_j == prev_j:
        direction = "сверху"
    elif curr_i == prev_i and curr_j == prev_j + 1:
        direction = "слева"
    else:
        direction = "начало"

    print(f"  Из {direction} → ({curr_i}, {curr_j})")




