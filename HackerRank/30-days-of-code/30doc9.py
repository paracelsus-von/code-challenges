def find_gcd(a,b):
    #write base condition
    if a == b:
        return a
    else:
        return find_gcd(max(a,b) - min(a,b),min(a,b))
    
#Take input
x = map(int,raw_input().strip().split())
a = x[0]
b = x[1]

gcd=find_gcd(a,b)

print gcd
    
# Possibly more efficient:

def find_gcd(a,b):
    #write base condition
    mx = max(a,b)
    mn = min(a,b)
    if mx % mn == 0:
        return mn
    else:
        return find_gcd(mx - mn,mn)
    
#Take input
x = map(int,raw_input().strip().split())
a = x[0]
b = x[1]

gcd=find_gcd(a,b)

print gcd
    
