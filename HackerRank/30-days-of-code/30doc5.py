T = int(raw_input())

for j in range(T):

	x = map(int, raw_input().split())

	a = x[0]
	b = x[1]
	N = x[2]

	A = []
	
	prev = a
	cur = 0

	for i in range(N):
		cur = prev + ((2**i)*b)
		A.append(cur)
		prev = cur
	
	print " ".join([str(m) for m in A])