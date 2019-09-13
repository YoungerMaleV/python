n = int(input())
b = list()

for i in range(0,n):
    c = input()
    b.append(c)
    
l = [[0 for m in range(0,n)] for p in range(0,n)]
flag = 0

for m in range(n-2,-1,-1):
    for p in range(1,n):
        if ord(b[m][p]) == 45 and ord(b[m+1][p])== 45 and ord(b[m][p-1])== 45:
            l[m][p] = 2
            if l[m+1][p] >= 1 and l[m][p-1]>= 1:
                l[m][p] = min (l[m+1][p],l[m][p-1])+1
                if l[m][p] > flag:
                    flag = l[m][p]
print(flag)
