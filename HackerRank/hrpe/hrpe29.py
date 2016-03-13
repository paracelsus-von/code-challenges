def distinctPowerlist(n):
	L = []
	for a in range(2,n+1):
		for b in range(2,n+1):
			L.append(a**b)
	return set(L)

N = int(raw_input())

print len(distinctPowerlist(N))