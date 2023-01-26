def allDivs(x: int) -> list:  # функция нахождения всех делителей числа
    divs = [1, x]
    d = 2
    while d * d <= x:
        if x % d == 0:  # нашли делитель
            divs.append(d)
            if x // d > d:  # проверили есть ли у него пара не равная ему
                divs.append(x // d)
        d += 1
    return sorted(divs)


def isPrime(x: int) -> bool:  # функция проверки на простое число
    if x <= 1: return False
    d = 2
    while d * d <= x:
        if x % d == 0:  # если делится на любое число, то сразу не простое
            return False
        d += 1
    return True


def isValid(x: int) -> int:  # фукнция проверки условия задачи
    primeDivs = [d for d in allDivs(x)[1:-1] if isPrime(d)]
    s = sum(primeDivs)
    if s > 250 and x % s == 0:
        return s
    else:
        return 0


def main():
    s, e = 33333, 55555
    for x in range(s, e + 1):
        s = isValid(x)
    if s > 0:
        print(x, s)


if __name__ == "__main__":
    main()
