def main():
    file = open("text/17(2).txt", 'r')
    arr = []
    for i in file:
        arr.append(int(i))

    # Две переменные счётчики (сумма элементов и их количество)
    summa = 0
    cnt = 0
    for x in arr:
        if x % 2:
            summa += x
            cnt += 1
    # Среднее арифметическое нечётных элементов
    avg = summa / cnt

    maxim = -20000
    cnt_res = 0
    for i in range(len(arr) - 1):
        if (arr[i] % 5 == 0 and arr[i + 1] < avg) or \
                (arr[i + 1] % 5 == 0 and arr[i] < avg):
            cnt_res += 1
            maxim = max(arr[i] + arr[i + 1], maxim)
    print(cnt_res, maxim, sep='\n')


if __name__ == "__main__":
    main()
