# Используем библиотеку для создания различных сочетаний и комбинаций
from itertools import product


def main():
    sym_set = input("Введите данный вам набор символов")
    rep_count = int(input("Введите длину создаваемой комбинации"))
    p = product(sym_set, repeat=rep_count)  # Создаём все возможные комбинации из данного набора символов длиной 5
    res_count = 0  # Итоговое значение, нужное нам для подсчёта выполнения условия
    # Здесь уже вручную поменять необходимое вам условие
    for x in p:
        if x.count('Й') <= 1 and x.count('Т') >= 1:
            res_count += 1
    print(res_count)


if __name__ == "__main__":
    main()
