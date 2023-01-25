class Solution:
    def minOperation(self, s):
        if len(s)<=1: return len(s)
        
        minOper = 0
        ans = ""
        n = len(s)
        for i in s:
            if ans and 2*len(ans)<n and 2*ans == s[:2*len(ans)]:
                minOper = len(ans)
            ans+= i
            
        return len(ans) - minOper + 1 if minOper>0 else n
