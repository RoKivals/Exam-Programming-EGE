'''
Задание 12. (ЕГЭ -  9365)
Решение использует функцию вхождения подстроки в строку (in).

! Наиболее эффективный вариант решения !
'''


def main():
    s = "8" * 68
    while "222" in s or "888" in s:
        if "222" in s:
            s = s.replace("222", "8", 1)
        else:
            s = s.replace("888", "2", 1)
    print(s)


if __name__ == '__main__':
    main()
