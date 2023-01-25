"""
Условие: Task2.png.

P.S. Нас интересуют все возможные случаи F, так как она равна и 1, и 0.
"""


# Функция, содержащая логическое выражение
def function(x, y, z, w):
    return ((not w or not x) == (not z or y)) and (y or w)


def main():
    # Функция 'rjust' используется для красивого вывода, она никак не влияет на работоспособность кода.
    print('x'.rjust(3), 'y'.rjust(6), 'z'.rjust(6), 'w'.rjust(6), sep='')
    # Ещё один вариант указания возможных значений.
    value = False, True
    for x in value:
        for y in value:
            for z in value:
                for w in value:
                    print(x, y, z, w, function(x, y, z, w))


if __name__ == "__main__":
    main()
