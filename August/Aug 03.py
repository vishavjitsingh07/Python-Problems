class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        c = 0
        for i in nums:
            c += 1 if i<0 else 0
        return -1 if c%2 == 1 else 1
