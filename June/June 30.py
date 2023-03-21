class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = c = 0
        for i in nums:
            if i == 0: c+=1
            else: c = 0
            ans+=c
        return ans
