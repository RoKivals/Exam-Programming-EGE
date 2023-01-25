'''
Рассматривается множество целых чисел, принадлежащих числовому отрезку [1000, 70000],
которые имеют 5 знаков в восьмеричной и 6 знаков в пятеричной записи,
а их запись в шестнадцатеричной системе счисления заканчивается на 'FA'.
Найдите количество таких чисел и максимальное из них. В ответе запишите два целых числа: сначала количество, затем максимальное число.
'''


def end_16(i):
    for n in range(2):
        if i % 16 == 10:
            i //= 16
            if i % 16 == 15:
                return True
            else:
                return False
        else:
            return False


def signs_8(i):
    count = 0
    while i:
        i //= 8
        count += 1
    if count == 5:
        return True
    else:
        return False


def signs_5(i):
    count = 0
    while i:
        i //= 5
        count+=1
    if count == 6:
        return True
    else:
        return False


def main():
    num = 0
    maximum = 0
    for i in range(1000, 70001):
        if signs_5(i) and signs_8(i) and end_16(i):
            num += 1
            if i > maximum:
                maximum = i
    print(num, maximum)


if __name__ == "__main__":
    main()
