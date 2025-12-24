#ЗАДАЧА 1
print("Задача 1:")

# 1) от 3 до 10
R = {3: 1}
for x in range(4, 11):
    ways = R.get(x-1, 0)
    ways += R.get(x-2, 0)
    if x % 2 == 0:
        ways += R.get(x//2, 0)
    R[x] = ways

ways_3_to_10 = R[10]
print(f"  Способов из 3 в 10: {ways_3_to_10}")

# 2) от 10 до 12
T = {10: 1}
for x in range(11, 13):
    ways = T.get(x-1, 0)
    ways += T.get(x-2, 0)
    if x % 2 == 0:
        ways += T.get(x//2, 0)
    T[x] = ways

ways_10_to_12 = T[12]
print(f"  Способов из 10 в 12: {ways_10_to_12}")

total_1 = ways_3_to_10 * ways_10_to_12
print(f"  Всего программ: {total_1}")

print()

#ЗАДАЧА 2
print("Задача 2:")

def ways_f(start, end, forbidden):
    dp = {start: 1}
    for x in range(start, end + 1):
        if x == forbidden:
            dp[x] = 0
        if x not in dp:
            continue
        # команда +1
        nx = x + 1
        if nx <= end:
            dp[nx] = dp.get(nx, 0) + dp[x]
        # команда 2x+1
        nx = 2*x + 1
        if nx <= end:
            dp[nx] = dp.get(nx, 0) + dp[x]
    return dp.get(end, 0)

result_2 = ways_f(1, 27, 26)
print(f"  Всего программ: {result_2}")

print()

#ЗАДАЧА 3
print("Задача 3:")

def ways_s(start, end, forbidden):
    if start > end:
        return 0
    dp = [0] * (end + 3)
    dp[start] = 1
    for x in range(start, end + 1):
        if x == forbidden:
            dp[x] = 0
        if dp[x] > 0:
            if x + 1 <= end:
                dp[x + 1] += dp[x]
            if x + 2 <= end:
                dp[x + 2] += dp[x]
    return dp[end]

# Разбиваем: 2 -> 9 (не проходя через 14), 9 -> 18 (не проходя через 14)
ways_2_to_9 = ways_s(2, 9, 14)
ways_9_to_18 = ways_s(9, 18, 14)

print(f"  Способов из 2 в 9 без 14: {ways_2_to_9}")
print(f"  Способов из 9 в 18 без 14: {ways_9_to_18}")

total_3 = ways_2_to_9 * ways_9_to_18
print(f"  Всего программ: {total_3}")