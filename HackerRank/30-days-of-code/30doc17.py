#Write your code here
class Calculator:
    def __init__(self):
        pass
        
    def power(self, n, p):
        self.n = n
        self.p = p
        if self.n < 0 or self.p < 0:
            return 'n and p should be non-negative'
        else:
            return self.n**self.p
myCalculator=Calculator()
T=int(raw_input())
for i in range(T):
    n,p = map(int, raw_input().split())
    try:
        ans=myCalculator.power(n,p)
        print ans
    except Exception,e:
        print e    
    