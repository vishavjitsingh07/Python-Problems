class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [10**9] *(n+1)

        def dfs(i):
            if i>=n:
                return 0
            if dp[i]!=10**9:
                return dp[i]
            dp[i] = stoneValue[i]-dfs(i+1)
            if i+2<=n:
                dp[i] = max(dp[i], stoneValue[i]+stoneValue[i+1]-dfs(i+2))
            if i+3<=n:
                dp[i] = max(dp[i], stoneValue[i]+stoneValue[i+1]+stoneValue[i+2]-dfs(i+3))

            return dp[i]

        ans = dfs(0)
        if ans>0:
            return "Alice"
        elif ans<0:
            return "Bob"
        else:
            return "Tie"

        
