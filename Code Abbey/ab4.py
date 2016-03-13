count = int(raw_input())
i = 0
A = ''

while i < count:
	x = map(int, raw_input().split())
	A = A + str(min(x)) + ' '
	i += 1

print A