a,b=map(int, input().split(" "))
for i in range(a,(b+1)):
    y=0
    c=str(i)
    for x in c:
        if int(x)==0:
            y+=100
        if int(x)!=0:
            if i%int(x)==0 and int(x)!=0:
                y+=1
    if y==len(c):
        print(i,end=" ")