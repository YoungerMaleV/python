import datetime
def shuju():
    f1 = open('tianqi.txt','r')
    a=[]
    for line in f1:
        a=line.split()
        tian[a[0]]=[]
        tian[a[0]].append(a[1])
        tian[a[0]].append(a[2])
        tian[a[0]].append(a[3])
        tian[a[0]].append(a[4])
        tian[a[0]].append(a[5])
        tian[a[0]].append(a[6])
        tian[a[0]].append(a[7])
        tian[a[0]].append(a[8])
    f1.close()
tian={}
shuju()
print(tian)
