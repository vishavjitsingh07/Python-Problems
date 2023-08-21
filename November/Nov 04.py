class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s1=s+s
        s1=s1[1:-1]
        return (s in s1)
