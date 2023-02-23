'''
Задание 12. (ЕГЭ -  9764)
Решение использует функцию подсчёта кол-ва подстрок в строке (str.count)
'''


def main():
    s = "9" * 127

    while s.count("999") or s.count("333"):
        if s.count("333"):
            s = s.replace("333", "9", 1)
        else:
            s = s.replace("999", "3", 1)

    print(s)


if __name__ == '__main__':
    main()
