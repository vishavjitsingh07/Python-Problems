class Solution:
    def minDifference(self, arr, n):
        # code here
        s = sum(arr)
        dp = [True] + [False] * s
        ans = s
        for i in arr:
            for j in range(s-i, -1, -1):
                if dp[j]:
                    dp[j+i] = True
                    ans = min(ans, abs(j+i-s+j+i))
        return ans
