import math

a=int(input())
count = []


for el in range(1, math.ceil(a/2)+1):
    if a % el == 0:
        count.append(el)
    if sum(count) >= a:
        break


if sum(count) == a:
    count=sorted(count)
    print(' '.join(list(map(str, count))))
else:
    print(0)