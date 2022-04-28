def f():
    for i in range(n // a + 1):
        for j in range(n // b + 1):
            r = n - (i * a + j * b)
            if r >= 0 and r % c == 0:
                yield i, j, r // c


a, b, c, n = map(int, input().split())
result = list(f())
print(len(result))
for row in result:
    print(*row)
