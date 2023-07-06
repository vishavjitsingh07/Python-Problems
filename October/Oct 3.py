class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen, l, currSum = float('inf'), 0, 0
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                minLen = min(minLen, r - l + 1)
                currSum -= nums[l]
                l += 1
        return minLen if minLen != float('inf') else 0
