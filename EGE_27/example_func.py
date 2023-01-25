def main():
    f = open('27.txt', 'r')
    summa = 0
    array_of_minD = [10001] * 6
    num_division = int(input("Какому числу кратна сумма:"))
    count_of_pairs = int(f.readline())
    for x in range(count_of_pairs):
        a, b = map(int, f.readline().strip().split())
        summa += max(a, b)
        d = abs(a - b)
        r = d % num_division
        if r > 0:
            temp_array = array_of_minD[:]
            for k in range(1, num_division):
                r0 = (r + k) % num_division
                temp_array[r0] = min(d + array_of_minD[k], temp_array[r0])
            temp_array[r] = min(d, temp_array[r])
            array_of_minD = temp_array[:]
    if summa % num_division == 0:
        print(summa)
    else:
        print(summa - array_of_minD[summa % num_division])


if __name__ == "__main__":
    main()
