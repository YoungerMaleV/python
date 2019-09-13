K=int(input())  #棱形行数是K，K是奇数
for i in range(1,K+1,2):
    print(('*'*i).center(K))
    



for i in range(K-2,0,-2):
    print(('*'*i).center(K))
