a=int(input())
if (a<=0) or (a>12):
    print('NO')
elif (a>=1) and (a<=2) or (a==12):
    print('winter')
elif (a>=3) and (a<=5):
    print('spring')
elif (a>=6) and (a<=8):
    print('summer')
else:
    print('autumn')