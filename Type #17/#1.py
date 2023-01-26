def main():
    l = []
    f = open('text/17.txt', 'r')
    for i in f:
        l.append(int(i))
    f.close()

    cnt = 0
    maxim = -20001

    for j in range(len(l) - 1):
        if l[j] % 3 == 0 or l[j + 1] % 3 == 0:
            cnt += 1
            maxim = max(maxim, l[j] + l[j + 1])

    print(cnt)
    print(maxim)


if __name__ == "__main__":
    main()
