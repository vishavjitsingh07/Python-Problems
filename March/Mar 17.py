class Solution:
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:    
        n = len(start)
        arr = sorted(zip(start, end, profit))
        @lru_cache
        def rec(i):
            if i>=n: return 0
            j = i+1
            while j<n and arr[i][1]>arr[j][0]:
                j+=1
            
            a = arr[i][2] + rec(j)
            b = rec(i+1)
            return max(a, b)
        return rec(0)
