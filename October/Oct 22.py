class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*n
        dp[0] = s[0] in wordDict
        for i in range(1,n):
            dp[i] = s[0:i+1] in wordDict
            for j in range(i):
                dp[i] = dp[i] or (dp[i-j-1] and (s[i-j:i+1] in wordDict))
        return dp[n-1]
