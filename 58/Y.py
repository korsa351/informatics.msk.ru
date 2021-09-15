n=str(input())
flag=True
for i in n:
    if flag==True:
        print(" " + i, end=" ")
        flag=False
    else:
        print(i, end=" ")