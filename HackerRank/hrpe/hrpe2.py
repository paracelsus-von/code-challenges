def fib(n):
	"""Returns the first n Fibonacci numbers"""
	A = []
	for i in range(n+1):
		if i < 1:
			continue
		elif i == 1:
			A.append(1)
		elif i == 2:
			A.append(1)
		else:
			A.append(A[-2] + A[-1])
	return A
		
def fibn(n):
	"""Returns the nth Fibonacci number"""
	return fib(n)[-1]

def fibLessN(n):
		A = [1, 1]
		while (A[-2] + A[-1]) <= n:
			A.append(A[-2] + A[-1])
		return A

def evenFibSum(n):
	"""Returns the sum of all the even Fibonacci numbers
		less than or equal to n"""
	return sum(fibLessN(n)[2::3])

T = int(raw_input())

for i in range(T):
	N = int(raw_input())
	#print evenFibSum(N)
	x = 0
	B = fibLessN(N)
	for b in B:
		if b%2 == 0:
			x += b
	print x