def helper(n, arr, cost, k, brokenArr, d):
    ans = 0
    for i in brokenArr:
        arr.remove(d[i])
        
    ans = 0
    for idx, i in enumerate(arr):
        cost-= i
        if cost<0: return idx
    return len(arr)

from collections import defaultdict
class Solution:
    def maximumToys(self,N,A,Q,Queries):
        ans = []
        d = defaultdict(int)
        for i in range(1, N+1):
            d[i] = A[i-1]
        A.sort()
        for i in range(Q):
            temp = A.copy()
            ans.append(helper(N, temp, Queries[i][0], Queries[i][1], Queries[i][2:], d))
        return ans
