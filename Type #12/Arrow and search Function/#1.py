# Решение задачи номер 12 ЕГЭ-2021. Обработка длинной строки чисел.

def search(s, element):  # Функция нахождения элемента в строке
    if s.find(element) != -1:  # Если в строке есть элемент, то вернётся его индекс, если нет, то -1
        return True
    else:
        return False


def main():
    s = ">"  # Пустая строка, которую мы будем заполнять числами

    # Заполнение строки определённым кол-вом чисел
    for i in range(10):
        s = s + "1"
    for i in range(20):
        s = s + "2"
    for i in range(30):
        s = s + "3"

    while search(s, '>1') or search(s, '>2') or search(s, ">3"):  # or search(s, '2222'):
        if search(s, ">1"):
            s = s.replace('>1', '>22', 1)  # Заменяем элементы строго по-одному
        if search(s, ">2"):
            s = s.replace('>2', '2>', 1)
        if search(s, ">3"):
            s = s.replace('>3', '1>', 1)
    summa = 0
    s = str(s)
    s = s[:-1]
    for x in s:
        summa += int(x)
    print(summa)


if __name__ == '__main__':
    main()