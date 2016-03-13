def R(k):
	x = 0
	for i in range(k):
		x += 10**i
	return x

def A(n):
	k = 1
	i = 1
	while k%n != 0:
		k = 10*k + 1
		i += 1
	return i

	
T = int(raw_input())

for t in range(T):
	N = int(raw_input())
	print A(N)