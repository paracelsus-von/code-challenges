T = int(raw_input())
N = []

for i in range(T):
	N.append(long(raw_input()))

ans = sum(N)
ans2 = ans
length = 1

while ans2 > 9:
	ans2 /= 10
	length += 1

result = ''

for j in range(10):
	result += str((ans/10**(length - j - 1)) % 10)

print result