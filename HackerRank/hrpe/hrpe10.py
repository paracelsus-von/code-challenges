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

def nPrimes(n):
	"""Returns the first n primes."""
	A = [2]
	i = 3
	while len(A) < n:
		for a in A:
			if i%a == 0:
				counter = 0
				break
			else:
				counter = 1
		if counter == 1:
			A.append(i)
		i += 2
	return A

def extendPrimesList(currprimes, n):
	i = currprimes[-1] + 2
	while i <= n:
		checklist = []
		for a in currprimes:
			if a <= n**0.5:
				checklist.append(a)
		for a in checklist:
			if i%a == 0:
				counter = 0
				break
			else:
				counter = 1
		if counter == 1:
			currprimes.append(i)
		i += 2
	return currprimes

def primeSums(n):
	

T = int(raw_input())

N = int(raw_input())
primeslist = primeList(N+1)
print sum(primeslist)

for i in range(T-1):
	N = int(raw_input())
	if N <= primeslist[-1]:
		for index, element in enumerate(primeslist):
			if primeslist[index+1] > N:
				print sum(primeslist[0:index+1])
	else:
		primeslist = extendPrimesList(primeslist, N)
		print sum(primeslist)