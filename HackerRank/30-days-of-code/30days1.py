A = [5.35, 'a', False, 100, "I am a code monkey", True, 17.3, 'c', "derp"]

for a in A:
	t = type(a)
	if t == str and len(a) == 1:
		t = 'char'
	elif t == str:
		t = 'String'
	elif t == int:
		t = 'int'
	elif t == bool:
		t = 'boolean'
	elif t == float:
		t = 'double'
	
	if t == 'String' or t == 'Array':
		tt = 'Referenced'
	else:
		tt = 'Primitive'
	print tt, ":", t