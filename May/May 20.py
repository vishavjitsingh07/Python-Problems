class Solution:
    def maximizeWin(self, arr: List[int], k: int) -> int:
        n = len(arr)
        best = [0]*(n+1)  # best segment after >= i 
        res = 0
        for i in range(n-1,-1,-1):   # curr seg start at ith
            print(best)
            e = bisect.bisect_right(arr,arr[i]+k)   # take maximum as possible
            res = max(res,e-i + best[e])  # maximize the segments by curr seg + next segment after >= e
            print(res, e, e-i, best[e])
            best[i] = max(best[i+1],e-i)  # track the best segment
        print(best)
        return res
