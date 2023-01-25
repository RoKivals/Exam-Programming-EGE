import itertools as it

prod = it.permutations("ЛЕВИЙ")
count = 0
for i in prod:
    if i[0] != 'Й' and 'ЕИ' not in ''.join(i):
        count += 1


print(count)
