def primeList(n):
	"""Returns the list of primes less than n"""
	A = []
	for i in range(n):
		if isPrime(i):
			A.append(i)
	return A

def isPrime(n):
	"""Returns if a number is prime."""
	if n < 2:
		return False
	if n == 2 or n == 3:
		return True
	if n%2 == 0 or n %3 == 0:
		return False
	if n < 10:
		return True
	root = int(n ** 0.5)
	factor = 5
	while factor <= root:
		if n%factor == 0 or n%(factor + 2) == 0:
			return false
		f += 6
	return True

def prod(elements):
	"""Returns the product of elements"""
	p = 1
	for i in elements:
		p *= i
	return p

def smallestMult(n):
	"""Returns the smallest number that is a multiple
	of all numbers <= n."""
	primes = primeList(n + 1)
	root = n ** 0.5
	less = []
	more = []
	for x in primes:
		if x <= root:
			less.append(x)
		else:
			more.append(x)
	for index, element in enumerate(less):
		temp = element
		while (less[index] * temp) <= n:
			less[index] *= temp
	product = prod(less) * prod(more)
	return product
	
	

T = int(raw_input())

for i in range(T):
	N = int(raw_input())
	print smallestMult(N)
	