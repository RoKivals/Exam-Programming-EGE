def main():
    count = 0
    min_x = 22000
    list_d = [11, 13, 17, 19]
    for x in range(22000, 10999, -1):
        k = 0
        for d in range(1, 20):
            if x % d == 0 and d in list_d:
                k += 1
        if k == 2:
            count += 1
            min_x = x
    print(count, min_x)


if __name__ == "__main__":
    main()
