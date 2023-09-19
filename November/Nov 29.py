class Solution:
    def getFirstSetBit(self,n):
        if n == 0: return 0
        count = 1
        while True:
            if n&1 == 1: break
            n = n>>1
            count+=1
            
        return count
