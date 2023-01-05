class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        total = 1
        prev = points[0]
        for s, e in points[1:]:
            if s>prev[1]:
                total+=1
                prev = [s, e]
            else: prev[1] = min(e, prev[1])
        return total
