# # Задача 1
# with open("39762.txt", "r") as f:
#     a = list(map(int, f.read().split()))
#
# cnt1 = 0
# mx1 = 0
#
# for i in range(len(a) - 1):
#     x, y = a[i], a[i + 1]
#     if (x * y) % 15 == 0 and (x + y) % 7 == 0:
#         cnt1 += 1
#         if x + y > mx1:
#             mx1 = x + y
#
# print("1:", cnt1,"и", mx1)
#
# # Задача 2
# with open("68279.txt", "r") as f:
#     b = list(map(int, f.read().split()))
#
# m = 0
# for num in b:
#     if num % 1000 == 562 and num > m:
#         m = num
#
# cnt2 = 0
# mx2 = 0
#
# for i in range(len(b) - 3):
#     q = b[i:i + 4]
#
#     # условие 1
#     f5 = sum(1 for x in q if 10000 <= x <= 99999)
#     if not (1 <= f5 <= 2):
#         continue
#
#     # условие 2
#     k3 = sum(1 for x in q if x % 3 == 0)
#     k7 = sum(1 for x in q if x % 7 == 0)
#     if k3 >= k7:
#         continue
#
#     # условие 3
#     s = sum(q)
#     if m < s < 2 * m:
#         cnt2 += 1
#         if s > mx2:
#             mx2 = s
#
# print("2:", cnt2,"и", mx2)
#
# # Задача 3
# with open("40992.txt", "r") as f:
#     c = list(map(int, f.read().split()))
#
# odd = [x for x in c if x % 2 != 0]
# if odd:
#     avg = sum(odd) / len(odd)
# else:
#     avg = 0
#
# cnt3 = 0
# mx3 = 0
#
# for i in range(len(c) - 1):
#     x, y = c[i], c[i + 1]
#
#     if (x % 5 == 0 or y % 5 == 0):
#         if x < avg or y < avg:
#             cnt3 += 1
#             if x + y > mx3:
#                 mx3 = x + y
#
# print("3:", cnt3,"и",mx3)