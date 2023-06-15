#User function Template for python3

class Solution:
    def lp(self,s,l,r):
        n=len(s)
        while r<n and l>=0:
            if s[l]!=s[r]:break
            l, r = l-1, r+1
        return l+1 , r
        
    def longestPalin(self, S):
        s = S
        n = len(s)
        start,end =0,0
        for i in range(n):
            l, r = self.lp(S,i,i)
            if (r-l)>(end-start):
                end, start = r, l
            l, r = self.lp(S,i,i+1)
            if (r-l)>(end-start):
                end, start = r, l

        return s[start:end] 
        # code here
