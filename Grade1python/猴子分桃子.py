n=int(input())
ai=[]
bi=[]
a,b=map(int,input().split())
for i in range(n):
    c,d=map(int,input().split())
    ai.append(c)
    bi.append(d)
for i in range(n):
    e=0
    for j in range(i+1,n):
        if ai[i]*bi[i]>ai[j]*bi[j]:
              c=ai[i]
              ai[i]=ai[j]
              ai[j]=c
              c=bi[i]
              bi[i]=bi[j]
              bi[j]=c
              e=1
        if e==0:
            break
m=int(0)
for i in range(n):
    if int(a/bi[i])>m:
        m=int(a/bi[i])
    a=a*ai[i]
print(m)
