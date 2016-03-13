def prod(elements):
	"""Returns the product of elements"""
	p = 1
	for i in elements:
		p *= i
	return p

def largestConsecProd(N, n, k):
	"""Returns the largest product of k consecutive digits
	in the n digit long number N."""
	A = []
	for i in range(n):
		digit = (N / (10 ** (n - 1 - i))) % 10
		A.append(digit)
	maxy = 0
	for j in range(n - k + 1):
		maxy = max(maxy, prod(A[j:j+k]))
	return maxy

T = int(raw_input())

for i in range(T):
	n,k = map(int, raw_input().strip().split())
	N = int(raw_input())
	print largestConsecProd(N, n, k)