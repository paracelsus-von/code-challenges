def prod(elements):
	p = 1
	for e in elements:
		p *= e
	return p

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
	return primeFactors(n)[-1]

def primeFactors(n):
	F = []
	while n%2 == 0 and n/2 != 1:
		n /= 2
		F.append(2)
	for j in xrange(3, int(n**0.5) + 1, 2):
		while n%j == 0 and n/j !=1:
			n /= j
			F.append(j)
	return set(F)


def primeList(n):
	P = [2,3]
	if n == 1:
		return [2]
	if n == 2:
		return [2,3]
	factor = 5
	while len(P) < n:
		if factor
	
def isPrime(n):
	if n ==1:
		return False
	if n == 2:
		return True
	if n ==3 or n ==5 or n ==7:
		return True
	if n%2 == 0:
		return False
	if n%3 == 0:
		return False
	root = int(n**0.5)
	for factor in range(5,root + 1,6):
		if n%factor == 0 or n%(factor + 2) == 0:
			return False
	return True

def rad(n):
	"""Returns the product of the distinct prime factors of n."""
	return prod(primeFactors(n))

def rabchit(r,a,b,c):
	if gcd(a,b) <> 1 or gcd(a,c) <> 1 or gcd(b,c) <> 1:
		return False
	if a > b:
		return False
	if a + b <> c:
		return False
	if rad(a*b*c) >= c**r:
		return False
	return True
	