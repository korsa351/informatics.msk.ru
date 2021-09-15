import random

a,b=map(int,input().split(' '))
for i in range(5):
    print(random.randint(a,b), end=" ")