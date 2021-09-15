import math
flag=0
stp=[]
a=int(input())
if a<4:
    print(0)
else:
    b=int(math.log2(a))
    for i in range(1,b+1):
        if i%2==0 and 2**i<=a:
            stp.append(2**i)
            flag+=1
if flag!=0:
    stp.reverse()
    for i in range(flag):
        print(stp[i], end=" ")