def rFunction(a,e):
	result = 0
	for n in range(0, a**e):
		x = ((a-1)**n + (a+1)**n) % a**e
		if x > result:
			result = x
		if x < result
	return result

def sillySum(A,e):
	result = 0
	for a in range(1,A+1):
		result += rFunction(a,e)
	return result % (10**9 + 7)

T = int(raw_input())

for t in range(T):
	A,e = map(int, raw_input().split())

	print sillySum(A,e)