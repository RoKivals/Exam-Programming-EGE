def main():
    with open("text/24_demo.txt", 'r') as f:
        s = f.read()

    maximum = 0
    curr_max = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            maximum = max(curr_max, maximum)
            curr_max = 1
        else:
            curr_max += 1
    else:
        maximum = max(curr_max, maximum)

    print(maximum)


if __name__ == '__main__':
    main()
