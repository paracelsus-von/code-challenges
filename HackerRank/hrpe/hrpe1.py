# Enter your code here. Read input from STDIN. Print output to STDOUT

def apSum(n,a,d):
	""" n is the number of terms
		a is the first term
		d is the difference between terms"""
	l = a + (n-1)*d
	return (n * (a + l)) / 2

T = int(raw_input())



for j in range(T):

#AP (arithmetic progression) sum formula
	i = long(raw_input())
	amt = 0
	
	if i > 3:
		n = (i-1) / 3
		a = 3
		d = 3
	
		amt += apSum(n,a,d)
	
	if i > 5:
		n = (i-1) / 5
		a = 5
		d = 5
	
		amt += apSum(n,a,d)
	
	if i > 15:
		n = (i-1) / 15
		a = 15
		d = 15
	
		amt -= apSum(n,a,d)
	print int(amt)
	