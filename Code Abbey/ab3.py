# sums a listed amount of pairs of integers

count = int(raw_input("How many tuples of numbers do you want to sum? "))

i = 0
A = []

while i < count:

	A.append(sum(map(int, raw_input().split())))
	
	i += 1

print ' '.join(str(a) for a in A)