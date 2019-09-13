from tkinter import*
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']#使汉字表示出

def a1():        #计算每周的平均最高气温和平均最低气温，并给出每周天气的变化趋势图
    y1=(8,9,13,7,8,6,6,8,10,14,11,15,17,15,12,10,4,13,13,10,11,17,18,22,24,25,27,25,19,18,23,25,26,14,10,10,11,12,18,20,24,23)
    #2018-03-01到2018-04-11北京市最高气温（共42天）
    list1=[]
    for i in range(1,7):
        h=0
        for j in range(7*i-6,7*i+1):
            h=h+y1[j-1]
        p=h/7
        list1.append(p)#计算这42天每周的最高气温平均值
    y1=tuple(list1)
    x=('3-1~3-7','3-8~3-14','3-15~3-21','3-22~3-28','3-28~4-4','4-5~4-11')
    plt.plot(x,y1,'r-',linewidth=3,label='最高气温')
    y2=(-3,-1,3,-2,-3,-3,-2,-4,-2,-2,0,3,5,6,-1,-1,0,1,2,-2,1,4,5,5,7,7,11,9,7,8,9,11,11,6,1,3,4,2,5,7,8,9)
     #2018-03-01到2018-04-11北京市最低气温（共42天）
    list1=[]
    for i in range(1,7):
        h=0
        for j in range(7*i-6,7*i+1):
            h=h+y2[j-1]
        p=h/7
        list1.append(p)#计算这42天每周的最低气温平均值
    y2=tuple(list1)
    x=('3-1~3-7','3-8~3-14','3-15~3-21','3-22~3-28','3-28~4-4','4-5~4-11')
    plt.plot(x,y2,'g--',linewidth=3,label='最低气温')
    plt.ylim(-10,30)    #纵坐标天气温度的上，下限
    plt.xlabel('时间段')
    plt.ylabel('平均气温')
    plt.title('2018-03-01到2018-04-11北京市最高与最低气温变化图')
    plt.legend(['最高气温','最低气温'])
    plt.show()
def a2():#2018年3月1到2018年4月11每周的平均最高气温和平均最低气温，并绘制柱状图
    y1=(8,9,13,7,8,6,6,8,10,14,11,15,17,15,12,10,4,13,13,10,11,17,18,22,24,25,27,25,19,18,23,25,26,14,10,10,11,12,18,20,24,23)
    #2018-03-01到2018-04-11北京市最高气温（共42天）
    list1=[]
    for i in range(1,7):
        h=0
        for j in range(7*i-6,7*i+1):
            h=h+y1[j-1]
        p=h/7
        list1.append(p)#计算这42天每周的最高气温平均值
    y1=tuple(list1)
    y2=(-3,-1,3,-2,-3,-3,-2,-4,-2,-2,0,3,5,6,-1,-1,0,1,2,-2,1,4,5,5,7,7,11,9,7,8,9,11,11,6,1,3,4,2,5,7,8,9)
     #2018-03-01到2018-04-11北京市最低气温（共42天）
    list1=[]
    for i in range(1,7):
        h=0
        for j in range(7*i-6,7*i+1):
            h=h+y2[j-1]
        p=h/7
        list1.append(p)#计算这42天每周的最低气温平均值
    y2=tuple(list1)
    '''月最高平均气温=(15,20,24,29,33,35,31)#北京市3月至9月的月最高平均气温
    月最低平均气温=(10,16,18,24,28,27,25)#北京市3月至9月的月最低平均气温'''
    N=6
    ind=np.arange(N)
    width=0.35
    fig,ax=plt.subplots()
    rects1=ax.bar(ind, y1,width,color='r')
    rects2=ax.bar(ind+width, y2,width,color='b')
    ax.legend((rects1[0],rects2[0]),('月最高平均气温','月最低平均气温'))#设置图例
    ax.set_ylabel('周平均温度')
    ax.set_title('北京市2018年3月1到2018年4月11每周的平均最高气温和平均最低气温的柱状统计图')
    ax.set_xticks(ind+width)
    ax.set_xticklabels(('第一周','第二周','第三周','第四周','第五周','第六周'))
    plt.show()
def a3():#统计并判断每天空气质量指数所对应的空气质量等级，用饼状图显示每个月以及全部时间范围内空气质量等级的相对比例
    data=(21,55,16,24,64,12,8,13,7,14,34,25,16,14,24,22,13,34,55,16,11,12,42,45,74,11,9,48,88,62,12,33,31,22,61)#某35天北京市空气质量的数据
    BEST,GOOD=0,0
    for i in data:
        if i<=50:
            BEST=BEST+1
        else:
            GOOD=GOOD+1
    sizes=BEST,GOOD
    labels=[u'优',u'良']
    colors=['r','b']
    pie=plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=-90)#绘制饼图
    plt.show()

top = Tk()#创建一个顶层窗口
top.title('2018-03-01到2018-04-11北京市气象变化（共42天）')
photo=PhotoImage(file="beijing.png")
label_image=Label(top,image=photo)
label = Label(top,text='请根据您的需求进行咨询')
button1 = Button(top, text='搜索北京市周平均最高气温与最低气温变化', command = a1)#使用command将菜单项与回调函数相关联，当用户点击该菜单项时将自动调用该函数
button2 = Button(top, text='搜索北京市月平均最高与最低气温的柱状统计图', command = a2)
button3 = Button(top, text='搜索北京市42天空气质量饼状图', command = a3)
label_image.pack()#采用pack方法进行组件布局，默认在父窗口中自顶3向下添加组件
button1.pack()
button2.pack()
button3.pack()
top.mainloop()#主循环，通过他程序可以长期运行，以等待用户的输入和输出操作
