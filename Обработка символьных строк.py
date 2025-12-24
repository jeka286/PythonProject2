#1 задача
# with open('27686.txt', 'r') as f:
#     s = f.read()
#
# max_len = 0
# cur_len = 0
#
# for char in s:
#     if char == 'X':
#         cur_len += 1
#         if cur_len > max_len:
#             max_len = cur_len
#     else:
#         cur_len = 0
#
# print(max_len)




# #2 задача
# with open('36037.txt', 'r') as f:
#     s = f.read()
#
# max_len = 0
# cur_len = 0
# i = 0
#
# while i < len(s):
#     # Проверяем, начинается ли с i подстрока XZZY
#     if i + 4 <= len(s) and s[i:i+4] == 'XZZY':
#         max_len = max(max_len, cur_len + 3)  # можем взять XZZ без Y
#         cur_len = 3  # если пройти назад на 3 символа — это ZZX, но нам нельзя включать Y
#         # лучше начать после XZZY
#         i += 3  # перепрыгиваем на последний Z (чтобы не считать заново)
#         # но правильнее: сбрасываем cur_len и начинаем с символа после XZZY
#         cur_len = 0
#         i += 1  # переходим к следующему символу после XZZY
#         continue
#     else:
#         cur_len += 1
#         i += 1
#
# max_len = max(max_len, cur_len)
# print(max_len)


# #3 задача
# with open('46982.txt', 'r') as f:
#     s = f.read()
#
# count = 0
# i = 0
#
# while i < len(s):
#     if s[i] == 'E':
#         start = i
#         i += 1
#         length = 1
#         valid = True
#         while i < len(s) and s[i] != 'E':
#             if s[i] == 'F':
#                 valid = False
#             i += 1
#             length += 1
#         if i < len(s) and s[i] == 'E':
#             length += 1
#             if valid and length >= 12:
#                 count += 1
#             i += 1
#         else:
#             i = start + 1  # если второй E не найден, идём дальше
#     else:
#         i += 1
#
# print(count)


