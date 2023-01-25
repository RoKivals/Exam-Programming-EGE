def main():
    file = open("text/17(Triangle).txt", 'r')
    arr = []
    for i in file:
        arr.append(int(i))
    file.close()
    maxim = -30000
    cnt = 0

    for i in range(len(arr) - 2):
        sides = tuple(arr[i + j] for j in range(3))
        sides = sorted(sides)
        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            cnt += 1
            maxim = max(sum(sides), maxim)

    if cnt:
        print(cnt, maxim, sep='---------')
    else:
        print(0, 0)


if __name__ == "__main__":
    main()
