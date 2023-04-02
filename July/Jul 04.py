class Solution:
    def successfulPairs(self, s: List[int], p: List[int], success: int) -> List[int]:
        p.sort()
        return [len(p) - bisect_left(p, success/ x) for x in s]
