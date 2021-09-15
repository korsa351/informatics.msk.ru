a,b,c=map(int,input().split(' '))
if a==b and b==c and a==c:
    print(0)
elif a==b and a>c:
    print("A", "B")
elif a==c and a>b:
    print("A", "C")
elif b==c and b>a:
    print("B", "C")
elif a>b and a>c:
    print("A")
elif b>a and b>c:
    print("B")
elif c>a and c>b:
    print("C")