import math


def up_low_border(lower, upper):
    for i in range(lower, upper):
        s = str(math.sqrt(i))
        if s[-2:] == '.0':
            low = int(math.sqrt(i))
            break

    for i in range(upper, lower, -1):
        s = str(math.sqrt(i))
        if s[-2:] == '.0':
            up = int(math.sqrt(i))
            break
    return low, up


def dividers(n):
    i = 2
    r = []
    while i * i <= n:
        while n % i == 0:
            r.append(i)
            n /= i
        i = i + 1
    if n > 1:
        r.append(n)
    return r


def bool_3div(num):
    a = dividers(num)
    n = 1
    prev_iter = 0
    for i in a:
        if i != prev_iter:
            itog = 1
            itog += a.count(i)
            n *= itog
            prev_iter = i
    return n


def main():
    summa = 0
    low, upper = up_low_border(123456789, 223456788)
    a = [i ** 2 for i in range(low, upper)]
    for i in a:
        if bool_3div(i) == 5:
            print(f'Вот число, у которого 3 нетривиальных делителя: {i}')
            print(f'А это его наибольший делитель: {math.sqrt(i)}')


if __name__ == "__main__":
    main()
