class Person:
	def __init__(self,initial_Age):
		if initial_Age < 0:
			print "This person is not valid, setting age to 0."
			age = 0

	def amIOld(self):
		if age < 13:
			print "You are young."
		elif age < 18:
			print "You are a teenager."
		else:
			print "You are old."

# Need to declare age a global variable or
# Python will interpret it as a local variable
# specific to this function.
	def yearPasses(self):
		global age
		age += 1


T = int(raw_input())

for i in range(0,T):
	age = int(raw_input())
	p = Person(age)
	p.amIOld()
	for j in range(0,3):
		p.yearPasses();
	p.amIOld();
	print ""