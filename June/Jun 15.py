class Solution:
    def minCost(self, arr) :
        n = len(costs)
        k = len(costs[0])
        
        if k <= 1 and n > 1:
            return -1
        
        dp = [[-1 for j in range(k)] for i in range(n)]
        
        min1 = float("inf")
        min2 = float("inf")
        
        for j in range(k):
            dp[0][j] = costs[0][j]
            if costs[0][j] < min1:
                min2 = min1
                min1 = costs[0][j]
            elif costs[0][j] < min2:
                min2 = costs[0][j]
                
        for i in range(1, n):
            newmin1 = float("inf")
            newmin2 = float("inf")
            for j in range(k):
                if min1 == dp[i-1][j]:
                    dp[i][j] = min2 + costs[i][j]
                else:
                    dp[i][j] = min1 + costs[i][j]
                    
                if dp[i][j] < newmin1:
                    newmin2 = newmin1
                    newmin1 = dp[i][j]
                elif dp[i][j] < newmin2:
                    newmin2 = dp[i][j]
                    
            min1 = newmin1
            min2 = newmin2
            
        return min1
