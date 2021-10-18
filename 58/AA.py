import sys


def simplenumber(g, n):
    numbrs = []
    for x in range(g, n+1):
        f = 2
        while x % f != 0:
            f += 1
        if f == x:
            numbrs.append(x)
    return numbrs


a, b = map(int, input().split(" "))
if a == 1 and b == 2:
    print(2)
else:
    lst = simplenumber(a, b)
    if not lst:
        print(0)
        sys.exit()
    for c in lst:
        print(c, end=" ")
