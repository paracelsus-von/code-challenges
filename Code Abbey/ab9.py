# Triangles
# Idea: Largest length must be <= sum of other two lengths

count = int(raw_input())

i = 0
A = []

while i < count:

	tri = map(int, raw_input().split())

	tri.sort()

	if tri[2] <= tri[0] + tri[1]:
		A.append(1)
	else:
		A.append(0)
	
	i += 1

print ' '.join(str(a) for a in A)