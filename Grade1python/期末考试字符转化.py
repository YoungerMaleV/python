a=list(input())
b=len(a)
if ord(a[0])>96:
    print(a[0].upper(),end="")
if ord(a[0])<97:
    print(a[0],end="")
for i in range(1,b):
    if a[i]=='i':
        c=i
        if a[c+1]==' ':
            print(a[c].upper(), end="")
        if a[c-1]==',' and a[c+1]==',':
            print(a[c].upper(), end="")
        else:
            print(a[c],end="")
    if a[i]=='I':
        c=i
        if a[c+1]!=' ':
            print(a[c].lower(), end="")
        else:
            print(a[c],end="")
    if ord(a[i])<97 and ord(a[i])>64 and a[i]!='I':
        d= ord(a[i]) - ord('A') + ord('a')
        print(chr(d),end="") #将大写字母转化为小写
    else:
        print(a[i],end="")
