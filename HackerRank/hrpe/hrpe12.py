def numDivs(n):
	"""Calculates the number of divisors a number has."""
	num = 0
	x = n/2
	if n == 1:
		return 1
	num = 2
	# 1 and itself
	for i in range(2,n/2):
		if i == x:
			return num
		#if you get back to something already counted, you kill the process
		if n%i == 0:
			if n/i == i:
				num += 1
			# so you don't double count squares
			else:
				num += 2
			x = n/i
			# the i and the thing it multiplies by to get n
	return num
	# Plus two for the number dividing itself and one dividing it

def calcTriNums(n):
	"""Calculates the first n Triangular Numbers."""
	A = [1]
	i = 2
	while len(A) < n:
		A.append(A[i-2] + i)
		i += 1
	return A
	
T = int(raw_input())

trinums = calcTriNums(1000000)

for i in range(T):
	N = int(raw_input())
	for j in range(len(trinums)):
		if numDivs(trinums[j]) > N:
			print trinums[j]
			break
