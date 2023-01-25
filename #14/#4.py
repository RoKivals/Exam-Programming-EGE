x = 9**18 + 3**54 - 9

s = ''
while x:
    t = str(x % 3)
    s = t + s
    x //= 3

print(s.count('2'))