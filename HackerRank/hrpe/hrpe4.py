T = int(raw_input())

def palindromeList(n):
	root = int(n**0.5)
	for i in range(1000 - root,900):
		i = 1000-i
		for j in range(101, root+1):
			print int(str(i*j)[::-1]), i*j
			if i*j <= n and int(str(i*j)[::-1]) == i*j:
				return i*j

for i in range(T):
	palindromeList(i)