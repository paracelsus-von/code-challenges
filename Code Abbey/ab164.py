import random

count = map(int, raw_input().split())
nodes = count[0]
edges = count[1]

A = [[] for _ in range(nodes)]
i = 0

# creates list with ith entry containing all nodes i can visit
while i < edges:
	e = map(int, raw_input().split())
	A[e[0]].append(e[1])
	i += 1

print A

amount = int(raw_input("How many runs do you want for each node? "))
run = int(raw_input("How long a run do you want? "))

C = [0 for _ in range(nodes)]

l = 0
			
while l < nodes:
	k = 0
	while k < amount:
		start = l
		j = 0
		while j < run:
# insert if else here in case there are no edges
			start = random.choice(A[start])
			j += 1
		C[start] += 1
		k += 1
	l += 1
	
print ' '.join(str(c) for c in C)