import turtle as t  # Подключим модуль черепашка


def main():
    t.color("black", "red")
    k = 100  # коэффициент для настраивания более удобного масштаба
    t.speed(50)
    t.begin_fill()
    for i in range(5):  # пропишем алгоритм построения фигуры по условию
        t.forward(9 * k)
        t.right(72)
    t.end_fill()
    canvas = t.getcanvas()
    x_max = -100000
    for x in range(-100 * k, 100 * k, k):
        for y in range(-100 * k, 100 * k, k):
            item = canvas.find_overlapping(x, y, x, y)
            if len(item) == 1 and item[0] == 5:
                x_max = max(x_max, x)
    print(x_max // k)
    t.done()


if __name__ == '__main__':
    main()
