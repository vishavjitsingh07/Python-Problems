class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos = lastPos = jump = 0
        for i in range(n-1):
            maxPos = max(maxPos, i + nums[i])
            if i == lastPos:
                jump+=1
                lastPos = maxPos
        return jump
