def divisors(n):
	D = []
	for i in range(1,n/2 + 1):
		if n%i == 0:
			D.append(i)
	return D
	
def divsum(n):
	return sum(divisors(n))

def amicableNums(n):
	A = []
	for a in range(1,n):
		b = divsum(a)
		if divsum(b) == a and a != b:
			A.append(a)
			#if b < n:
				#A.append(b)
	return set(A)


T = int(raw_input())

for i in range(T):
	N = int(raw_input())
	print sum(amicableNums(N))
	