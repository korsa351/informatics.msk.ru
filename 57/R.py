import sys

x,y=map(float, input().split(" "))

if x**2+y**2<=1:
    print("YES")
    sys.exit()

if x**2+y**2>1 and y<1 and x>0 and x<1 and y>0:
    print("YES")
    sys.exit()

print("NO")