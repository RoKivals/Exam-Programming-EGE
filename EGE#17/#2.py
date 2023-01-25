def main():
    # Открываем файл в режиме чтения
    file = open("text/17(1).txt", 'r')
    # Массив для хранения данных из файла
    arr = []
    for i in file:
        arr.append(int(i))

    # Две переменные: cnt - счётчик пар, maxim - максимальная сумма пар
    cnt = 0
    maxim = -20000

    # Идём по каждому элементу и смотрим каждый парный элемент справа от него (до конца списка)
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) % 120 == 0:
                cnt += 1
                maxim = max(arr[i] + arr[j], maxim)

    print(cnt, maxim, sep='\n')


if __name__ == "__main__":
    main()
