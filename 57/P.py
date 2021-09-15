import sys

x,y=map(float, input().split(" "))

if y>2*(x**2) and y>1-x and x<1:
    print("YES")
    sys.exit()

if x<1 and y>1-x and y<2*(x**2) and x>0:
    print("YES")
    sys.exit()

print("NO")