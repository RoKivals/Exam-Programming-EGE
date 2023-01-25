array_of_100 = [i for i in range(20000000000, 40000000000, 100000)]  # Берём числа в интервале, делящиеся на 100 000
# из 2ККК остётся 200К
array_of_nums = []  # Пустой массив для вставки хранения элементов делящихся на 100 000 И 7
for i in array_of_100:
    if i % 7 == 0:
        array_of_nums.append(i)  # После всех итераций остаётся всего-лишь 28к чисел
min = max(array_of_nums)  # Изначально минимальное число равно максимально возможному в массиве
count_num = 0  # Кол-во цифр
for num in array_of_nums:
    if num % 13 != 0 and num % 29 != 0 and num % 43 != 0 and num % 101 != 0:  # Проверяем на неделимость на остальные числа
        count_num += 1
        if num < min:
            min = num

print(count_num)
print(min)
