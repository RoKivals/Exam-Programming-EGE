from csv import reader

rows = []


def process(stroka):
    if stroka[2] == [0]:
        return stroka[1]
    else:
        maximum = 0
        for i in stroka[2]:
            maximum = max(maximum, process(rows[i - 1]))
        return maximum + stroka[1]


def main():
    with open("source/22_4.csv") as f:
        s = reader(f, delimiter=';')
        next(s)
        for i in s:
            rows.append([int(i[0]), int(i[1]), list(map(int, str(i[2]).split(';')))])
        for i in range(len(rows)):
            print(i + 1, process(rows[i]))


if __name__ == '__main__':
    main()
