n=int(input())
a=list()
b=list()
for i in range(0,n):
    y1,y2,y3=input().split(' ')
    y1=int(y1)
    y2=int(y2)
    y3=int(y3)
    Y=y1+y2+y3
    c=[i+1,Y,y1]
    a.append(c)
b.append(a[0])
for j in range(1,n):
    d=len(b)
    e=0
    for k in range(0,d):
        if a[j][1]>b[k][1]:
            e=1
            b.insert(k,a[j])
            break
        elif a[j][1]==b[k][1]:
            if a[j][2]>b[k][2]:
                e=1
                b.insert(k,a[j])
                break
            else:
                continue
        if e==0:
            b.append(a[j])
for i in range(0,5):
    f=b[i][0]
    g=b[i][1]
    print(str(f)+' '+str(g))
