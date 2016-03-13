# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input().strip())

for t in range(T):
    x = int(raw_input().strip())
    ans = ''
    i = 0
    j = 0
    
    while j <= x:
        j = 2**i
        i += 1
    
    i -= 2
    
    while i >= 0:
        j = 2**i
        if x >= j and x != 0 and x != 1:
            ans = ans + '1'
            x -= j
        elif i == 0 and (x == 0 or x == 1):
            ans = ans + str(x)
        else:
            ans = ans + '0'
        i -= 1
    
    print ans