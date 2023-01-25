def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) * n


def main():
    print(F(5))


if __name__ == "__main__":
    main()
