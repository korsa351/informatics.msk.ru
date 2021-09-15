a=int(input())
flag=False
a1=str(a)
for i in range(1,10):
    if a1.find(str(i))!=a1.rfind(str(i)):
        print('YES')
        flag=True
        break
if a1.find('0')!=a1.rfind('0'):
    print('YES')
    flag=True

if flag==False:
    print('NO')