import os
import time
import sys

text = raw_input()


for i in range(100):
	time.sleep(0.5)
	os.system('cls')
	if (i % 20) < 10:
		y = "\n" * (i % 10)
	else:
		y = "\n" * ((-i -1) % 10)
	
	if (i % 20) < 10:
		x = "  " * (i % 10)
	else:
		y = "  " * ((-i -1) % 10)
	x = '   ' * (i % 10)
	sys.stdout.write(y) 
	sys.stdout.write(x)
	sys.stdout.write(text)
	sys.stdout.flush()