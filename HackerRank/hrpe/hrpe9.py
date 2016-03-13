def pythagTrips(n):
	"""Finds all Pythagorean Triplets a, b, c
	such that a + b + c = n."""
	x = -1
	for a in range(1, n/3):
		if (n**2 - 2*n*a) % (2 * (n-a)) != 0:
			continue
		b = (n**2 - 2*n*a)/(2 * (n-a))
		c = n - a - b
		x = max(x, a*b*c)
	return int(x)

T = int(raw_input())

for i in range(T):
	N = int(raw_input())
	print pythagTrips(N)