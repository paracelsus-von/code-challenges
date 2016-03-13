import math

def isPrime(n):
	if n ==2 or n ==3:
		return True
	elif n < 2 or n%2 == 0:
		return False
	elif n < 9:
		return True
	elif n%3 == 0:
		return False
	root = int(n**0.5)
	factor = 5
	while factor <= root:
		if n%factor == 0 or n%(factor + 2) == 0:
			return False
		f += 6
	return True

def largPrimeFactor(n):
	while n%2 == 0 and n/2 != 1:
		n /= 2
	for j in xrange(3, int(n**0.5) + 1, 2):
		while n%j == 0 and n/j !=1:
			n /= j
	return n

	
T = int(raw_input())

for i in range(T):
	n = int(raw_input())
	print largPrimeFactor(n)