def q(n,m):
    if n==1 or m==1:
        return 1
    if n<m:
        return q(n,n)
    if n==m:
        return 1+q(n,n-1)
    if n>m>1:
        return q(n,m-1)+q(n-m,m)
n=int(input())
m=n
print(q(n,m))
