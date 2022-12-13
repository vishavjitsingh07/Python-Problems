#User function Template for python3

class Solution:
    def splitArray(self, arr, n, K):
        # code here 
        def fun(mid):
            subarray = 0
            curSum = 0
            for i in arr:
                curSum+=i
                if curSum>mid:
                    subarray+=1
                    curSum=i
            return subarray+1<=K
        l,r=max(arr),sum(arr)
        res = r
        while l<=r:
            mid = l+r>>1
            if fun(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res
        
