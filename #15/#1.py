for A in range(1000):
    flag = True
    for x in range(1000):
        if not ((x & 29 == 0) or (x & 17 != 0 or x & A != 0)):
            flag = False
            break
    if flag:
        print(A)
        break
