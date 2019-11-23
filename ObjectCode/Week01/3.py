import math
x,y,z=map(int,input().split())
def leapyear(x):
    return(x%4==0)
days=[0,31,28,31,30,31,30,31,31,30,31,30]
a=0
if leapyear(x):
    days[2]=days[2]+1
for i in range(y):
    a=a+days[i]
print('This is the %d day' %x,end=" ")
print('of %d' %(a+z))