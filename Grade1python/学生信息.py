a = int(input())
dic = {} #构造字典
for i in range(a) :
	b = input()
	c = input()
	dic[b] = c
d = int(input())
for i in range(d) :
	b = input()
	answer = dic.get(b, "Not Found!")
	print(answer)
