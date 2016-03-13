sent = raw_input()
for i in len(sent):
	sent.append(sent[i])
	sent.pop(i)

#built in function:
# reverse(raw_input())