class Solution:
    def findSubArrays(self,arr,n):
        d ={0:1}
        currSum = 0
        ans = 0
        arr.append(float('inf'))
        for i in arr:
            currSum += i
            if currSum in d:
                ans+=d[currSum]
                d[currSum] +=1
            else: d[currSum] = 1
            
        return ans
            
