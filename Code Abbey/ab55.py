wordlist = raw_input().split()

wordlist.sort()

A = []
i = 0

while i < len(wordlist) - 1:
	if wordlist[i] == wordlist[i+1]:
		A.append(wordlist[i])
		i += 2
	else:
		i += 1

j = 0
while j < len(A) - 1:
	if A[j] == A[j+1]:
		A.pop(j)
	j += 1
	
print ' '.join(str(a) for a in A)