#1
# from collections import Counter
#
# with open('59778.csv', encoding='utf-8') as f:
#     data = [list(map(int, line.strip().split(';'))) for line in f]
#
# count = 0
# for row in data:
#     c = Counter(row)
#     vals = list(c.values())
#     if sorted(vals) != [1, 1, 1, 4]:
#         continue
#     a = [k for k, v in c.items() if v == 4][0]
#     others = [k for k, v in c.items() if v == 1]
#     if sum(others) / 3 > 4 * a:
#         count += 1
#
# print(count)



#2
import csv

numbers = []
with open("29666.csv", 'r') as file:
    r = csv.reader(file, delimiter=';')
    for row in r:
        numbers.extend([float(x.replace(',', '.')) for x in row]) #запятые на точки для преобразования

max_sum = numbers[0]
n = len(numbers)
print(numbers)
for i in range(n): #все возможные начальные позиции
    current_sum = numbers[i]
    current_max = numbers[i]

    for j in range(i + 1, n):
        if numbers[j] < numbers[j - 1]: #следующее число меньше предыдущего
            current_sum += numbers[j]
            if current_sum > current_max:
                current_max = current_sum
        else: #если нарушается, то прерываем
            break

    if current_max > max_sum:
        max_sum = current_max

print(f"Максимальная сумма {max_sum}")