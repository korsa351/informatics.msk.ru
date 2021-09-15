a=int(input())
b=str(a)
c=len(b)
chet=0
for i in range(c):
    ad=b[i]
    g=int(ad)
    if g%2==0:
        chet+=1
print(chet)