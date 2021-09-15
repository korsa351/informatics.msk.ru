a,b=map(int, input().split(" "))
c=b+1
d=0
for i in range(a,c):
    k=str(i)
    l=len(k)
    if((i**2)%(10**l)==i):
        print(i, end=" ")
        d=10
if d==0:
    print('-1')