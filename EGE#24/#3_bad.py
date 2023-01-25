def main():
    file = open('text/24_3.txt', 'r')
    s = file.read()
    file.close()
    maximum = 0
    curr_max = 0
    i = 0
    while i < len(s) - 3:
        if s[i] + s[i + 1] + s[i + 2] == "XYZ":
            curr_max += 3
            i += 3
        elif s[i] + s[i + 1] == "XY":
            i += 2
            curr_max += 2
            maximum = max(curr_max, maximum)
            curr_max = 0
        elif s[i] == "X":
            i += 1
            curr_max += 1
            maximum = max(curr_max, maximum)
            curr_max = 0
        else:
            maximum = max(curr_max, maximum)
            curr_max = 0
            i += 1

    print(maximum)


if __name__ == '__main__':
    main()
