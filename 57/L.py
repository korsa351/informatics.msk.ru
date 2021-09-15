x,y=map(float, input().split(" "))
if y<2-x*x and y>x or x>0 and y<x and y<2-x*x and y>0:
    print('YES')
else:
    print('NO')