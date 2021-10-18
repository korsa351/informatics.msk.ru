N = int(input())

D = [d for d in range(1, N // 2 + 1) if N % d == 0]
if N == sum(D):
    print(*D)
else:
    print(0)
