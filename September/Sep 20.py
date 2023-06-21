class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def solve(mid):
            return sum([abs(nums[i] - mid)*cost[i] for i in range(len(nums))])
        left = min(nums)
        right = max(nums)
        while left<right:
            mid = (left + right)//2
            if solve(mid)<solve(mid+1): right = mid
            else: left = mid+1
            
        return solve(left)
