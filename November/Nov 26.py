from functools import lru_cache
class Solution:
    def countWays(self,n):
        @lru_cache(None)
        def solve(n):
            if n==0:
                return 1
            if n<0:
                return 0
            return (solve(n-1)%m+solve(n-2)%m+solve(n-3)%m)%m
        m=10**9+7
        return solve(n)
