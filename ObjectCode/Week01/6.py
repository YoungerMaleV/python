def encrypt(str0):
    s=list(str0)
    a=[0,0,0,0]
    for i in range (len(str0)):
        a[3-i]=(int(s[i])+5)%10
    print('The New number is:',end=" ")
    for i in range(len(a)):
        print(a[i],end=" ")
    return a

def decrypt(intzu):
    c=[0,0,0,0]
    d=[0,0,0,0]
    for i in range (len(intzu)):
        c[i]=intzu[3-i]
    for i in range (len(c)):
        if c[i]<5:
            d[i]=int(c[i])+5
        else:
            d[i]=int(c[i])-5
    for i in range(len(d)):
        print(d[i],end=" ")
        
tel=input("Plz input the four-digit integer:")
sec=encrypt(tel)
print("\nIf you want to decrpt the Ciphertext ,Plz input 1")
b=int(input())
if b==1:
    decrypt(sec)
else:
    print('Over')
