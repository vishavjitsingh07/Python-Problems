class Solution:
    def countPaths (self, N):
        lastVal, val, mod = 0, -3, 10**9 + 7
        for i in range(1, N):
            val = -val
            lastVal = (3*lastVal + val) % mod
        return lastVal % mod
        
