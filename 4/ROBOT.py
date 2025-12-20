import csv

with open("36031.csv", "r") as f:
    t = list(csv.reader(f))
    for i in range(len(t)):
        t[i] = list(map(int, t[i][0].split(';')))

# Разворачиваем матрицу (чтобы идти от конца к началу)
reversed_grid = [r[::-1] for r in t[::-1]]

# Заполняем значения с путем
for i in range(len(reversed_grid)):
    for j in range(len(reversed_grid[i])):
        if i == 0 and j == 0:
            # Начальная позиция (конечная точка в исходной матрице)
            reversed_grid[i][j] = [reversed_grid[i][j], ["начало"]]
            continue
        elif i == 0:
            # Первая строка - всегда движение ВЛЕВО (поскольку не можем идти вверх)
            total_value = reversed_grid[i][j] + reversed_grid[i][j - 1][0]
            path_sequence = reversed_grid[i][j - 1][1] + ["влево"]
            reversed_grid[i][j] = [total_value, path_sequence]
        elif j == 0:
            # Первый столбец - всегда движение ВВЕРХ
            total_value = reversed_grid[i][j] + reversed_grid[i - 1][j][0]
            path_sequence = reversed_grid[i - 1][j][1] + ["вверх"]
            reversed_grid[i][j] = [total_value, path_sequence]
        else:
            # Выбор оптимального пути
            if reversed_grid[i - 1][j][0] >= reversed_grid[i][j - 1][0]:
                # Движение сверху (ВВЕРХ)
                total_value = reversed_grid[i][j] + reversed_grid[i - 1][j][0]
                path_sequence = reversed_grid[i - 1][j][1] + ["вверх"]
                reversed_grid[i][j] = [total_value, path_sequence]
            else:
                # Движение слева (ВЛЕВО)
                total_value = reversed_grid[i][j] + reversed_grid[i][j - 1][0]
                path_sequence = reversed_grid[i][j - 1][1] + ["влево"]
                reversed_grid[i][j] = [total_value, path_sequence]

final_result = reversed_grid[-1][-1]

#  путь ведет от конца к началу
print(f"\nМаксимальное количество монет: {final_result[0]}")
print(f"\nПуть от конца к началу:")
print(f"Путь : {' '.join(final_result[1])}")
