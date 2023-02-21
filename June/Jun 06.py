class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(0)
        right = n
        left = 0
        mid = (left + right) // 2
        while right>left:
            mid = (left + right) // 2
            if (nums[mid+1] != nums[mid]) and (nums[mid-1] != nums[mid]): return nums[mid]
            elif mid%2 == 0:
                if nums[mid+1] == nums[mid]: left = mid+1
                else: right = mid
            else:
                if nums[mid-1] == nums[mid]: left = mid +1
                else: right = mid
        return nums[mid]
