a=int(input())
a1=str(a)
y=0
for i in range(1,len(a1)):
    if a1[i]==a1[i-1]:
        print('YES')
        y+=1
        break
if y==0:
    print('NO')