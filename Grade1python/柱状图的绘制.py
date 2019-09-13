
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
shuju=[[u'A组数据',96,67,89,65],[u'B组数据',56,37,59,64],[u'C组数据',78,89,67,5],
       [u'D组数据',87,47,37,24],[u'E组数据',78,36,34,76],[u'F组数据',56,49,76,87],
       [u'G组数据',86,32,23,34],[u'H组数据',65,25,27,65],[u'I组数据',52,97,75,24]]
ind=np.arange(9)
shuju1Mean=(96,56,78,87,78,56,86,65,52)
shuju2Mean=(67,37,89,47,36,49,32,25,97)
shuju3Mean=(89,59,67,37,34,76,23,27,75)
shuju4Mean=(65,64,45,24,76,87,34,65,24)
width=0.23
fig,ax=plt.subplots()
rects1=ax.bar(ind,shuju1Mean,width,color='blue')
rects2=ax.bar(ind+width,shuju2Mean,width,color='yellow')
rects3=ax.bar(ind+2*width,shuju3Mean,width,color='green')
rects4=ax.bar(ind+3*width,shuju4Mean,width,color='red')
ax.legend((rects1[0],rects2[0],rects3[0],rects4[0]),(u'附加数据1',u'附加数据2',u'附加数据3',u'附加数据4'))
def autolabel(rects):
    for rect in rects:
        height=rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.,1.05*height,'%d'%int(height),ha='center',va='bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
ax.set_ylabel(u'数值')
ax.set_title(u'数据分析表')
ax.set_xticks(ind+width)
ax.set_xticklabels((u'A组数据',u'B组数据',u'C组数据',u'D组数据',u'E组数据',u'F组数据',u'G组数据',u'H组数据',u'I组数据'))
plt.show()
