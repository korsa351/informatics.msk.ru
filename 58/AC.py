def simplenumbers(g, n):
    numbrs = []
    for x in range(g, n+1):
        f = 2
        while x % f != 0:
            f += 1
        if f == x:
            numbrs.append(x)
    return numbrs


a = int(input())
if a <= 1:
    print(0)
    exit()
perfect_numbers = []
Array_simple_numbers = simplenumbers(2, 100)
for i in Array_simple_numbers:
    perfect_number = 2**(i-1)*(2**i-1)
    if perfect_number <= a:
        perfect_numbers.append(perfect_number)
    else:
        pass
if perfect_numbers:
    print(*perfect_numbers)
else:
    print(0)
