class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        start, ans, end = 0, 0, len(nums)-1
        while start <= end:
            if nums[start] + nums[end] <= limit: start += 1
            end, ans = end -1, ans+1
        return ans
