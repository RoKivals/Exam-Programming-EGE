def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n > 2:
        return F(n - 1) * n + F(n - 2) * (n - 1)


def main():
    print(F(5))


if __name__ == "__main__":
    main()
