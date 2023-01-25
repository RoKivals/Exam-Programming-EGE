"""
Условие: Task1.png.

P.S. Нас интересуют только те случаи, когда F ложна.
"""


# Функция, содержащая логическое выражение
def function(x, y, z, w):
    return (not x and not y) or (y == z) or not w


def main():
    print('x y z w')
    # В алгебре логики переменная может принимать только два значения (False / True),
    # что в Python эквивалентно (0 / 1).
    value = 0, 1
    for x in value:
        for y in value:
            for z in value:
                for w in value:
                    if not function(x, y, z, w):
                        print(x, y, z, w)


if __name__ == "__main__":
    main()
