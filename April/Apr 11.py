from typing import List
from functools import lru_cache
import sys
class Solution:
    def maxCoins(self, N : int, arr : List[int]) -> int:
        arr.append(1)
        arr.insert(0,1)

        @lru_cache(None)
        def solve(i,j):
            if i>j: return 0
            mx = -sys.maxsize
            for k in range(i,j+1):
                temp = arr[i-1]*arr[k]*arr[j+1] + solve(i,k-1)+solve(k+1,j)
                mx= max(mx,temp)
            return mx
        return solve(1,N)
