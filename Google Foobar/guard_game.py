def singleDigit(n):
	# takes an integer input n and returns the sum of its digits mod 10
	n = str(n)
	A = []
	for number in n:
		A.append(int(number))
	return sum(A) % 10

n = raw_input()
print singleDigit(n)