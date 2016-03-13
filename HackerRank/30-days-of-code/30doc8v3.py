import sys

Q = []

for line in sys.stdin:
	Q.append(line.strip())

N = int(Q[0])

R = Q[2*N+1::]
del Q[2*N+1::]
del Q[0]

for r in R:
	flag = 0

	for j in range(N*2 - 1)[0::2]:
		if r == Q[j]:
			print Q[j] + '=' + Q[j+1]
			flag = 1
		elif flag == 1:
			break

	if flag == 0:
		print "Not found"
		flag = 0
