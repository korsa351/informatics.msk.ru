import sys

x,y=map(float, input().split(" "))

if y>(x**2-2):
    if y<-x:
        print("YES")
        sys.exit()
    if y<x:
        print("YES")
        sys.exit()
    print("NO")
else:
    print("NO")
