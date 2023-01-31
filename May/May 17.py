class Solution:
    def minRepeats(self, A, B):
        n = max(len(B)//len(A), 1)
        if B in A*n: return n
        if B in A*(n+1): return n+1
        return -1
