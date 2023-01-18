class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        best, s, N = max(nums), sum(nums), len(nums)
        def kadans(nums):
            curr, maxSum = 0, float('-inf')
            for i in nums:
                curr+=i
                maxSum = max(curr, maxSum)
                curr = max(curr, 0)
            return maxSum

        best = max(best, kadans(nums))
        if any(x>=0 for x in nums):
            best_neg = kadans([-x for x in nums])
            best = max(best, s + best_neg)
        return best
