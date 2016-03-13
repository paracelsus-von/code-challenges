x = map(int, raw_input())

initial_Age = x(1)

T = x(0)

for

if initial_Age < 0:
	print "This person is not valid, setting age to 0."
	initial_Age = 0

age = initial_Age

if age < 13:
	print "You are young."
elif age < 18:
	print "You are a teenager."
else:
	print "You are old"

yearPasses = age + 1