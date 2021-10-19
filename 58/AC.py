a = int(input())
total = []
for i in range(1, a+1):
    D = [d for d in range(1, i // 2 + 1) if i % d == 0]
    if sum(D) == i:
        total.append(i)
if total:
    print(*total)
else:
    print(0)
