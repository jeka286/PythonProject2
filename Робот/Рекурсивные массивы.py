# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# # Проверка функции:
# print(factorial(1))  # 1
# print(factorial(2))  # 2
# print(factorial(3))  # 6
# print(factorial(4))  # 24
# print(factorial(5))  # 120
# print(factorial(6))  # 720
# print(factorial(7))  # 5040
# print(factorial(8))  # 40320


# #2
#
# def remove_vowels(string):#если не гласные буквы то убирает, если гласные то оставляет
#     vowels = 'aeiouAEIOU'  #строчные и заглавные гласные
#     result = ''
#     for char in string:
#         if char not in vowels:
#             result += char
#     return result
#
# # Проверка функции:
# print(remove_vowels('apple'))      # ppl
# print(remove_vowels('orange'))     # rng
# print(remove_vowels('pear'))       # pr
# print(remove_vowels('pineapple'))  # pnppl
# print(remove_vowels('durian'))     # drn
# print(remove_vowels('banana'))     # bnn

# # 3
# def pascal(n):
#     # n-я строка треугольника Паскаля
#     row = [1]
#
#     for i in range(1, n):
#         # Создаем новую строку
#         new_row = [1]
#         for j in range(1, i):
#             new_row.append(row[j - 1] + row[j])
#         new_row.append(1)
#         row = new_row
#
#     return row
#
# print(pascal(8))




# Final boss
def solve(maze, row=None, col=None, path=None):
    if row is None:
        # ищу стартовую позицию
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 's':
                    # ищу все возможные пути, добавляя старт в начало
                    result = solve(maze, i, j, [])
                    # добавляю стартовую точку в каждый найденный путь
                    for route in result:
                        route.insert(0, f's({i},{j})')
                    return result
        return []

    # если робот дошёл до цели (x) - добавляем этот путь в результат
    if maze[row][col] == 'x':
        return [path] if path else [[]]

    orig = maze[row][col]  # сохраняю оригинальное значение клетки
    maze[row] = maze[row][:col] + '#' + maze[row][col + 1:]  # помечаю клетку как посещённую

    all_paths = []
    directions = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]

    for x, y, direction in directions:
        new_row, new_col = row + x, col + y

        # проверяю, можно ли двигаться в эту клетку
        if (0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and
                maze[new_row][new_col] != '#'):
            # рекурсивно ищу пути из новой позиции
            additional_paths = solve(maze, new_row, new_col, path + [direction])
            all_paths.extend(additional_paths)  # добавляю найденные пути к общему списку

    # восстановление оригинального значения клетки для других ветвей поиска
    # maze[row] = maze[row][:col] + orig + maze[row][col + 1:]
    return all_paths

maze = [
    's----',
    '##---',
    '---##',
    '----x'
]

result = solve(maze)
for i in result:
    print(i)



