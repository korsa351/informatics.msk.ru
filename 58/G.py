a,b=map(int, input().split(" "))
c,d=map(int, input().split(" "))
n=0
for i in range (10000,100000):
    if ((i%a==b) and (i%c==d)):
        print(i,end=" ")
        n=10
if n==0:
    print('-1')