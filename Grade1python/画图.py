import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(8,6))
x=np.linspace(1.0,10.0)
y1=np.sin(1/x)
y2=np.log(x)
z1=plt.plot(x,y1,'r-',linewidth=3,label='sin(1/x)')
z2=plt.plot(x,y2,'g--',linewidth=3,label='log(x)')
plt.xlim(1,10)
plt.ylim(-1.2,4.5)
plt.xlabel('Time(s)')
plt.title('volt')
plt.ylabel('CHT figure')
plt.legend(['sin(1/x)','log(x)'])
plt.show()

