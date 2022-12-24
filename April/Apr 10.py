class Solution:
    def numTilings(self, n: int) -> int:
        if n <=2: return n
        a, b, c, d = (0, 1, 2, 5)
        for i in range(3, n):
            a = d * 2 + b
            b = c
            c = d
            d = a

        mod = 10 ** 9 + 7
        return d%mod
