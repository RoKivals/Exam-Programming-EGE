def Check(num: int, arr: list) -> bool:
    mid = int(len(arr) / 2)
    quarter = int(len(arr) / 4)
    if num > arr[mid] and num < arr[len(arr) - quarter]:
        return True
    return False


def main():
    arr = []
    file = open("Text/26-50.txt")
    n = int(file.readline())
    for line in file:
        arr.append(int(line))
    file.close()
    arr.sort()
    count = 0
    min_S = 1e10
    for i in range(1, n - 1):
        if arr[i] % 2 == 0:
            for j in range(i + 1, n):
                if arr[j] % 2 == 0:
                    sredn = int((arr[i] + arr[j]) / 2)
                    if Check(sredn, arr):
                        if sredn < min_S:
                            count += 1
                            min_S = sredn
    print(f"{count}   {min_S}")


if __name__ == "__main__":
    main()
