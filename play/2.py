x=int(input()) #输入待分解的的合式，不超过1000
#判断x能否分解
while(x!=1):
    for i in range(2,x+1):
     if x%i==0:
            print(i,end="")
            if i!=x:
                 print(" *",end=" ")
            x=int(x/i)
            break
