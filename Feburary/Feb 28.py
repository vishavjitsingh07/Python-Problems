class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        s = " "+ s
        n = len(s)
        while s and 0<=i<n-1:
            if s[i]!= s[i+1] and (s[i] == s[i+1].upper() or s[i].upper() == s[i+1]):
                s = s[:i] + s[i+2:]
                n = len(s)
                i = i-1
            else:
                i+=1
        return s[1:]
