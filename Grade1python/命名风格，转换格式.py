m = input()
n = list(m)
fir=0
for i in range(len(n)) :
	if n[i] >= 'A' and n[i] <= 'Z' :
		if (fir == 0) :
			fir = 1
			l = ord(n[i]) - ord('A') + ord('a')
			print(chr(l), end = "")
		else :
			print("_", end = "")
			l = ord(n[i]) - ord('A') + ord('a')
			print(chr(l), end = "")
	else :
		print(n[i], end = "")
