for A in range(1000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if not((x > 9 or x ** 2 <= A) and (y ** 2 > A or y <= 9)):
                flag = False
                break
    if flag:
        print(A)

