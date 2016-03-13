def prod(elements):
	"""Returns the product of elements"""
	p = 1
	for i in elements:
		p *= i
	return p


A = []
for x in range(20):
	A.append(map(int, raw_input().strip().split()))

currmax = None
for i in range(20):
	for j in range(17):
		# rows
		currmax = max(currmax, prod(A[i][j:j+4]))
		# columns
		currmax = max(currmax, prod([A[j][i], A[j+1][i], A[j+2][i], A[j+3][i]]))
		if i < 17:
			# diag right down
			currmax = max(currmax, prod([A[i][j], A[i+1][j+1], A[i+2][j+2], A[i+3][j+3]]))
			# diag right up
			currmax = max(currmax, prod([A[i+3][j], A[i+2][j+1], A[i+1][j+2], A[i][j+3]]))

print currmax