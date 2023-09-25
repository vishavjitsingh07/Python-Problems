class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = Counter(s)
        s2 = Counter(t)
        for i in s2:
            if s1[i] != s2[i]:
                return i
