from collections import defaultdict
class Solution():
    def maxWeightCell(self, N, Edge):
        if N == 1: return 0
        d = defaultdict(int)
        currMax, res = 0, 0
        for idx, i in enumerate(Edge):
            d[i]+=idx
            if d[i]>=currMax:
                res = i
                currMax = d[i]
        return res
