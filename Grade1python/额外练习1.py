x=list(input())
list1=[]
list2=[]
list3=[]
n=len(x)
for i in range(0,n):
    if ord(x[i])>96:
        list1.append(x[i])
    if ord(x[i])>47 and ord(x[i])<58:
        list2.append(x[i])
    if ord(x[i])<97 and ord(x[i])>64:
        list3.append(x[i])
n1=len(list1)
n2=len(list2)
n3=len(list3)
n4=n-n1-n2-n3
print(n2)
print(n3)
print(n1)
print(n4)

