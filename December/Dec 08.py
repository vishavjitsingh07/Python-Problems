class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        d = {0 : [], 1 : []}
        for i in nums:
            d[i%2].append(i)
        return d[0] + d[1]
        
