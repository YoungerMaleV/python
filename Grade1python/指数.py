import math
a, b = input().split()
a = int(a)
b = int(b)
tar = [0] * 1000005
ans = 0
tar[1] = 1
for i in range (2, b+1	) :
	if tar[i] == 0 :
		k = math.ceil(b/i)
		for j in range (i, k+1) :
			tar[i*j] = 1
for i in range (a, b+1) :
	if (tar[i] == 0) :
		ans = ans + i
print(ans, end = "")
