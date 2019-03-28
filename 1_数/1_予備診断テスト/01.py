# 1 次の数のうち、素数はどれか。
I = [47, 75, 109, 83]

def IsPrimeNumber(n):
	for d in range(2, n-1):
		if n % d == 0:
			return False
	return True

for i, v in enumerate(I):
	print("%3d" % v, ":", IsPrimeNumber(v))
