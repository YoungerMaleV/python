class Matrix:
    def __init__(self):  # 建立一个4x4的零矩阵
          self.items=[
                [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
              ]



    def get_pos(self, x, y):
         return self.items[x-1][y-1]


    def set_pos(self, x, y, value):
         self.items[x-1][y-1] = value


    def initialize(self, matlist):  #矩阵初始化
       for a in range (0,4):
           for b in range (0,4):
               self.items[a][b]=matlist[a][b]


    def output(self):  # 输出矩阵
        for c1 in range(1,5):
            print('|', end='')
            for c2 in range(1,5):
                print("%5d" % self.get_pos(c1, c2), end='')
            print('    |')


    def trans(self):  # 求转置矩阵
        trans = Matrix()
        for d1 in range(1, 5):
            for d2 in range(1, 5):
                trans.set_pos(d2, d1, self.get_pos(d1, d2))
        return trans


    def plus(self, m2):  # 矩阵相加
        res = Matrix()
        for o in range(1, 5):  # 矩阵行数
            for p in range(1, 5):  # 矩阵列数
                q = self.get_pos(o, p) + m2.get_pos(o, p)
                res.set_pos(o, p, q)
        return res


    def multiply(self, m2):# 矩阵相乘
        res=Matrix()
        for hang in range (0,4):
            for lie in range (0,4):
                zong=0
                for flag in range (0,4):
                    zong+=self.get_pos(hang,flag)* m2.get_pos(flag,lie)
                    res.set_pos(hang,lie,zong)
        return res

'''
参考输入测试数据：
1 0 0 0
0 1 0 1
0 1 0 0
0 0 1 0
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''

if True:  # 以下为主程序
    N = 4  # 方阵阶数
    array1 = []
    array2 = []
    for i1 in range(0, N):
        array1.append([])
        array1[i1] = input().split()
        for i2 in range(0, N):
            array1[i1][i2] = int(array1[i1][i2])

    for j1 in range(0, N):
        array2.append([])
        array2[j1] = input().split()
        for j2 in range(0, N):
            array2[j1][j2] = int(array2[j1][j2])

    x = Matrix()
    print("x before initialization:")
    x.output()
    x.initialize(array1)
    print("x after initialization:")
    x.output()
    y = Matrix()
    y.initialize(array2)
    print("y after initialization:")
    y.output()
    print()

    del array1
    del array2

    xT = x.trans()
    print("Transpose x is:")
    xT.output()
    print("Transpose y is:")
    y.trans().output()
    print("Transpose x+y is:")
    z = x.plus(y).trans()
    z.output()
    print("x*y is:")
    w = x.multiply(y)
    w.output()
