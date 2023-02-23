# start - текущее
# x - конечное

def numProg(start, x):
    if start < x:
        return 0
    if x == start:
        return 1
    return numProg(start - 1, x) + numProg(start // 2, x)


def main():
    print(numProg(32, 11) * numProg(11, 1))


if __name__ == "__main__":
    main()
