a=int(input())
n=0
for i in range(a,0,-1):
    if (i%2==0):
        print(2**i, end=" ")
        n=10
if n==0:
    print('0')