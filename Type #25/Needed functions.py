# Нахождение простых делителей числа
def simple_dividers(digit: int):
    res = []
    d = 2
    while digit != 1:
        if digit % d == 0:
            res.append(d)
            digit /= d
        else:
            d += 1
    return res


# Нахождение обычных делителей (!не простых!)
def dividers(digit: int):
    res = [1, digit]
    d = 2
    while d * d <= digit:
        if digit % d == 0:
            res.append(d)
            res.append(digit // d)
        d += 1
    return sorted(res)


# Проверка на простое число
def IsSimple(digit: int):
    if len(dividers(digit)) == 2:
        return True
    else:
        return False