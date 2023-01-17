class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero, one = s.count('0'), 0
        ans = zero
        for i in s:
            if i == "0": zero-=1
            if i == "1": one+=1
            ans = min(ans, zero + one)
        return ans
