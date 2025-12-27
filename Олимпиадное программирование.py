def f(n, dup=None):
    if dup is None:
        dup = []
    # Базовый случай
    if len(n) <= 1:
        return n
    # Условие 1
    if len(n) >= 2 and n[0] >= n[1]:
        # Добавляем только если элемента еще нет в dup
        if n[1] not in dup:
            dup.append(n[1])
        return f(n[1:], dup)
    # Условие 2
    if len(n) >= 4 and n[1] >= n[2] >= n[3]:
        return f(n[:1] + n[2:], dup)
    # Условие 3: поиск дубликатов из dup в n
    for i in range(len(n)):
        if n[i] in dup:
            # Проверяем, есть ли этот элемент более одного раза в n
            count_in_n = n.count(n[i])
            if count_in_n > 1:
                # Удаляем текущий элемент (первый найденный дубликат из dup)
                return n[:i] + n[i + 1:]
    return n


print(f([6, 2, 5, 4, 2, 5, 6]))