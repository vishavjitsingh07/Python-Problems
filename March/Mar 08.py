from collections import defaultdict
class Solution:
    def beautySum(self, s):
        res = 0
        n = len(s)
        d = defaultdict(int)
        
        for i in range(n):
            d[s[i]] +=1
            for j in range(i+1, n):
                d[s[j]] +=1
                res += max(d.values()) - min(d.values())
            d = defaultdict(int)
            
        return res
