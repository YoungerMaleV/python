n=int(input())
while (n!=1):
    if n%2!=0:
       n=3*n+1
       print(int(n))
    else:
        n=n/2
        print(int(n))
