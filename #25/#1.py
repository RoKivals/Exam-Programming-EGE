'''
РЕШУ-ЕГЭ № 27422
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [174457;174505],
числа, имеющие ровно два различных делителя, кроме единицы и самого числа.
Для каждого найденного числа запишите два делителя в порядке возрастания произведения этих двух делителей.
Делители в строке также должны следовать в порядке возрастания.
'''


# Нахождение обычных делителей (!не простых!)
def dividers(digit: int):
    res = []
    d = 2
    while d * d <= digit:
        if digit % d == 0:
            res.append(d)
            res.append(digit // d)
        d += 1
    return sorted(res)


def main():
    res = []
    for i in range(174457, 174506):
        arr = dividers(i)
        if len(arr) == 2:
            res.append(arr)
            print(arr, arr[0] * arr[1])

    print(sorted(res, key=lambda x: x[0] * x[1]))


if __name__ == '__main__':
    main()
