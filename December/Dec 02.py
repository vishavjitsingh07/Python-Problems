class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1 = Counter(t)
        s2 = Counter(s)
        for i in s:
            if (i not in s1) or s1[i] < s2[i]:
                return False
            
        n = len(s)
        m = len(t)
        i = 0
        j = 0
        while i<n and j<m:
            if s[i] == t[j]:
                i+=1
            j+=1
        return i == n
            
            
        
