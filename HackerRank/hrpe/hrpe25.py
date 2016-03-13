def fibNum(n):
	"""Returns the nth Fibonacci number."""
	return fibList(n)[-1]

def fibList(n):
	"""Returns the first n Fibonacci numbers."""
	if n == 1:
		return [1]
	if n == 2:
		return [1, 1]
	F = [1,1]
	for i in range(n-2):
		F.append(F[-1] + F[-2])
	return F

def numDigits(n):
	"""Returns the number of digits of n."""
	i = 1
	while n < 10**i and n < 10**(i+1):
		i += 1
	return i

def fibListSize(n):
	"""Returns the first Fibonacci number to be n digits long."""
	if n == 1:
		return 1
	if n == 2:
		return 13
	F = fibList(11)
	while numDigits(F[-1]) < n:
		F.append(F[-1] + F[-2])
	return F[-1]

T = int(raw_input())

for i in range(T):
	N = int(raw_input())
	
	print fibListSize(N)