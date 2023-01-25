def all_divisions(x: int) -> list:  # функция нахождения всех делителей числа
    lst = [1, x]  # список с делителями, состоящий как по умолчанию из 1 и самого числа
    d = 2
    while d * d <= x:
        if x % d == 0:  # находим первый делитель и добавляем его
            lst.append(d)
            if x // d > d:  # добавляем и противоположный первому делитель, если он отличается
                lst.append(x // d)
        d += 1
    return sorted(lst)  # сортируем массив перед возвратом


def main():
    for x in range(143146, 143215):
        r = all_divisions(x)
        if len(r) == 6:
            print(' '.join(str(s) for s in r))


if __name__ == "__main__":
    main()
