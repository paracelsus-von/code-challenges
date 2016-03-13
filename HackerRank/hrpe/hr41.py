n = int(raw_input())
times = map(int, raw_input().split())

x = times[0]
A = [[] for _ in range(times[n-1])]

utimes = list(set(times))

for t in utimes:
	A[t - 1].append(t)
	A[t-1].append(times.count(t))

A[:] = (value for value in A if value != [])

y = times[n-1]
overlap = 0
j = 0

while j < len(A) - 1:
	overlap += (A[j][1] + x + overlap - A[j+1][0])
	j += 1

if overlap > 0:
	y += overlap
else:
	y += (times.count(times[n-1]) - 1)

print y