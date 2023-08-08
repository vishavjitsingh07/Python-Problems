class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        n = len(nums)
        j = n-1
        mid = n//2
        midL = mid
        midR = mid
        while i<=midL:
            if nums[i] == target:return i
            if nums[j] == target: return j
            if nums[midL] == target: return midL
            if nums[midR] == target: return midR
            i +=1
            j -=1
            midL -=1
            midR +=1
        return -1
