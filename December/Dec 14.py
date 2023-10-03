class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans = 0
        for i in c.values():
            ans+= ((i * (i-1))//2)
        return ans
