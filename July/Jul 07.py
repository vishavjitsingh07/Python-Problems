from collections import Counter
class Solution:
    def countSpecialNumbers(self, N, arr):
        c = Counter(arr)
        ans = set()
        count = 0
        for i in sorted(c.keys()):
            if c[i]>1: 
                count+=c[i]
                ans.add(i)
                continue
            for j in ans:
                if i%j == 0:
                    count+=1
                    break
            ans.add(i)
        return count
        
