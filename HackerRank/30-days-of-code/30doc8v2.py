import sys

N = int(raw_input().strip())

Q = []

for i in range(2*N):
	Q.append(raw_input().strip())


for line in sys.stdin:
	flag = 0

	for j in (0,len(Q)-2,2):
		if line == Q[j]:
			print Q[j] + '=' + Q[j+1]
			flag = 1
			break

	if flag == 0:
		print "Not found"
		flag = 0
