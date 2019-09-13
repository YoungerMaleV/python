x=int(input())
grade=[]
credit=[]
a=0
b=0
for i in range (0,x):
    y=int(input())
    if y<60:
        grade.append(0)
    else:
      grade.append(4-3*(100-y)**2/1600)
for i in range (0,x):
    z=float(input())
    credit.append(z)
for i in range (0,x):
    a+=grade[i]*credit[i]
    b+=credit[i]
print('%.3f'%(a/b))
    




