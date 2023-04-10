from collections import defaultdict
class Solution: 
    def maxIntersections(self, lines, N):
        a = defaultdict(int)
        for j in lines:
            a[j[0]]+=1
            a[j[1]+1]-=1
        pas=0
        maax=1
        for i in sorted(a):
            pas+=a[i]
            maax=max(maax,pas)
        return maax
