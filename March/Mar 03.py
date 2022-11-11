s = set()
s2 = set()
def checkPrime(n):
    if n in s: return True
    if n in s2: return False
    i = 2
    while i<=n**(1/2):
        if n%i == 0: 
            s2.add(n)
            return False
        i+=1
    s.add(n)
    return True
    
class Solution:
    def isSumOfTwo (self, N):
        for i in range(2, N//2 + 1):
            if checkPrime(i) and checkPrime(N-i): return "Yes"
        return "No"
