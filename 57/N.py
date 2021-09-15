x,y=map(float, input().split(" "))
if x*x+y*y<=1 and y>x:
    print('YES')
elif x*x+y*y<=1 and y<=0 and x<=0:
    print('YES')
else:
    print('NO')