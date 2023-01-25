def Fy(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n > 1 and n % 3 != 0:
        return Fy(n - 1) + Fy(n - 2)
    elif n > 1 and n % 3 == 0:
        return Fy(n - 1) + Fy(n - 2) + Fy(n // 3)


def Fx(n):
    if n == 10:
        return Fy(10)
    elif n < 10:
        return Fy(n)
    elif n == 14:
        return 0
    elif n > 10 and n % 3 != 0:
        return Fx(n - 1) + Fx(n - 2)
    elif n > 10 and n % 3 == 0:
        return Fx(n - 1) + Fx(n - 2) + Fy(n // 3)


print(Fx(15))
