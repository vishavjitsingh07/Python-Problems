class Solution:
    def numSquares(self, n: int) -> int:
        if n<4: return n
        
        dp = [float("inf") for _ in range(n+1)] 
        sqrNos = []
        for i in range(int(n**.5)+1):
            sqrNos.append(i**2)

        dp[0], dp[1], dp[2] = 0, 1, 2
        for i in range(n+1):
            for j in sqrNos:
                if i-j>=0:
                    dp[i] = min(dp[i], dp[i-j]+1)

        return dp[n]
