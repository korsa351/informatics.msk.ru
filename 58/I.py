a,b=map(int, input().split(" "))
d=0
che=b+1
for i in range(a,che):
    ab=0
    c=str(i)
    s=len(c)
    st=int(s)
    for k in range(s):
        ad=c[k]
        ai=int(ad)
        ab+=(ai**st)
    if ab==i:
        print(i,end=" ")
        d=10
if d==0:
    print('-1')