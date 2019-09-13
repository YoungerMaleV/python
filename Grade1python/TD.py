import math
a=0
b=int(input())
for i in range(1,b+1):
    a=a+int(input())
if (48-a)/(15-b)>10:
    print('gg')
else: 
     c=(48-a)/(15-b)
     d=math.ceil(c)
     print(d)
