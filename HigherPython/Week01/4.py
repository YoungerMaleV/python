a=int(input("Plz input the basis number: "))
n=int(input("Plz input the longest length of number: "))
basis=a
s=0
for i in range(n):
    s=s+basis
    basis=basis*10+a
print('The total is %d' %s)