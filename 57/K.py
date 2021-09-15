import math
x,y=map(float, input().split(" "))
if y<=math.sin(x) and y<=0.5 and x>0 and y>=0 and x<math.pi:
    print('YES')
else:
    print('NO')