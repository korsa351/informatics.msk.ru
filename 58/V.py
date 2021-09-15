chisl=[]
a=1
while a!=0:
    a=int(input())
    chisl.append(a)
chisl.sort()
if chisl[0]==0:
    print(chisl[1], chisl[-1])
elif chisl[-1]==0:
    print(chisl[0], chisl[-2])
else:
    print(chisl[0], chisl[-1])