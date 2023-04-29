class Solution:
    def findNumber(self, N : int) -> int:
        if N == 0:
            return 0
        N -= 1
        return 10*self.findNumber(N//5) + 2*(N%5) + 1ˇ
