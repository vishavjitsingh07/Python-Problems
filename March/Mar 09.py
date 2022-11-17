class Solution:
	def countSubarray(self,arr, n, k):
	    lastMax, ans = -1, 0
        for i in range(n):
            if arr[i]>k:
                ans += (i- lastMax)*(n-i)
                lastMax = i
        return ans
