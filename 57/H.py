import sys

a,b=map(int, input().split(" "))
if (a<1) or (a>12):
    print(-1)

if a==2 and b>28:
    print(-1)
    sys.exit()

if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    if b<1 or b>31:
        print(-1)
        sys.exit()

if a==4 or a==6 or a==9 or a==11:
    if b<1 or b>30:
        print(-1)
        sys.exit()

if a==1:
    print(365-b)

if a==2:
    print(365-31-b)

if a==3:
    print(365-31-28-b)

if a==4:
    print(365-31-28-31-b)

if a==5:
    print(365-31-28-31-30-b)

if a==6:
    print(365-31-28-31-30-31-b)

if a==7:
    print(365-31-28-31-30-31-30-b)

if a==8:
    print(365-31-28-31-30-31-30-31-b)

if a==9:
    print(365-31-28-31-30-31-30-31-31-b)

if a==10:
    print(365-31-28-31-30-31-30-31-31-30-b)

if a==11:
    print(365-31-28-31-30-31-30-31-31-30-31-b)

if a==12:
    print(365-31-28-31-30-31-30-31-31-30-31-30-b)