x,y=map(float,input().split(" ")) 
if y>1: 
 a=0 
else: 
 a=1 
if x>0 and y>0: 
 b=0 
elif x>=0 and y<=0 and y<=-x: 
 b=1 
elif x<=0 and y>=0 and y<=-x: 
 b=1 
elif x<=0 and y<=0: 
 b=1 
else: 
 b=0 
j=(x**2+y**2) 
if j>=0 and j<=1: 
 c=1 
else: 
 c=0 
h=x-1 
k=h**2 
u=y**2 
if k+u>=0 and k+u<=1: 
 d=1 
else: 
 d=0 
print(a,b,c,d, sep="")