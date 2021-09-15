x,y=map(float, input().split(" "))
if x<=2 and y>=0 and y<=x and x*x+y*y>=4:
    print('YES')
else:
    print('NO')