import math
import random
from scipy import stats
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
print('Poisson distribution:')

for i in range(8):
     x=poisson(8)
     print(x,end=' ')
print('')
print('')
print('Normal distrubution:')
print('Number of elements:10')
print('Elements:')
a=stats.norm(loc=0,scale=1)
b=a.rvs(size=10)
print(b)
print('Minimum:%.5f Maximum:%.5f'%(stats.describe(b).minmax[0],stats.describe(b).minmax[1]))
print('Mean:%.5f'%stats.describe(b).mean)
print('Variance:%.5f'%stats.describe(b).variance)
print('Skewness:%.5f'%stats.describe(b).skewness)
print('Kurtosis:%.5f'%stats.describe(b).kurtosis)
