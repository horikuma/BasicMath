# 2 次の各数の素因数を見いだせ。
I = [150, 186, 2048, 735]

def IsPrimeNumber(n):
	for d in range(2, n-1):
		if n % d == 0:
			return False
	return True

for i in I:
	pn = []
	for x in range(2, i + 1):
		if i % x == 0 and IsPrimeNumber(x):
			pn.append(x)
	print("%4d" % i, ":", *pn)
