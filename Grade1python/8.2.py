from tkinter import *
import math
import random
from scipy import stats
from scipy.interpolate import spline

root = Tk()
root.title('统计')
root.geometry('1200x300')

x11=StringVar()
x12=StringVar()
x21=StringVar()
x22=StringVar()
x23=StringVar()

x11_entry=Entry(root,width=20,textvariable=x11)
x11_entry.place(x=260,y=20,anchor=CENTER)
x12_entry=Entry(root,width=20,textvariable=x12)
x12_entry.place(x=1100,y=20,anchor=CENTER)
x21_entry=Entry(root,width=20,textvariable=x21)
x21_entry.place(x=260,y=40,anchor=CENTER)
x22_entry=Entry(root,width=20,textvariable=x22)
x22_entry.place(x=680,y=40,anchor=CENTER)
x23_entry=Entry(root,width=20,textvariable=x23)
x23_entry.place(x=1100,y=40,anchor=CENTER)

Label(text='泊松分布样本大小').place(x=80,y=20,anchor=CENTER)
Label(text='泊松分布λ').place(x=920,y=20,anchor=CENTER)
Label(text='正态分布样本大小').place(x=80,y=40,anchor=CENTER)
Label(text='正态分布μ').place(x=500,y=40,anchor=CENTER)
Label(text='正态分布σ').place(x=920,y=40,anchor=CENTER)

Button(text='生成并统计',command=lambda:sheng()).place(x=574,y=66,anchor=CENTER)    

Label(text='泊松分布样本').place(x=230,y=92,anchor=CENTER)
Label(text='正态分布样本').place(x=900,y=92,anchor=CENTER)
textbox1= Text(root,width=100,height=13.4)
textbox2= Text(root,width=100,height=13.4)
textbox1.place(x=350,y=192,anchor=CENTER)
textbox2.place(x=950,y=192,anchor=CENTER)
Label(text='λ-0.5插值为：').place(x=70,y=290,anchor=CENTER)
Label(text='λ+1.5插值为：').place(x=400,y=290,anchor=CENTER)
def poisson(a):
    k=0
    p=math.exp(-a)
    s=p
    u=random.random()
    if u<=math.exp(-a):
        return 0
    else:
        while u>s:
            p=a*p/(k+1)
            s=s+p
            k=k+1
        return k-1

def pin(a,d):
    if d in a:
        a[d]+=1
    else:
        a[d]=1

def sheng():
    bo1=int(x11.get())
    bo2=int(x12.get())
    zheng1=int(x21.get())
    zheng2=int(x22.get())
    zheng3=int(x23.get())
    zheng=stats.norm(loc=zheng2,scale=zheng3)
    chu=zheng.rvs(size=zheng1)
    for i in range (zheng1):
        textbox2.insert(INSERT,'%-10d'%(int(chu[i])))
        if i%5==4:
            textbox2.insert(INSERT,'\n')
    tong={}
    for i in range (bo1):
        flag=poisson(bo2)
        textbox1.insert(INSERT,'%-10d'%(flag))
        if i%5==4:
            textbox1.insert(INSERT,'\n')
        pin(tong,flag)
    key=list(tong.keys())
    zhi=list(tong.values())
    zhi=list(map(lambda x: float(x/bo1),zhi))
    Label(text='%.6f'%spline(key,zhi,bo2-0.5)).place(x=140,y=290,anchor=CENTER)
    Label(text='%.6f'%spline(key,zhi,bo2+1.5)).place(x=470,y=290,anchor=CENTER)
    
    
        


    
    
