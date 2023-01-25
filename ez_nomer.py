def differ(x: int) -> int:
    older_num = str(x)[0:2]
    little_num = str(x)[-2:]
    return abs(int(older_num) - int(little_num))


def main():
    valid_arr = []
    for x in range(1234567, 7654321):
        if differ(x) != 0 and x % differ(x) == 0:
            valid_arr.append(x)
    print(len(valid_arr))
    print(max(valid_arr))


if __name__ == "__main__":
    main()
