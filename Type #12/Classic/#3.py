'''
Задание 12. (ЕГЭ -  10290)
Решение использует функцию нахождения индекса подстроки в строке (str.find).
В случае отсутствия искомой подстроки find возвращает -1 (в отличие от str.index, которая вызывает ошибку).
'''


def main():
    s = "1" + "8" * 100000
    while s.find("18") != -1 or s.find("288") != -1 or s.find("3888") != -1:
        if s.find("18") != -1:
            s = s.replace("18", "2", 1)
        elif s.find("288") != -1:
            s = s.replace("288", "3", 1)
        else:
            s = s.replace("3888", "1", 1)
    print(s)


if __name__ == '__main__':
    main()
