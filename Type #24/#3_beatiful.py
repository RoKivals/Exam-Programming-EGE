def main():
    file = open('text/24_3.txt', 'r')
    s = file.read()
    file.close()
    maximum = curr_max = 0
    for i in range(len(s)):
        if (s[i] == "X" and curr_max % 3 == 0) or \
                (s[i] == "Y" and curr_max % 3 == 1) or \
                (s[i] == "Z" and curr_max % 3 == 2):
            curr_max += 1
        else:
            maximum = max(curr_max, maximum)
            curr_max = 0
    else:
        maximum = max(curr_max, maximum)
        print(maximum)


if __name__ == '__main__':
    main()
