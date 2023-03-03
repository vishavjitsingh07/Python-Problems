import math
class Solution:
    def minimumSquares(self, L, B):
        side = math.gcd(L, B)
        return L*B//side**2, side
