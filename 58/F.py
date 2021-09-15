import random
a,b,n=map(int, input().split(" "))
for i in range(n):
    print(random.randint(a, b), end=" ")