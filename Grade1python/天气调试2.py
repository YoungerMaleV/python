from tkinter import*
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
mpl.rcParams['font.sans-serif']=['FangSong']
mpl.rcParams['axes.unicode_minus']=False


plt.xlim(1,5)
plt.ylim(-20,35)
y=(19,25,16,34,25,16,26,31,29,18,24,15,33,28,22,26,33,31,28,27,26,31,33,34,35,29,32,31,30,21,24,26,25,19,24)
   
list0=[]
n=0
for i in range(1,6):
    h=0
    for j in range(7*i-6,7*i+1):
        h=h+y[j-1]
    p=h/7
    p=int(p)
    list0.append(p)
y=list0
x=(1,2,3,4,5)
plt.plot(x,y)

    
y=(-6,-2,-5,-1,-2,-3,0,2,1,5,3,-1,-2,-3,-4,-5,-9,-6,-1,-2,0,0,0,0,-1,2,4,-2,-3,1,2,0,0,1,3)

list0=[]
n=0
for i in range(1,6):
    h=0
    for j in range(7*i-6,7*i+1):
        h=h+y[j-1]
    p=h/7
    p=int(p)
    list0.append(p)
y=list0
x=(1,2,3,4,5)
plt.plot(x,y)

plt.show()
