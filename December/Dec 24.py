class Solution(object):
    def minCostClimbingStairs(self, cost):
            n = len(cost)
            dp = [0]*n
            dp[:2] = cost[:2]
            for i in range(2, n):
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            return min(dp[-2:])
