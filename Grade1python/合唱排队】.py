N=int(input())
a=input().split()
list1=[]
list2=[]
for i in range(N):
    a[i]=int(a[i])
    list1.append(0)
    list2.append(0)
for i in range(N):
    list1[i]=1
    for j in range(i):
        if a[i]>a[j]:
            list1[i]=max(list1[i],list1[j]+1)

for i in range(N):
    list2[N-1-i]=1
    for j in range(N-i,N):
        if a[N-1-i]>a[N-1+N-i-j]:
            list2[N-1-i]=max(list2[N-1-i],list2[N-1+N-i-j]+1)

m=1
for i in range(N):
    if m<list1[i]+list2[i]:
        m=list1[i]+list2[i]
print(N-m+1)
