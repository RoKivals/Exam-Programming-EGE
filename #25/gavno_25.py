def base_8_num(x:int) -> int:
    answer = ''
    while x:
        answer = str(x % 8) + answer
        x //= 8
    answer = answer.strip()
    return len(answer)


def is_valid(n: int) -> bool:
    s_dec = str(n)
    if len(s_dec) == base_8_num(n):
        return True
    else:
        return False


def main():
    array_of_nums = []
    for x in range(127, 9852):
        if is_valid(x) and x % 3 == 0 and x % 9 !=0:
            array_of_nums.append(x)

    print(len(array_of_nums))
    print(max(array_of_nums))



if __name__ == "__main__":
    main()
