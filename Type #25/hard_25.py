def is_valid(x: int) -> bool:
    s = str(x)
    arr = list(map(int, s))
    m = max(arr)
    if s.rfind(str(m)) != 0:
        return False
    else:
        return True


def find_divisors(x: int) -> list:
    array_of_dividers = [1, x]
    d = 2
    while d * d <= x:
        if x % d == 0:
            array_of_dividers.append(d)
            if x % (x // d) == 0:
                array_of_dividers.append(x // d)
                break
        d += 1
    return sorted(set(array_of_dividers))



def main():
    valid_arr = []
    for x in range(1082, 129932):
        if is_valid(x) and len(find_divisors(x)) == 3:
            valid_arr.append(x)

    print(valid_arr)



if __name__ == "__main__":
    main()
