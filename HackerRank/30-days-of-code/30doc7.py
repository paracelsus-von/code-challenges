# prints input in reverse order

N = int(raw_input().strip())
A = map(int, raw_input().strip().split( ))

B = []

for i in range(N):
	B.append(A[N-(i+1)])

print " ".join([str(b) for b in B])