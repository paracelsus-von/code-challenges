# sums a listed amount of integers

count = int(raw_input("How many pairs of numbers do you want to sum? "))

i = 0
A = ''

while i < count:

	num = raw_input("Can you list them? ")
	num = num.split()
	num = map(int, num)
	
	A = A + str(sum(num)) + ' '
	
	i += 1

# shorter
# num = map(int, raw_input().split())

print A