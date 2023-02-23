import itertools as it


def main():
    # Рассматриваем все перестановки данных символов
    prod = it.permutations("ЛЕВИЙ")
    count = 0
    for i in prod:
        # Проверяем нет ли сочетания ЕИ в строке, которая собрана из кортежа i
        if i[0] != 'Й' and 'ЕИ' not in ''.join(i):
            count += 1
    print(count)


if __name__ == '__main__':
    main()
