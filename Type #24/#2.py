def main():
    with open("text/24_2.txt", 'r') as file:
        s = file.read()
    maximum = 0
    curr_max = 0
    for i in s:
        if i == 'Z':
            curr_max += 1
        else:
            maximum = max(curr_max, maximum)
            curr_max = 0
    else:
        maximum = max(curr_max, maximum)
    print(maximum)


if __name__ == '__main__':
    main()
