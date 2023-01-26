def check(elem: str) -> int:
    max_len = 0
    if elem.count("G") >= 25:
        pass
    else:
        for sym in elem:
            if elem.count(sym) > 1:
                max_len = max(max_len, elem.rfind(sym) - elem.find(sym))
    return max_len


def main():
    f = open("inf_26_04_21_24.txt")
    maximum = 0
    for s in f.readlines():
        maximum = max(maximum, check(s))
    f.close()
    print(maximum)


if __name__ == "__main__":
    main()
