a,b=map(int, input().split(" "))
chet=0
while (a!=0) and (b!=0):
    if a>=b:
        a=a-b
        chet+=1
    elif b>=a:
        b=b-a
        chet+=1
if a==0:
    print(b,chet)
if b==0:
    print(a,chet)