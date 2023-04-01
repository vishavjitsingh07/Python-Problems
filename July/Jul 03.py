class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x, n = bisect_left(nums, target), len(nums)
        return x if (x<n and nums[x] == target) else -1
