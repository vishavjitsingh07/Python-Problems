class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        evenSum, oddSum = sum([nums[i] for i in range(n) if i%2 == 0]), sum([nums[i] for i in range(n) if i%2 == 1])
        totalSum = evenSum + oddSum
        currEven = currOdd = count = 0
        for i in range(n):
            if i%2 == 0:
                evenSum -= nums[i]
                if currEven + oddSum == currOdd + evenSum:
                    count+=1
                currEven+=nums[i]
            else:
                oddSum -= nums[i]
                if currEven + oddSum == currOdd + evenSum:
                    count+=1
                currOdd+=nums[i]
        return count
