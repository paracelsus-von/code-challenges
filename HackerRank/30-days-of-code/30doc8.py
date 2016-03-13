N = int(raw_input().strip())

Q = []

for i in range(2*N):
	Q.append(raw_input().strip())

while True:
	curr = raw_input().strip()
	
	if curr.strip() == "":
		break

	flag = 0

	for j in (0,len(Q)-2,2):
		if curr == Q[j]:
			print Q[j] + '=' + Q[j+1]
			flag += 1

	if flag == 0:
		print "Not found"
		flag = 0
