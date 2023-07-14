class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        d = {}
        for i in arr:
            d[i] = d.get(i - diff, 0)+1
        return max(d.values())
