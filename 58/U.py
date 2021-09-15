chisl=[]
a=1
while a!=0:
    a=int(input())
    chisl.append(a)
chisl=chisl[:len(chisl)-1]
sum1=0 
proizv=1
for i in range(len(chisl)):
    sum1+=chisl[i]
    proizv*=chisl[i]
print(sum1, proizv)