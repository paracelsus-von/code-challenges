def numRATris(p):
	"""Finds the number of right angled triangles, ie with distinct
	sets of side lengths, for a given perimeter p."""
	total = 0
	for a in range(1,p/3):
		b = ((p - a)**2 - a**2)/(2*(p - a))
		if a + b + (a**2 + b**2)**0.5 == p:
			total += 1
	return total

T = int(raw_input())

for i in range(T):
	N = int(raw_input())
	currmax = None
	for i in range(1,N+1):
		if numRATris(i) > currmax:
			result = i
			currmax = numRATris(i)
	print result