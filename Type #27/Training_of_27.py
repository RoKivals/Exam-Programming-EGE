def main():
    file = open("27.txt")
    summa = 0
    num_of_div = 3
    min_of_pair = 10001
    N = int(file.readline())
    for x in range(N):
        a, b = map(int, file.readline().split())
        summa += min(a, b)
        d = abs(a - b)

        if d % num_of_div > 0:
            min_of_pair = min(min_of_pair, d)

    if summa % num_of_div != 0:
        print(summa)
    else:
        print(summa + min_of_pair)


if __name__ == "__main__":
    main()
