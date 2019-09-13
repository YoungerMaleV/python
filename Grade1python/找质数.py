for n in range(2,10):
    for x in range(2,n):
        if n %x ==0:
            #找到n的一个因数
            break
        else:
            #遍历完毕未找到n的因式完成循环，即n为质数
            print(n)
