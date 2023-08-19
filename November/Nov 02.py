class Solution:
    def subArraySum(self,arr, n, target):
        if target == 0: return (-1, )
        currSum, d = 0, {0 : 0}
        for i in range(n):
            currSum += arr[i]
            d[currSum] = i+1
            if currSum - target in d: return (d[currSum - target]+1, i+1)
        return (-1, ) 
