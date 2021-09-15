import random

a,b=map(float,input().split(' '))
for i in range(5):
    print('%.3f' % (random.uniform(a,b)), end=" ")