import sys

x,y=map(float, input().split(" "))

if x**2+y**2<1:
    if y>-x:
        print("YES")
        sys.exit()
    if y<x:
        print("YES")
        sys.exit()
    print("NO")
else:
    print("NO")