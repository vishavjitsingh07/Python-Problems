class Solution:
    def noConseBits(self, n : int) -> int:
        n = list(str(bin(n))[2:])
        k = len(n)
        for i in range(2, k):
            if n[i] == n[i-1] == n[i-2] == "1":
                n[i] = "0"
        return int("".join(n), 2)
