x,y=map(float,input().split(" "))
xi,yi=map(float,input().split(" "))
r=((xi-x)**2)+((yi-y)**2)
print('%.03f'%r**(1/2))