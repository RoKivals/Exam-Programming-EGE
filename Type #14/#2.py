# Массив сумм, которые кратны 80
ans = []

for x in range(12):
    for y in range(12):
        # Вычисляем значение арифм выражения
        t = int(str(y) + 'AA' + str(x), 12) + int(str(x) + '02' + str(y), 14)
        if t % 80 == 0:
            # Добавляем в список всех возможных выражений
            ans.append(t)

print(min(ans) // 80)
