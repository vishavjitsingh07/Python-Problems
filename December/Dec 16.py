#User function Template for python3
def solve(s, k):
    ct = 0
    d = {}
    j = 0
    i = 0
    n = len(s)
    for i in range(n):
        if i<n:
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
            
        while len(d)>k:
            d[s[j]] -= 1
            if d[s[j]] == 0:
                del d[s[j]]
            j = j + 1
            
        ct += i-j+1
       
        
    return ct

class Solution:
    def substrCount (self,s, k):
        return solve(s, k)-solve(s, k-1)
