def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


a = int(input())
perfect_numbers = []
if a <= 5:
    print(0)
    exit()
for i in range(2, 101):
    if IsPrime(2**i-1):
        perfect_number = 2**(i-1)*(2**i-1)
        if perfect_number <= a:
            perfect_numbers.append(perfect_number)
        else:
            break
if perfect_numbers:
    print(*perfect_numbers)
else:
    print(0)
