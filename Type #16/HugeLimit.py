# Рекурсивный метод работает за 6 +- минут
def F_recursive(n):
    if n == 0:
        return 0
    if n % 2:
        return F_recursive(n - 1) + 1
    if n > 0 and n % 2 == 0:
        return F_recursive(n / 2)


# Метод без рекурсии работает порядка 12 минут
def F_linear(n):
    result = 0
    while n:
        if n % 2 == 0:
            n /= 2
        if n % 2:
            result += 1
            n -= 1
        if n == 0:
            return result


# Работает по принципу нахождения 3 единиц, работает за 8 минут
def F_analytics(n):
    binary_digit = str(bin(n))[2:]
    return binary_digit.count('1')


def main():
    cnt = 0
    for n in range(1_000_000_000):
        # Одна из трёх любых функций
        if F_analytics(n) == 3:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
