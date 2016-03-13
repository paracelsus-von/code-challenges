A = []
 
for i in range (6):
	A.append(map(int, raw_input().strip().split()))

#print A

# Issue here
B = None

for k in range(4):
	for j in range(4):
		B = max(B,sum(A[k][j:j+3]) + A[k+1][j+1] + sum(A[k+2][j:j+3]))

print B