n = int(input())
l=[]
r=[]
for i in range(n+1):
    l.append(0)
    r.append(0)
    a=input().split()
    l[i]=int(a[0])
    r[i]=int(a[1])

for i in range(n+1):
    for j in range(1,n):
        p=1
        for z in range(j):
            p=p*l[z]
        sum1=int(p/r[j])
        sum2=int(p*l[j]/r[j+1])
        
        b=l[j]
        l[j]=l[j+1]
        l[j+1]=b
            
        b=r[j]
        r[j]=r[j+1]
        r[j+1]=b
        p=1
        for z in range(j):
            p=p*l[z]
        sum3=int(p/r[j])
        sum4=int(p*l[j]/r[j+1])
        if max(sum3,sum4)>max(sum1,sum2):
            b=l[j]
            l[j]=l[j+1]
            l[j+1]=b
            
            b=r[j]
            r[j]=r[j+1]
            r[j+1]=b

list1=[]
for j in range(1,n+1):
        p=1
        for z in range(j):
            p=p*l[z] 
        list1.append(int(p/r[j]))

max1=0
for i in range(n):
    if max1<list1[i]:
        max1=list1[i]
print(max1)
