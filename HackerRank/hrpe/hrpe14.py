def collatzSeq(n):
	"""Returns the Collatz Sequence of n."""
	C = []
	if n == 1:
		return [1]
	C.append(n)
	while n != 1:
		if n%2 == 0:
			n = n/2
		else:
			n = 3*n + 1
		C.append(n)
	return C

def collatzSeqLens(n):
	"""Returns the lengths of all CollatzSequences of numbers <=n."""
	L = []
	for i in range(n+1):
		L.append(len(collatzSeq(i))
	return L

T = int(raw_input())

currmaxlength = 1
currmaxstart = 1

for i in range(T):
	N = int(raw_input())
	

	if currmaxstart > N:
		currmaxlength = 1
		currmaxstart = 1
		for j in range(1,N+1):
			currlength = len(collatzSeq(j))
			if currlength >= currmaxlength:
				currmaxlength = currlength
				currmaxstart = j
	
	else:
		for j in range(currmaxstart,N+1):
			currlength = len(collatzSeq(j))
			if currlength >= currmaxlength:
				currmaxlength = currlength
				currmaxstart = j
	print currmaxstart
	