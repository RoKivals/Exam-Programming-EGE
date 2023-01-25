def Func(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return Func(n / 2)
    if n % 2:
        return 1 + Func(n - 1)


def main():
    cnt = 0
    for n in range(1, 1001):
        if Func(n) == 3:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
