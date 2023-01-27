class Solution:
	def CountWays(self, s):
	    mod = 10**9+7
        if len(s)<=1: return len(s)
        for i in ['30', '40', '50', '60', '70','80', '90', "00"]:
            if i in s: return 0
        
        n = len(s)
        dp = [0]*(n)
        dp[0] = 1
        if 11<=int(s[:2])<=26:
            dp[1] = 2
        else:
            dp[1] = 1 
            
        for idx in range(2, n):
            if 11<= int(s[idx-1:idx+1]) <=26:
                dp[idx] = dp[idx-1] + dp[idx-2]
            elif s[idx] == "0":
                dp[idx] = dp[idx-1] = dp[idx-2]
            else:
                dp[idx] = dp[idx-1]
        return dp[-1]%mod
