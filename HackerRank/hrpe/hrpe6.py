def sumSquares(n):
	"""Returns the sum of the squares of all integers <= n"""
	x = 0
	for i in range(n+1):
		x += i**2
	return x

def squareSums(n):
	"""Returns the square of the sum of the integers <= n."""
	x = 0
	for i in range(n+1):
		x += i
	x *= x
	return x

T = int(raw_input())

for i in range(T):
	N = int(raw_input())
	print abs(sumSquares(N) - squareSums(N))