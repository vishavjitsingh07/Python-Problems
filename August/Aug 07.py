from typing import List


class Solution:
    def solve(self,n,k,target,coins,dp):
        if k==0 and target==0:
            return True
        if dp[k][target]!=-1:
            return dp[k][target]
        ans=False
        for i in range(n):
            if target>=coins[i] and k-1>=0:
                ans|=self.solve(n,k-1,target-coins[i],coins,dp)
        dp[k][target]=ans
        return dp[k][target]
    def makeChanges(self, N : int, K : int, target : int, coins : List[int]) -> bool:
        dp=[[-1 for i in range(target+1)] for j in range(K+1)]
        return self.solve(N,K,target,coins,dp)
